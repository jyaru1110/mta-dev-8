#-*- coding utf-8 -*-
from odoo import http
from odoo.http import request

class OdooControllers(http.Controller):
    @http.route(['/get_products'], type='json',auth='public', website=True)
    def get_products(self, **post):
        product_ids = http.request.env['product.template'].sudo().search_read([], ['name', 'id'])
        products = []
        for product in product_ids:
            products.append({
                'id': product.id,
                'name': product.name,
                'qty_ordered': product.qty_ordered,
                'qty_transit': product.qty_transit,
                'buffer_size': product.buffer_size,
                'oc': product.oc,
                'bp_solicitud': product.bp_solicitud,
                'bp_transito': product.bp_transito,
                'bp_disponible': product.bp_disponible,
            })
        return {'products': products}