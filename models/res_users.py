# -*- coding: utf-8 -*-
# Copyright 2020 Subteno IT
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    mail_user_alias_ids = fields.One2many(
        comodel_name='mail.user.alias',
        inverse_name='user_id',
    )
    server_mail_id = fields.Many2one(
        string='Server Mail',
        comodel_name='ir.mail_server',
        help='The server mail used for the user if the configuration is split server mail by user',
    )

    def __init__(self, pool, cr):
        """ Override of __init__ to add access rights.
            Access rights are disabled by default, but allowed
            on some specific fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
        """

        sale_stock_writeable_fields = [
            'mail_user_alias_ids',
            'server_mail_id',
        ]

        super().__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = type(self).SELF_READABLE_FIELDS + sale_stock_writeable_fields
        type(self).SELF_WRITEABLE_FIELDS = type(self).SELF_WRITEABLE_FIELDS + sale_stock_writeable_fields
