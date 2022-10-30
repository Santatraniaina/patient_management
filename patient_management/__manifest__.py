# -*- coding: utf-8 -*-
{
    'name': "patient_management",

    'summary': """
        Module for patient management""",

    'description': """
        Module for patient management
    """,

    'author': "Santatraniaina",
    'website': "http://www.kasia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail'
    ],

    # always loaded
    'data': [
        # security
        'security/ir.model.access.csv',

        # views
        'views/patient_list_views.xml',

        # wizard
        'wizard/patient_birthday_view.xml',

        #reports
        'reports/patient_list_report_view.xml',
    ],
}
