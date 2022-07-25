# -*- coding utf-8 -*- 
from odoo import models, fields, api
from datetime import datetime

class MtaProducto(models.Model):
    _inherits = {'product.product': 'product_tmpl_id'}
    _name = 'mta.producto'
    _description = 'Product MTA'
   
    #buffer_changes = fields.One2many(comodel_name='buffer.time',
     #                             inverse_name = 'product_id',
      #                            string = 'Cambios en buffer')
    #product.template relation:
    product_tmpl_id = fields.Many2one('product.product', 'Product Product', required=True, ondelete='cascade')
    #mta monitoring
    #be_mta_mon = fields.Boolean(string='Es monitoreado por MTA', default=True)
    #dbm_v = fields.Integer(string="Condicion demasiado verde",default=5)
    #dbm_r = fields.Integer(string="Condicion demasiado rojo",default=1)
    contador_v = fields.Integer(string="Contador de verde")
    contador_r = fields.Integer(string="Contador de rojo")
    estado = fields.Integer(string="1. Verde 2. Amarillo 3. Rojo", compute='_compute_estado')
    recomendacion = fields.Selection(string="Recomendación", selection=[('ibs','Incrementar buffer size'),('dbs','Reducir buffer_size')])
    #graficos:
    #cont
    #attributes
    #lt = fields.Integer(string='Tiempo de respuesta del proveedor')
    #loteOptimo = fields.Integer(string='Lote óptimo')
    #qty_sitio = fields.Integer(string='# sitio')
    #qty_transit = fields.Integer(string='# transito')
    #buffer_size = fields.Integer(string="Buffer Size",default=1)
    oc = fields.Integer(string="# OC", default=0)
    bp_solicitud = fields.Integer(string="%BP en solicitadas",
                                compute='_compute_bp_solicitud')
    bp_transito = fields.Integer(string="%BP en transito"
                               , compute='_compute_bp_transito')
    bp_sitio = fields.Integer(string="%BP en sitio",
                               compute='_compute_bp_sitio')
    alerta = fields.Selection(string="Alerta",selection=[('DV','DV'),('DR','DR'),('N/A','N/A')], default="N/A")
    
    @api.model
    def create(self,values):
        override_create = super(MtaProducto,self).create(values)
        self.env['buffer.time'].create({'product_id':override_create.id,'buffer_size':override_create.buffer_size})
        return override_create
        
    @api.depends('buffer_size','qty_transit','qty_available', 'estado')
    def _compute_bp_transito(self):
       for record in self:
            record.bp_transito = ((record.buffer_size-record.qty_available-record.qty_transit)/(record.buffer_size))*100
    def _compute_bp_solicitud(self):
        for record in self:
            record.bp_solicitud = ((record.buffer_size-record.oc-record.qty_available-record.qty_transit)/(record.buffer_size))*100
    def _compute_bp_sitio(self):
        for record in self:
            record.bp_sitio = ((record.buffer_size-record.qty_available)/(record.buffer_size))*100
    def _compute_estado(self):
        for record in self:
            if(record.qty_available>=2*record.buffer_size/3):
                record.estado = 1
            elif record.qty_available >=record.buffer_size/3:
                record.estado = 2
            else:
                record.estado = 3
    
    def write(self,values):
        actual_buffer_size = self._origin.buffer_size
        actual_estado = self._origin.estado
        if 'buffer_size' in values:
            if(values['buffer_size']!=actual_buffer_size):
                print("sí setee contadores a 0 jiji")
                values['contador_v'] = 0
                values['contador_r'] = 0
                self.env['buffer.time'].create({'product_id':self._origin.id,'buffer_size':values['buffer_size']})
        #if 'qty_available' in values:
         #   if(values['qty_available']>=2*self.buffer_size/3):
          #      values['estado'] = 1
           # elif(values['qty_available']>=values['buffer_size']/3):
            #    values['estado'] = 2
            #else:
             #   values['estado'] = 3
        if 'estado' in values:
            if(actual_estado != values['estado'] and values['estado']==2):
                values['contador_v'] = 0
                values['contador_r'] = 0
        print('ola si entre aki jejeJEJEJEJ')
        override_write = super(MtaProducto,self).write(values)
        return override_write
        
        
        
    def daily(self):
        productos = self.env['mta.producto'].search([('buffer_size','!=',0)])
        
        for producto in productos:
            contador = False
            product = self.env['mta.producto'].browse(producto['id'])
            if producto.estado == 1:
                product.contador_v =product.contador_v + (product.qty_available-2*product.buffer_size/3)/(product.buffer_size/3)
            elif producto.estado == 3:
                product.contador_r =product.contador_r + 1-(producto.qty_available)/(producto.buffer_size/3)
                
            if(product.contador_v>=product.dbm_v):
                product.alerta = 'DV'
                contador = True
            if(product.contador_r>=product.dbm_r):
                product.alerta = 'DR'
                contador = True
            if( not contador):
                product.alerta = 'N/A'
            
            
            if (product.alerta == 'DV'):
                if(product.buffer_changes):
                    now = datetime.now()
                    last_buffer_size_update = product.buffer_changes[len(product.buffer_changes)-1].create_date
                    delta_time = now - last_buffer_size_update
                    if(delta_time.days>product.lt and product.lt!=0):
                        product.recomendacion = 'dbs'
                
            if (product.alerta == 'DR'):
                if(product.buffer_changes):
                    now = datetime.now()
                    last_buffer_size_update = product.buffer_changes[len(product.buffer_changes)-1].create_date
                    delta_time = now - last_buffer_size_update
                    if(delta_time.days>product.lt and product.lt!=0):
                        product.recomendacion = 'ibs'