# -*- coding:utf-8 -*-

from odoo import http
from odoo.http import request

class SetBufferSize(http.Controller):
    @http.route(['/set_buffer_size/<int:buffer_size>/<int:id>'],type='json',auth='public',website=True)
    
    def set_buffer_size(self,id,buffer_size):
        producto = http.request.env['mta.producto'].sudo().search([('id','=',id)])
        producto.write({'buffer_size':buffer_size})
        
        return True
        