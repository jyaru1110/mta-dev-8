# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    @api.model
    def create(self,values):
        # your logic goes here
        producto = self.env['mta.producto'].browse(values['product_id'])
        oc_actual = producto.oc
        print('OC_ACTUAL: ',oc_actual)
        print('producto.oc: ',producto.oc)
        producto.oc = oc_actual + values['product_uom_qty']
        print('producto.oc 2: ',producto.oc)
        override_create = super(StockMove,self).create(values)
        return override_create