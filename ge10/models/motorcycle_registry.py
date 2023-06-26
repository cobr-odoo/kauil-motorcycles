from odoo import api, models, fields

class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    customer_address = fields.Char(related='owner_id.contact_address')