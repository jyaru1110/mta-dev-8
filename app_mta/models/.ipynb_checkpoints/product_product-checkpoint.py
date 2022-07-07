# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    @api.model
    def create(self,values):
        # your logic goes here
        product_info = {'product_tmpl_id':self.id}
        self.env['mta.producto'].create(product_info)
        override_create = super(ProductProduct,self).create(values)
        return override_create