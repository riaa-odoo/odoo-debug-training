{
    "name": "Debug Training",
    "summary": "Debug Odoo Framework (Py, XML and JS) using VSCode and Chrome",
    "description": """
        Debug Odoo Framework (Py, XML and JS) using VSCode and Chrome.
    """,
    "version": "1.0.0",
    "category": "Custom Developments",
    "license": "OPL-1",
    "author": "RIAA",
    "website": "www.odoo.com",
    "depends": ["product", "sale", "stock", "website"],
    "data": [
        "views/debug_training_templates.xml",
        "views/product_template_views.xml",
        "views/snippets/snippets.xml",
        "views/snippets/s_shoe_sales.xml",
    ],
}
