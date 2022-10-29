# -*- coding: utf-8 -*-
# from odoo import http


# class PatientManagement(http.Controller):
#     @http.route('/patient_management/patient_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/patient_management/patient_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('patient_management.listing', {
#             'root': '/patient_management/patient_management',
#             'objects': http.request.env['patient_management.patient_management'].search([]),
#         })

#     @http.route('/patient_management/patient_management/objects/<model("patient_management.patient_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('patient_management.object', {
#             'object': obj
#         })
