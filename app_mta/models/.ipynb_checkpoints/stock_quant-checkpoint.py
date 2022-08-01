# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    
    def write(self,values):
        override_write = super(StockQuant,self).write(values)
        if(self._origin.location_id.id==14):
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.product_id.id)])
            self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':self._origin.inventory_quantity_auto_apply*-1,'buffer_size':producto_mta.buffer_size,'type':'available'})
        return override_write