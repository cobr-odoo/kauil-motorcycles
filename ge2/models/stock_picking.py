from odoo import api, fields, models
import re

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):

        for record in self:
            
            for line in record.move_line_ids:
                lot = line.lot_id
                product_tmp_id =lot.product_id.product_tmpl_id
                # is order going to customer + is a motorcycle
                if self.env.ref('stock.stock_location_customers') == line.location_dest_id and product_tmp_id.detailed_type == 'motorcycle' and line.qty_done == line.reserved_qty:
                    vin_number = lot.name
                    owner_id = line.picking_partner_id
                    
                    target_model = self.env['motorcycle.registry']
                    target_model.create({
                        'vin': vin_number,
                        'owner_id': owner_id.id,
                        'sale_order': record.origin
                
                    })
    
                
        return super(StockPicking,self).button_validate()
