#-*- coding utf-8 -*-
from odoo import http
from odoo.http import request

class OdooControllers(http.Controller):
    @http.route(['/get_products'], type='json',auth='public', website=True)
    def get_products(self, **post):
        product_ids = http.request.env['mta.producto'].sudo().search_read([], ['name', 'id'])
        products = []
        for product in product_ids:
            products.append({
                'id': product.id,
                'name': product.name
            })
        return {'products': products}