# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    # Add a new column to the product.template model
    qty_ordered = fields.Integer(string='# Ordered')
    buffer_size = fields.Integer(string="Buffer Size")
    oc = fields.Integer(string="OC")
    bp_solicitud = fields.Integer(string="Buffer Penetration Solicitadas",
                                compute='_compute_bp_solicitud')
    bp_transito = fields.Integer(string="Buffer Penetration en Transito"
                                , compute='_compute_bp_transito')
    bp_disponible = fields.Integer(string="Buffer Penetration Disponible",
                                compute='_compute_bp_disponible')

    @api.depends('qty_available','buffer_size','virtual_available')
    def _compute_bp_transito(self):
        for record in self:
            record.bp_transito = (1-((record.buffer_size-record.qty_available-record.virtual_available)/(record.buffer_size)))*100
    def _compute_bp_disponible(self):
        for record in self:
            record.bp_disponible = (1-((record.buffer_size-record.qty_available)/(record.buffer_size)))*100