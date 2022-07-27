from odoo import models, fields, api

class ChangesTime(models.Model):
    _name = 'changes.time'
    _description = "Model that records everytime a product buffer size changes"
    product_id = fields.Many2one(comodel_name="mta.producto",
                               string="Producto",
                               ondelete="cascade",
                               required=True)
    buffer_size = fields.Integer(string="buffer size",default=0)
    qty_available = fields.Integer(string="Qty On Hand",default=0)
    type = fields.Char(string="Tipo de cambios", required = True)