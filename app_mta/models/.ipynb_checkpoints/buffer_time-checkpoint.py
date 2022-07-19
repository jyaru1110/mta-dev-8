from odoo import models, fields, api

class BufferTime(models.Model):
    _name = 'buffer.time'
    _description = "Model that records everytime a product buffer size changes"
    product_id = fields.Many2one(comodel_name="mta.producto",
                               string="Producto",
                               ondelete="cascade",
                               required=True)
    buffer_size = fields.Integer(string="buffer size", required=True)