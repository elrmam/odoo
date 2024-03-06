# -*- coding: utf-8 -*-
{
    'name': "HMS",
    'summary': """ """,
    'description': """ """,
    'author': "Ahmed Reda",
    'category': 'Productivity',
    'version': '17.0.0.1.0',
    'depends': ['base','crm' ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
        'reports/report.xml',
        'reports/template.xml',

    ],
}