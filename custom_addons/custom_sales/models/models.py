from odoo import models, fields, api

class custom_sales(models.Model):
    _inherit = 'product.template'

    c_type = fields.Char(string='Type')
    c_location = fields.Char(string="Location")
    c_product_reference = fields.Binary(string="Produt Reference")
    c_dimension = fields.Char(string="Dimension")
    c_finish = fields.Char(string="Finish")
    c_adaptability = fields.Char(string="Adaptability")
    c_ip_rating = fields.Char(string="IP Rating")
    c_optics_type = fields.Char(string="Optics Type")
    c_beam_angle = fields.Char(string="Beam Angle")
    c_light_source = fields.Char(string="Light Source")
    c_actual_power = fields.Char(string="Actual Power")
    c_unit = fields.Char(string="Unit")
    c_lumen_package = fields.Char(string="Lumen Package")
    c_color_temperature = fields.Char(string="Color Temperature")
    c_cri = fields.Char(string="CRI")
    c_power_supply = fields.Char(string="Power Supply")
    c_control_type = fields.Char(string="Control Type")
    c_unit = fields.Char(string="Unit")
    c_total_power = fields.Char(string="Total Power")