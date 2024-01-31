# Odoo 17.0 - Debug Training
*By Ricardo Alonso*
## Bugs
### [IMP] debug_training: Added pair_per_case and price_per_pair fields
The computation on 'list_price' applies for all product templates, but it should only apply for products that have both of these fields set (greater than 0).
### [IMP] debug_training: Added 'Compare' website page
Field 'price' is referenced on the web QWeb template, but it doesn't exist on the 'product.template' (should use 'list_price' instead).
### [IMP] debug_training: Added 'Shoe Sales' snippet
In the snippet, we are tying to access the 'sales' attribute on the values, but it doesn't exist (use 'total_sales' instead).
