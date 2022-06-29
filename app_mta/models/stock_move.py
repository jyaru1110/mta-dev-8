# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    @api.model
    def create(self,values):
        # your logic goes here
        producto = self.env['mta.producto'].search([('id', '=', self.product_id)])
        producto.oc = producto.oc + self.product_uom_qty
        override_create = super(your_model,self).create(values)
        return override_create