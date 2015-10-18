# -*- coding: utf-8 -*-
{
    'name': "cnpe_meeting",

    'summary': """
        CNPE meeting schdule and meeting room booking tools.
        For tsc only""",

    'description': """
        CNPE meeting schdule and meeting room booking tools.
        - create meeting room.
        - meeting room booking.
        - meeting scheduling.
        - meeting room managing.
    """,

    'author': "Mack Fire",
    'website': "http://tsc.cnpe.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','auth_ldap'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cnpe_meeting_templates.xml',
        'views/cnpe_meeting_views.xml',
        'data/cnpe_meeting_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/cnpe_meeting_demo.xml',
    ],
}
