from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _inherit = 'motorcycle.registry'

    sale_order = fields.Char(string="Sales Order")

    stock_lot_id_one2many = fields.One2many(comodel_name='stock.lot', inverse_name="motorcycle_registry_id")
    stock_lot_id = fields.Many2one(comodel_name='stock.lot', compute= "compute_one", store=True ,ondelete='set null') 

    @api.depends('stock_lot_id_one2many')
    def compute_one(self):
        for record in self:
            if self.stock_lot_id_one2many:
                self.stock_lot_id = self.stock_lot_id_one2many[0]
            else:
                self.stock_lot_id = False
        
