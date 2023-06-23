from odoo import api, fields, models
import re

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
       
    
        pattern = r'^[A-Z]{4}\d{9}'
        
    