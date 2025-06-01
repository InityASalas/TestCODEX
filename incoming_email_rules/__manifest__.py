{
    'name': 'Incoming Email Rules',
    'version': '1.0',
    'summary': 'Define rules for incoming emails to create records',
    'category': 'Tools',
    'author': 'Generated',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/incoming_email_rule_views.xml',
    ],
    'installable': True,
    'application': False,
}
