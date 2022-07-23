# -*- coding:utf-8 -*-

from odoo import http
from odoo.http import request

class Controller(http.Controller):
    @http.route(['/get_buffer_changes'],type='json',auth='public',website=True)
    
    def get_products(self,**kw):
        buffer_changes = http.request.env['mta.producto'].sudo().search([],limit=5)
        
        bc = []
        
        for buffer_change in buffer_changes:
            n={
                "buffer_size" : buffer_change.buffer_size,
                "id" : buffer_change.id,
                "create_date" : buffer_change.create_date 
            }
            bc.append(n)
        return bc
            
        