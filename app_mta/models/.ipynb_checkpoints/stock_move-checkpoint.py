# -*- coding utf-8 -*- 
from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'
    
    @api.model
    def create(self,values):
        override_create = super(StockMove,self).create(values)
        if(override_create.reference[0:6]=='WH/IN/'):
            producto = self.env['mta.producto'].search([('product_tmpl_id','=',values['product_id'])])
            oc_actual = producto.oc
            producto.oc = oc_actual + values['product_uom_qty']
            
        return override_create