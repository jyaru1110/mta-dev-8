odoo.define('module_name.CategoryScreen', function(require) {
  'use strict';
  const PosComponent = require('point_of_sale.PosComponent');
  const ProductScreen = require('point_of_sale.ProductScreen');
  const {useListener} = require('web.custom_hooks');
  const Registries = require('point_of_sale.Registries');
  class CategoryScreen extends PosComponent {
      back() {
          this.trigger('close-temp-screen');
      }
  }
  CategoryScreen.template = 'CategoryScreen';
  Registries.Component.add(CategoryScreen);
  return CategoryScreen;
});