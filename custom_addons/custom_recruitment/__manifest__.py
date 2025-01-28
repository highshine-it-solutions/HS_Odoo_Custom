# -*- coding: utf-8 -*-
{
    'name': "custom_recruitment",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Gokul",
    'website': "https://highshine.in/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_recruitment'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/c_recruitment_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'module_type': 'official',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    
}

