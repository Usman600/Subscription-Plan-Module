from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SubscriptionPlan(models.Model):
    _name = "subscription.plan"
    _description = "Subscription Plan"

    name = fields.Char(string="Plan Name", required=True)
    price = fields.Float(string="Monthly Price", required=True)
    duration_months = fields.Integer(string="Duration (Months)", required=True)
    total_price = fields.Float(string="Total Price", compute="_compute_total_price", store=True)
    discount_price = fields.Float(string="Discounted Price", compute="_compute_discount_price", store=True)
    is_discount_applied = fields.Boolean(string="Discount Applied", default=False)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('discounted', 'Discount Applied'),
    ], string="Status", default='draft', tracking=True)

    @api.depends('price', 'duration_months')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.price * record.duration_months

    @api.depends('is_discount_applied', 'price')
    def _compute_discount_price(self):
        for record in self:
            if record.is_discount_applied:
                record.discount_price = record.total_price * 0.9  # Apply 10% discount
            else:
                record.discount_price = 0.0  # No discount if button not clicked

    @api.constrains("duration_months")
    def _check_duration(self):
        for plan in self:
            if plan.duration_months <= 0:
                raise ValidationError("Duration must be greater than 0.")

    def action_open_discount_wizard(self):
        """Opens a wizard to confirm the discount."""
        return {
            'name': 'Confirm Discount',
            'type': 'ir.actions.act_window',
            'res_model': 'subscription.plan.discount.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_plan_id': self.id},
        }


class SubscriptionPlanDiscountWizard(models.TransientModel):
    _name = 'subscription.plan.discount.wizard'
    _description = 'Confirm Discount'

    plan_id = fields.Many2one('subscription.plan', string="Subscription Plan", required=True)

    def confirm_discount(self):
        """Apply discount and change status"""
        self.plan_id.write({
            'is_discount_applied': True,
            'status': 'discounted'
        })
        return {'type': 'ir.actions.act_window_close'}

    def cancel_discount(self):
        """Close wizard without applying discount"""
        return {'type': 'ir.actions.act_window_close'}
