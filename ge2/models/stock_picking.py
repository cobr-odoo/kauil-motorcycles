from odoo import api, fields, models
import re

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):

        for record in self:
            
            for line in record.move_line_ids:
                lot = line.lot_id
                product_tmp_id =lot.product_id.product_tmpl_id
                #is order going to customer + is a motorcycle
                if self.env.ref('stock.stock_location_customers') == line.location_dest_id and product_tmp_id.detailed_type == 'motorcycle':
                    serial = lot.name

                    #create registry using serial 

                    print("it worked")
                    


                
        super(StockPicking,self).button_validate()
    #     pas
        # order_name = self._origin.origin
 
        # print(order_name)
        # pattern = r'^[A-Z]{4}\d{9}'
