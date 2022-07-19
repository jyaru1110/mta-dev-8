# -*- coding utf-8 -*- 
from odoo import models, fields, api

class MtaProducto(models.Model):
    _inherits = {'product.product': 'product_tmpl_id'}
    _name = 'mta.producto'
    _description = 'Product MTA'
   
    buffer_changes = fields.One2many(comodel_name='buffer.time',
                                  inverse_name = 'product_id',
                                  string = 'Cambios en buffer')
    #product.template relation:
    product_tmpl_id = fields.Many2one('product.product', 'Product Product', required=True, ondelete='cascade')
    #mta monitoring
    be_mta_mon = fields.Boolean(string='Es monitoreado por MTA', default=True)
    dbm_v = fields.Integer(string="Condicion demasiado verde",default=5)
    dbm_r = fields.Integer(string="Condicion demasiado rojo",default=1)
    contador_v = fields.Integer(string="Contador de verde")
    contador_r = fields.Integer(string="Contador de rojo")
    estado = fields.Integer(string="1. Verde 2. Amarillo 3. Rojo")
    #graficos:
    #cont
    #attributes
    lt = fields.Integer(string='Tiempo de respuesta del proveedor')
    loteOptimo = fields.Integer(string='Lote óptimo')
    #qty_sitio = fields.Integer(string='# sitio')
    qty_transit = fields.Integer(string='# transito')
    buffer_size = fields.Integer(string="Buffer Size",default=1)
    oc = fields.Integer(string="# OC", default=0)
    bp_solicitud = fields.Integer(string="%BP en solicitadas",
                                compute='_compute_bp_solicitud')
    bp_transito = fields.Integer(string="%BP en transito"
                               , compute='_compute_bp_transito')
    bp_sitio = fields.Integer(string="%BP en sitio",
                               compute='_compute_bp_sitio')
    alerta = fields.Selection(string="Alerta",selection=[('dv','DV'),('dr','DR'),('na','N/A')], default="na")
    @api.depends('buffer_size','qty_transit','qty_available')
    def _compute_bp_transito(self):
       for record in self:
            record.bp_transito = ((record.buffer_size-record.qty_available-record.qty_transit)/(record.buffer_size))*100
    def _compute_bp_solicitud(self):
        for record in self:
            record.bp_solicitud = ((record.buffer_size-record.oc-record.qty_available-record.qty_transit)/(record.buffer_size))*100
    def _compute_bp_sitio(self):
        for record in self:
            record.bp_sitio = ((record.buffer_size-record.qty_available)/(record.buffer_size))*100
            
    @api.onchange('qty_available', 'contador_r', 'contador_v', 'buffer_size')
    def _onchange_qty_available(self):
        estado_anterior = self.estado
        if(self.qty_available>=2*self.buffer_size/3):
            self.estado = 1
        elif(self.qty_available>=self.buffer_size/3):
            self.estado = 2
        else:
            self.estado = 3
        if(estado_anterior != self.estado):
            self.contador_v = 0
            self.contador_r = 0
        elif(self.estado == 1):
            self.contador_v = (self.qty_available-2*self.buffer_size/3)/(self.buffer_size/3)
        elif(self.estado == 3):
            self.contador_r = 1-(self.qty_available)/(self.buffer_size/3)
            
    def _onchange_buffer_size(self):
            self.contador_v = 0
            self.contador_r = 0
            
    def _onchange_contador_v(self):
        if(self.contador_v>=self.dbm_v):
            self.alerta = 'dv'
            
    def _onchange_contador_r(self):
        if(self.contador_r>=self.dbm_r):
            self.alerta = 'dr'
            
            