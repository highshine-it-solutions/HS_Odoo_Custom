# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAppraisal(http.Controller):
#     @http.route('/custom_appraisal/custom_appraisal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_appraisal/custom_appraisal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_appraisal.listing', {
#             'root': '/custom_appraisal/custom_appraisal',
#             'objects': http.request.env['custom_appraisal.custom_appraisal'].search([]),
#         })

#     @http.route('/custom_appraisal/custom_appraisal/objects/<model("custom_appraisal.custom_appraisal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_appraisal.object', {
#             'object': obj
#         })

