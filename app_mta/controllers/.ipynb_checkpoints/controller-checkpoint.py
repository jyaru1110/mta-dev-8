# -*- coding:utf-8 -*-

from odoo import http
from odoo.http import request

class Controller(http.Controller):
    @http.route(['/get_buffer_changes/<int:product_id>'],type='json',auth='public',website=True)
    
    def get_products(self,product_id):
        buffer_changes = http.request.env['buffer.time'].sudo().search([('product_id','=',product_id)])
        
        bc = []
        
        for buffer_change in buffer_changes:
            n={
                "buffer_size" : buffer_change.buffer_size,
                "id" : buffer_change.id,
                "create_date" : buffer_change.create_date 
            }
            bc.append(n)
        return bc
            
        