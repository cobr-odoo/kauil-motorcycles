from odoo import api, fields, models

class StockLot(models.Model):
    _inherit = 'stock.lot'
    motorcycle_registry_id = fields.Many2one(comodel_name="motorcycle.registry")
    # motorcycle_registry = fields.One2many(required= True, comodel_name='motorcycle.registry')

    # @api.depends('motorcycle_registry')
    # def GetFinalAnswer(self):
    #     if len(self.motorcycle_registry) > 0:
    #         self.motorcycle_registry_final = self.motorcycle_registry[0]
        
    
        