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
    'depends' : ['sale','purchase','stock'],
    'data':[
       'views/product_view_inherit.xml',
    ],
    'demo' : [
        
    ],
    'license': 'OPL-1'
}