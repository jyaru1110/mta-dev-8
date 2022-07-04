# -*- coding: utf-8 -*-
{
    'name' : 'App',
    'summary': """App to manage inventory with TOC""",
    'description':"""
    App to manage inventory with TOC
    """,
    'author' : 'odoo',
    'category' : 'Training',
    'version' : '0.1',
    'depends' : ['sale'],
    'data':[
       'security/mta_security.xml',  
       'security/ir.model.access.csv',
       'views/mta_app_view.xml',
       'views/product_view.xml'
    ],
    'assets': {
        'web.assets_backend': {
            '/app_mta/static/src/css/my_field_widget.css',
            '/app_mta/static/src/js/my_field_widget.js',
        },
        'web.assets_qweb': {
            '/app_mta/static/src/xml/my_field_widget.xml',
        },
    },
    'demo' : [
        
    ],
    'license': 'OPL-1'
}