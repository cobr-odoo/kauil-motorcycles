from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    new_customer = fields.Boolean(compute='_compute_new_customer', default=True)

    @api.depends('partner_id')
    def _compute_new_customer(self):
        pass

    #     for record in self:
            
    #         record.new_customer = True
    #         for orders in record.partner_id.sale_order_ids[1:]:
    #             if orders.order_line.product_id.detailed_type == 'motorcycle':
    #                 record.new_customer = False
    #                 break
                

                