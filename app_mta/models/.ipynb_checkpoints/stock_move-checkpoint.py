# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    @api.model
    def create(self,values):
        # your logic goes here
        producto = self.env['mta.producto'].search([('product_tmpl_id','=',values['product_id'])])
        print(producto)
        print(producto.oc)
        oc_actual = producto.oc
        producto.oc = oc_actual + values['product_uom_qty']
        override_create = super(StockMove,self).create(values)
        return override_create