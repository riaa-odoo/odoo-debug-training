from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(selection_add=[("shoes","Shoes")], 
                            ondelete={"shoes": "set product"},
                            help="A storable product is a product for which you manage stock. The Inventory app has to be installed.\n"
                            "A consumable product is a product for which stock is not managed.\n"
                            "A service is a non-material product you provide.\n"
                            "Shoes are a captivating expression of personal style, comfort, and individuality.")
    list_price = fields.Float(
        "Sales Price", default=1.0,
        digits="Product Price",
        help="Price at which the product is sold to customers.",
        compute="_compute_list_price",
        store=True,
        readonly=False
    )
    pair_per_case = fields.Integer(
        "Pairs Per Case",
        help="Set the number of pairs each shoe case has for this product."
    )
    price_per_pair = fields.Monetary(
        "Price Per Pair",
        help="Set the price for a pair of this type of shoes."
    )

    @api.depends("pair_per_case", "price_per_pair")
    def _compute_list_price(self):
        for template in self.filtered(lambda t: t.pair_per_case > 0 and t.price_per_pair > 0):
            template.list_price = template.pair_per_case * template.price_per_pair

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping["shoes"] = "product"
        return type_mapping
