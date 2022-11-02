odoo.define('app_mta.CategoryScreen', function(require) {
  'use strict';
  const PosComponent = require('point_of_sale.PosComponent');
  const ProductScreen = require('point_of_sale.ProductScreen');
  const {useListener} = require('web.custom_hooks');
  const Registries = require('point_of_sale.Registries');
  class CategoryScreen extends PosComponent {
      api(){
           fetch('https://api-dev-dot-mada-dev.ue.r.appspot.com/api/creditosAfiliado/consultarPorFolio/?folio=A-00001-0011-NOP&afiliadoId=2&access_token=hJUjJT6bllOsfmdHwgxYWMC8r7X4BHDzBf4CXPWmDni0VPkD308WidX71MjEv27V').then((response) => response.json()).then((data) => 
                //this.$('.id-api').text(data.id);
                /*this.$('.folio-api').text(data.folio);
          this.$('.monto-api').text(data.monto);*/
          console.log(data);
           );
      }

      back() {
          this.trigger('close-temp-screen');
      }
  }
  CategoryScreen.template = 'CategoryScreen';
  Registries.Component.add(CategoryScreen);
  return CategoryScreen;
});