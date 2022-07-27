# -*- coding utf-8 -*- 
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    dbm_v = fields.Integer(string="Condicion demasiado verde",default=5)
    dbm_r = fields.Integer(string="Condicion demasiado rojo",default=1)
    be_mta_mon = fields.Boolean(string="Es monitoreado por MTA", default=True)
    lt = fields.Integer(string="Tiempo de respuesta del proveedor")
    loteOptimo = fields.Integer(string="Lote óptimo")
    qty_transit = fields.Integer(string="# transito")
    buffer_size = fields.Integer(string="Buffer Size",default=1)
    contador_v = fields.Integer(string="Contador de verde")
    contador_r = fields.Integer(string="Contador de rojo")
    
    @api.model
    def create(self,values):
        override_create = super(ProductProduct,self).create(values)
        #product_info={'product_tmpl_id':override_create.id,'be_mta_mon':override_create.be_mta_mon,'dbm_v':override_create.dbm_v,'dbm_r':override_create.dbm_r,'lt':override_create.lt,'loteOptimo':override_create.loteOptimo,'qty_transit':override_create.qty_transit, 'buffer_size':override_create.buffer_size}
        #product_info = values
        #product_info['product_tmpl_id'] = override_create.id
        self.env['mta.producto'].create({'product_tmpl_id':override_create.id})
        return override_create
    
    def write(self,values):
        # your logic goes here
        print('aki si entre jiji')
        actual_buffer_size = self._origin.buffer_size
        actual_qty_available = self._origin.qty_available
        if 'buffer_size' in values:
            if(values['buffer_size']!=actual_buffer_size):
                print("sí setee contadores a 0 jiji")
                values['contador_v'] = 0
                values['contador_r'] = 0
                producto_mta = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.id)])
                self.env['changes.time'].create({'product_id':producto_mta.id,'buffer_size':values['buffer_size'],'type':'buffer'})
        if 'qty_available' in values:
            if values['qty_availale']!=actual_qty_available:
                self.env['changes.time'].create({'product_id':producto_mta.id,'qty_available':values['qty_available'],'type':'available'})
    
        override_write = super(ProductProduct,self).write(values)
       # producto = self.env['mta.producto'].search([('product_tmpl_id','=',self._origin.id)])
       # if(producto):
            #if 'dbm_v' in values:
             #   producto.dbm_v = values['dbm_v']
            #if 'dbm_r' in values:
            #    producto.dbm_r = values['dbm_r']
            #if 'be_mta_mon' in values:
            #    producto.be_mta_mon = values['be_mta_mon']
            #if 'lt' in values:
           #     producto.lt = values['lt']
            #if 'loteOptimo' in values:
             #   producto.loteOptimo = values['loteOptimo']
            #if 'qty_transit' in values:
             #  producto.qty_transit = values['qty_transit']
            #if 'buffer_size' in values:
             #   producto.buffer_size = values['buffer_size']
            #if 'qty_available' in values:
             #   producto.qty_available = values['qty_available']
        #    print('ola entra aki pero producto producto')
         #   producto.write(values)
        return override_write