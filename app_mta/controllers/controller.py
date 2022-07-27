# -*- coding:utf-8 -*-

from odoo import http
from odoo.http import request

class Controller(http.Controller):
    @http.route(['/get_buffer_changes/<int:product_id>'],type='json',auth='public',website=True)
    
    def get_products(self,product_id):
        changes = http.request.env['changes.time'].sudo().search([('product_id','=',product_id)])
        bc = []
        for change in changes:
            n={
                "buffer_size" : change.buffer_size,
                "qty_available": change.qty_available,
                "type":change.type,
                "id" : change.id,
                "create_date" : change.create_date 
            }
            bc.append(n)
        return bc
            
        