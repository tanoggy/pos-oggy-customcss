# -*- coding: utf-8 -*-
{
    'name': "pos-oggy-screen",

    'summary': """Custom Oggy""",

    'description': "",

    'author': "",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
     'depends': [
        'base', 'point_of_sale',
    ],

    # always loaded
   'data': [
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    'auto_install': True,
}