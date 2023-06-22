from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    battery_capacity = fields.Selection(selection=[('xs','Small'),
                                        ('0m','Medium'),
                                        ('0l','Larga'),
                                        ('xl','Extra Large'),],
                                        copy=False
                                       )
    charge_time = fields.Float()
    curb_weight = fields.Float()
    horsepower = fields.Float()
    launch_date = fields.Date()
    make = fields.Char()
    model = fields.Char()
    range = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    year = fields.Integer()
    name = fields.Char(default="", compute='set_motorcycle_name', inverse='_inverse_name')
    
    detailed_type = fields.Selection(selection_add=[('motorcycle','Motorcycle')], 
                            ondelete={'motorcycle': 'set product'},
                            help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
                            'A consumable product is a product for which stock is not managed.\n'
                            'A service is a non-material product you provide.\n'
                            'A motorcycle is a captivating symbol of freedom, power, and adventure, offering an exhilarating two-wheeled escape that combines speed, agility, and the thrill of the open road.')

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping
    
    @api.depends('make', 'model', 'year')
    def set_motorcycle_name(self):
        # for motorcycle in self.filtered(lambda r: r.detailed_type == "motorcycle"):
        #     motorcycle.name="hihi"
        for motorcycle in self:
            if motorcycle.detailed_type == 'motorcycle':
                if motorcycle.make and motorcycle.model and motorcycle.year:
                    motorcycle.name = str(motorcycle.make) + str(motorcycle.model) + str(motorcycle.year)
                else:
                    motorcycle.name = None
    
    def _inverse_name(self):
        for motorcycle in self:
            if motorcycle.detailed_type != 'motorcycle':
                pass