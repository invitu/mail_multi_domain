# -*- coding: utf-8 -*-
# Copyright 2021 Subteno (<https://www.subteno.com>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': "mail_multi_domain",
    'summary': "Multi-domain management in Odoo",
    'description': """
        Long description of module's purpose
    """,
    'author': "Subteno IT",
    'website': "https://www.subteno-it.com",
    'category': 'Discuss',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ir_mail_server.xml',
        'views/res_company.xml',
        'views/mail_user_alias.xml',
        'views/res_users.xml',
        'data/base.xml',
    ],
}