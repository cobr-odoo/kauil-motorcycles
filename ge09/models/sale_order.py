from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    new_customer = fields.Boolean(compute='_compute_new_customer', default=False)

    @api.depends('partner_id')
    def _compute_new_customer(self):
        for record in self:
            record.new_customer = True
