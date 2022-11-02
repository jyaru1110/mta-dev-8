odoo.define('pos_custom_screen.CategoryControlButton', function (require) {
    'use strict';
    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');
    class CategoryControlButton extends PosComponent {
    }
    CategoryControlButton.template = 'pos_custom_screen.CategoryControlButton';
    ProductScreen.addControlButton({
        component: CategoryControlButton,
        condition: function () {
            return true;
        },
        position: ['before', 'SetPricelistButton'],
    });
    Registries.Component.add(CategoryControlButton);
    return CategoryControlButton;
});