# -*- coding: utf-8 -*-
# from odoo import http


# class AamHospital(http.Controller):
#     @http.route('/aam_hospital/aam_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aam_hospital/aam_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aam_hospital.listing', {
#             'root': '/aam_hospital/aam_hospital',
#             'objects': http.request.env['aam_hospital.aam_hospital'].search([]),
#         })

#     @http.route('/aam_hospital/aam_hospital/objects/<model("aam_hospital.aam_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aam_hospital.object', {
#             'object': obj
#         })

