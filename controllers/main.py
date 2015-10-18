# -*- coding: utf-8 -*-
from openerp import http

# class CnpeLdap(http.Controller):
#     @http.route('/cnpe_meeting/cnpe_meeting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cnpe_meeting/cnpe_meeting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cnpe_meeting.listing', {
#             'root': '/cnpe_meeting/cnpe_meeting',
#             'objects': http.request.env['cnpe_meeting.cnpe_meeting'].search([]),
#         })

#     @http.route('/cnpe_meeting/cnpe_meeting/objects/<model("cnpe_meeting.cnpe_meeting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cnpe_meeting.object', {
#             'object': obj
#         })