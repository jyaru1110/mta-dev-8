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
    'depends' : ['sale','stock','point_of_sale'],
    'data':['security/mta_security.xml',
            'security/ir.model.access.csv',
            'views/mta_app_view.xml',
            'views/product_view.xml',
            'views/product_views_inherit.xml',
            'schedule/schedule.xml'
    ],
    'assets': {
        
        'point_of_sale.assets':[
            '/app_mta/static/src/js/CategoryControlButton.js',
        ],
        'web.assets_backend': [
            ('prepend','/app_mta/static/src/css/progress_bar_widget.css'),
            '/app_mta/static/src/js/progress_bar_widget.js',
            '/app_mta/static/src/js/chart_widget.js',
            '/app_mta/static/src/js/recomendacion_widget.js',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.8.0/chart.min.js',
            "https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns/dist/chartjs-adapter-date-fns.bundle.min.js"
        ],
        'web.assets_qweb': [
            '/app_mta/static/src/xml/progress_bar_widget.xml',
            '/app_mta/static/src/xml/chart_widget.xml',
            '/app_mta/static/src/xml/recomendacion_widget.xml',
            '/app_mta/static/src/xml/CategoryControlButton.xml',
        ],
    },
    
    'demo' : [
        
    ],
    'license': 'OPL-1'
}