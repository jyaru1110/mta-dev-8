# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    #save when qty available is updated
    
    @api.model
    def create(self,values):
        override_create = super(StockQuant,self).create(values)
        if(override_create.location_id.id==14):
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',override_create.product_id.id)])
        if(override_create.location_id.id==4):
        #self.env['changes.time'].create({'product_tmpl_id':override_create.id})
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',override_create.product_id.id)])
            oc_actual = producto_mta.oc
            producto_mta.oc = oc_actual - override_create.inventory_diff_quantity
            self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':producto_mta.qty_available+override_create.inventory_diff_quantity,'buffer_size':producto_mta.buffer_size,'type':'available'})
            
        if(override_create.location_id.id==5):
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',override_create.product_id.id)])
            self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':producto_mta.qty_available+override_create.inventory_diff_quantity,'buffer_size':producto_mta.buffer_size,'type':'available'})
        return override_create
    
    def write(self,values):
        old_inventory_quantity_auto_apply = self._origin.inventory_quantity_auto_apply
        override_write = super(StockQuant,self).write(values)
        if(self._origin.location_id.id==14):
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.product_id.id)])
            self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':self._origin.inventory_quantity_auto_apply*-1,'buffer_size':producto_mta.buffer_size,'type':'available'})
            
        dif = self._origin.inventory_quantity_auto_apply - old_inventory_quantity_auto_apply
        if self._origin.location_id.id==4:
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.product_id.id)])
            oc_actual = producto_mta.oc
            producto_mta.oc = oc_actual + dif
            self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':producto_mta.qty_available-dif,'buffer_size':producto_mta.buffer_size,'type':'available'})
        if self._origin.location_id.id==5:
            producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.product_id.id)])
            self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':producto_mta.qty_available-dif,'buffer_size':producto_mta.buffer_size,'type':'available'})
        return override_write