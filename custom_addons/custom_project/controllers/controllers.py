# -*- coding: utf-8 -*-
# from odoo import http


# class CustomProjet(http.Controller):
#     @http.route('/custom_projet/custom_projet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_projet/custom_projet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_projet.listing', {
#             'root': '/custom_projet/custom_projet',
#             'objects': http.request.env['custom_projet.custom_projet'].search([]),
#         })

#     @http.route('/custom_projet/custom_projet/objects/<model("custom_projet.custom_projet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_projet.object', {
#             'object': obj
#         })

