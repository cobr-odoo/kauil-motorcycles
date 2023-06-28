from odoo import api, models, fields

class RepairOrder(models.Model):
    _inherit = 'repair.order'

    vin = fields.Char(string='VIN', required=True)
    current_mileage = fields.Float(string='Current Mileage')

    registry_id = fields.Char(compute='_compute_registry_id')

    partner_id = fields.Many2one(compute='_compute_fields')
    sale_order_id = fields.Char(compute='_compute_fields')
    product_id = fields.Many2one(compute='_compute_fields')

    

    @api.depends('vin')
    def _compute_registry_id(self):
        for record in self:
            record.registry_id = self.env['motorcycle.registry'].search([('vin','=', record.vin)]).registry_number
            
    @api.depends('registry_id')
    def _compute_fields(self):
        for record in self:
            motorcycle_registry = self.env['motorcycle.registry']
            record.partner_id = motorcycle_registry.search([('registry_number','=', record.registry_id)]).owner_id
            record.sale_order_id = motorcycle_registry.search([('registry_number','=', record.registry_id)]).sale_order

            mrp_object = self.env['mrp.production'].search([('origin', '=', record.sale_order_id)])
            for reference in mrp_object:
                serial_number = reference.lot_producing_id
                if serial_number.name == record.vin:
                    record.product_id = reference.product_id

