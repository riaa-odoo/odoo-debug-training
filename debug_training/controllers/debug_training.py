from odoo import http


class Compare(http.Controller):
    @http.route(["/get-shoe-sales"], type="json", auth="public", website=True)
    def get_mileage(self):
        order_lines = http.request.env["sale.order.line"].search([("order_id.state", "=", "sale"),
                                                                  ("product_template_id.detailed_type", "=", "shoes")])
        total_sales = sum(order_lines.mapped("price_total"))
        return {"total_sales": total_sales}

    @http.route("/compare", auth="public", website=True)
    def index(self):
        templates = http.request.env["product.template"].search([("detailed_type", "=", "shoes")])
        return http.request.render("debug_training.compare_website", {"templates": templates})
