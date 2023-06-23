from odoo import api, fields, models


class StockLot(models.Model):
    _inherit = 'stock.lot'


    def _get_next_serial(self, company, product):


        prod_tmpl_id = product.product_tmpl_id
        if prod_tmpl_id.detailed_type == 'motorcycle' and product.tracking != 'none':

            prod_make = prod_tmpl_id.make if prod_tmpl_id.make else 'XX'
            prod_model = prod_tmpl_id.model if prod_tmpl_id.model else 'XX'
            prod_year = str(prod_tmpl_id.year)[-2:] if prod_tmpl_id.year else '00'
            sequence = self.env['ir.sequence'].next_by_code('stock.lot.serial')
            return f'{prod_make}{prod_model}{prod_year}{sequence}'

        else:
            return super(StockLot, self)._get_next_serial(company, product)

