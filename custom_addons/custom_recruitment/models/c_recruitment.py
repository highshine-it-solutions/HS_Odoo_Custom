from odoo import models, fields

class CustomRecruitment(models.Model):
    _inherit = 'hr.applicant'

    c_date = fields.Date(string='Date')
    c_time = fields.Char(string='Time')
    c_round1_score = fields.Char(string='1st Round Score')
    c_round2_score = fields.Char(string='2nd Round Score')
    c_source_name = fields.Char(string='Source Name')
    c_specialization = fields.Selection(
        selection=[
            ('odoo', 'Odoo'),
            ('ifs', 'IFS'),
            ('sales', 'Sales')], 
        string="Specialization")
    
    