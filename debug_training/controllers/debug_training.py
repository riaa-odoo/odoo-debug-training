from odoo import http


class Compare(http.Controller):
    @http.route("/compare", auth="public", website=True)
    def index(self):
        templates = http.request.env["product.template"].search([("detailed_type", "=", "shoes")])
        return http.request.render("debug_training.compare_website", {"templates": templates})
