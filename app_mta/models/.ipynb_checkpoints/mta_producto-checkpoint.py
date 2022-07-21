# -*- coding utf-8 -*- 
from odoo import models, fields, api
from datetime import datetime

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
    recomendacion = fields.Selection(string="Recomendación", selection=[('ibs','Incrementar buffer size'),('dbs','Reducir buffer_size')])
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
    
    def write(self,values):
        actual_buffer_size = self._origin.buffer_size
        actual_estado = self._origin.estado
        if 'buffer_size' in values:
            if(values['buffer_size']!=actual_buffer_size):
                values['contador_v'] = 0
                values['contador_r'] = 0
                self.env['buffer.time'].create({'product_id':self._origin.id,'buffer_size':values['buffer_size']})
        if 'qty_available' in values:
            if(values['qty_available']>=2*self.buffer_size/3):
                values['estado'] = 1
            elif(values['qty_available']>=values['buffer_size']/3):
                values['estado'] = 2
            else:
                values['estado'] = 3
            if(actual_estado != values['estado'] and values['estado']==2):
                values['contador_v'] = 0
                values['contador_r'] = 0
        override_write = super(MtaProducto,self).write(values)
        
        
        
    def daily(self):
        productos = self.env['mta.producto'].search([('buffer_size','!=',0)])
        for producto in productos:
            producto.contador_v = (producto.qty_available-2*producto.buffer_size/3)/(producto.buffer_size/3)
            producto.contador_r = 1-(producto.qty_available)/(producto.buffer_size/3)
                
            if(producto.contador_v>=producto.dbm_v):
                producto.alerta = 'dv'
            if(producto.contador_r>=producto.dbm_r):
                producto.alerta = 'dr'
            
            if (producto.alerta == 'dv'):
                if(producto.buffer_changes):
                    now = datetime.now()
                    last_buffer_size_update = producto.buffer_changes[len(producto.buffer_changes)-1].create_date
                    delta_time = now - last_buffer_size_update
                    if(delta_time.days>producto.lt and producto.lt!=0):
                        producto.recomendacion = 'dbs'
                
            if (producto.alerta == 'dr'):
                if(producto.buffer_changes):
                    now = datetime.now()
                    last_buffer_size_update = producto.buffer_changes[len(producto.buffer_changes)-1].create_date
                    delta_time = now - last_buffer_size_update
                    if(delta_time.days>producto.lt and producto.lt!=0):
                        producto.recomendacion = 'ibs'