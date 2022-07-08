# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    def get_id(self):
        print(self.id)
        return self.id
    
    @api.model
    def create(self,values):
        # your logic goes here
        print("entra aquí")
        print(get_id())
        #print(values)
        #product_info={'product_tmpl_id':values['id']}
        #self.env['mta.producto'].create(product_info)
        override_create = super(ProductProduct,self).create(values)
        return override_create