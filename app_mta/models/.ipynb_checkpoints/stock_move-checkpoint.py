# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    @api.model
    def create(self,values):
        # your logic goes here
        producto = self.env['mta.producto'].browse(self.product_id.id)
        print(self.product_id.ola)
        if producto:
            print('encontrado')
        oc_actual = producto.oc
        producto.oc = oc_actual + self.product_uom_qty
        override_create = super(StockMove,self).create(values)
        return override_create