# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductInventory(models.Model):
    _name = 'product.inventory'
    _inherits = {'product.template': 'product_id'}
    
    # Add a new column to the product.template model
    qty_ordered = fields.Integer(string='# Ordered')
    qty_transit = fields.Integer(string='# Transit')
    buffer_size = fields.Integer(string="Buffer Size",default=10)
    oc = fields.Integer(string="Orden de compra")
    bp_solicitud = fields.Integer(string="Buffer Penetration Solicitadas",
                                compute='_compute_bp_solicitud')
    bp_transito = fields.Integer(string="Buffer Penetration en Transito"
                                , compute='_compute_bp_transito')
    bp_disponible = fields.Integer(string="Buffer Penetration Disponible",
                               compute='_compute_bp_disponible')

    @api.depends('qty_available','buffer_size','qty_transit')
    def _compute_bp_transito(self):
       for record in self:
            record.bp_transito = (1-((record.buffer_size-record.qty_available-record.qty_transit)/(record.buffer_size)))*100
    def _compute_bp_solicitud(self):
        for record in self:
            record.bp_solicitud = (1-((record.buffer_size-record.qty_ordered-record.qty_available-record.qty_transit)/(record.buffer_size)))*100
    def _compute_bp_disponible(self):
        for record in self:
            record.bp_disponible = (1-((record.buffer_size-record.qty_available)/(record.buffer_size)))*100