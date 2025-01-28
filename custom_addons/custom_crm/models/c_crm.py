from odoo import models, fields

class CustomCrm(models.Model):
    _inherit = 'crm.lead'

    c_start_date = fields.Datetime(string='Start Date')
    c_next_date = fields.Datetime(string="Next Step Date")
    c_next_desc = fields.Text(string="Next Step Description")
    c_industry_type = fields.Char(string="Industry Type")