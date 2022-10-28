# -*- coding utf-8 -*- 
from numpy import product
from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    @api.model
    def create(self,values):
        override_create = super(StockQuant,self).create(values)
        if(override_create.location_id.id==8):
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',override_create.product_id.id)])
            if producto_mta:
                self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':override_create.quantity,'buffer_size':producto_mta.buffer_size,'type':'available'})

            
        return override_create
        
    
    def write(self,values):
        old_inventory_quantity_auto_apply = self._origin.inventory_quantity_auto_apply
        qty_actual = self._origin.quantity
        override_write = super(StockQuant,self).write(values)
        if(self._origin.location_id.id==8 and qty_actual!=self._origin.quantity):
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.product_id.id)])
            if producto_mta:
                self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':self._origin.quantity,'buffer_size':producto_mta.buffer_size,'type':'available'})
        
        return override_write
        