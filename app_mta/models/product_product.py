# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    
    @api.model
    def create(self,values):
        override_create = super(ProductProduct,self).create(values)
        product_info={'product_tmpl_id':override_create.id}
        self.env['mta.producto'].create(product_info)
        return override_create