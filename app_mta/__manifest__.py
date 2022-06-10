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
       'views/product_view.xml',
       'views/assets.xml',
    ],
    'demo' : [
        
    ],
    'license': 'OPL-1'
}