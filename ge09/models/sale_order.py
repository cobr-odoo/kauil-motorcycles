from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    new_customer = fields.Boolean(compute='_compute_new_customer')

    @api.depends('partner_id')
    def _compute_new_customer(self):
        for sale_order in self:
            sale_order.new_customer = True
            orders = sale_order.partner_id.sale_order_ids
            if len(orders) < 2:
                continue
            
            for order in orders[1:]:
                if order.order_line.product_id.detailed_type == 'motorcycle':
                    sale_order.new_customer = False
                    break

    def add_discount(self):
        pass
    #     for record in self:
            
    #         record.new_customer = True

                

                