{
    'name': "custom_project",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/project_task_rules.xml',
        'views/project_task.xml',
    ],
    # only loaded in demonstration mode
    'module_type': 'official',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    
}
