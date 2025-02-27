{
        "name": "Subscription Plan",
    "version": "17.0.1.0.0",
    "summary": "Manage subscription plans with automatic total price calculation.",
    "category": "Sales/Subscription",
    "author": "Muhammad Usman Hussain | Evolusion",
    "license": "OPL-1",
    "depends": ["base", 'sale_subscription'],
    "data": [
        "security/ir.model.access.csv",
        "views/subscription_view.xml",

    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
