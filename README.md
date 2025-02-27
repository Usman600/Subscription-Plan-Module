# Subscription Plan Module for Odoo 17

## Overview
This Odoo module allows businesses to manage subscription plans efficiently. It enables users to define different subscription plans with pricing, duration, and an automatically computed total price.

## Features
- Create subscription plans with name, price, and duration.
- Automatic calculation of the total subscription cost (price * duration).
- User-friendly tree and form views for managing subscriptions.
- Accessible from the "Subscriptions" menu in Odoo.

## Installation
1. Copy the module to your Odoo `custom_addons` directory.
2. Restart the Odoo server.
3. Activate the developer mode in Odoo.
4. Go to **Apps > Update Apps List** and install the **Subscription Plan** module.

## Usage
1. Navigate to **Subscriptions > Subscription Plans**.
2. Click on **Create** to define a new plan.
3. Fill in the details:
   - **Name**: Subscription plan name.
   - **Price**: Monthly price.
   - **Duration**: Number of months.
   - **Total Price**: Automatically computed (Price × Duration).
4. Save and manage subscription plans easily.

## Technical Details
- The model `subscription.plan` includes:
  - `name` (Char): Subscription plan name.
  - `price` (Float): Monthly price.
  - `duration_months` (Integer): Duration in months.
  - `total_price` (Computed Float): Auto-calculated total subscription cost.
  
- XML views for tree and form layouts.

## License
This module is licensed under the **Odoo Proprietary License**.

## Author
- **Developer**: Muhammad Usman Hussain 
- **Company**: Evolusion-tech  
- **Email**: usman@evolusiontech.com  
