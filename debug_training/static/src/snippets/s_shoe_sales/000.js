/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

const ShoeSalesWidget = publicWidget.Widget.extend({
    selector: ".s_shoe_sales",
    disabledInEditableMode: false,

    init() {
        this._super.apply(this, arguments);
        this.rpc = this.bindService("rpc");
    },

    start() {
        this.$wrapper = this.$(".s_shoe_sales_wrapper");
        this._render();
        return this._super(...arguments);
    },

    _render: async function () {
        var vals = await this.rpc("/get-shoe-sales");
        this.$wrapper.empty();
        this._drawText(vals);
    },

    _drawText: function (vals) {
        let textWrapper = $("<h3/>").attr({
            class: "s_shoe_sales_text_wrapper o_default_snippet_text",
        });
        textWrapper.text(`$${vals.total_sales.toLocaleString()}`);
        textWrapper.appendTo(this.$wrapper);
    },
});

publicWidget.registry.shoeSales = ShoeSalesWidget;

export default ShoeSalesWidget;
