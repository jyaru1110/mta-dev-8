# -*- coding utf-8 -*- 
from odoo import models, fields, api

class MtaProducto(models.Model):
    _inherits = {'product.template': 'product_tmpl_id'}
    _name = 'mta.producto'
    _description = 'Product MTA'

    bp_d_ind = fields.Char(string='BP D. Ind.')
    bp_t_ind = fields.Char(string='BP D. Ind. Desc.')
    bp_s_ind = fields.Char(string='BP D. Ind. Cod.')
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', required=True, ondelete='cascade')
    
    lt = fields.Integer(string='Tiempor de respuesta del proveedor')
    loteOptimo = fields.Integer(string='Lote óptimo')
     #Add a new column to the product.template model
    qty_ordered = fields.Integer(string='# Ordered')
    qty_transit = fields.Integer(string='# Transit')
    buffer_size = fields.Integer(string="Buffer Size",default=10)
    oc = fields.Integer(string="Orden de compra")
    bp_solicitud = fields.Integer(string="Solicitadas BP",)
                                #compute='_compute_bp_solicitud')
    bp_transito = fields.Integer(string="Transito BP")
                               # , compute='_compute_bp_transito')
    bp_disponible = fields.Integer(string="Buffer Penetration Disponible",)
                               #compute='_compute_bp_disponible')
    alerta = fields.Selection(string="Alerta",selection=[('dv','DV'),('dr','DR'),('na','N/A')])
    #@api.depends('qty_available','buffer_size','qty_transit')
    #def _compute_bp_transito(self):
    #   for record in self:
    #        record.bp_transito = (1-((record.buffer_size-record.qty_available-record.qty_transit)/(record.buffer_size)))*100
    #def _compute_bp_solicitud(self):
    #    for record in self:
    #        record.bp_solicitud = (1-((record.buffer_size-record.qty_ordered-record.qty_available-record.qty_transit)/(record.buffer_size)))*100
    #def _compute_bp_disponible(self):
   #     for record in self:
    #        record.bp_disponible = (1-((record.buffer_size-record.qty_available)/(record.buffer_size)))*100