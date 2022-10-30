# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PatientList(models.Model):
    _name = 'patient.list'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient list to manage'

    name = fields.Char(string='Full name', compute="_concat_name")
    first_name = fields.Char(string='First name', default='')
    last_name = fields.Char(string='Last name', default='')
    age = fields.Integer(string='Age', tracking=True)
    state = fields.Selection(
        [('new', 'New'), ('consulted', 'Consulted'), ('treated', 'Treated'), ('cancelled', 'Cancelled')],
        default='new'
    )

    @api.depends('first_name', 'last_name')
    def _concat_name(self):
        for record in self:
            record.name = "%s %s" % (record.first_name, record.last_name)

    def consult(self):
        self.write({'state': "consulted"})

    def treat(self):
        self.write({'state': "treated"})

    def cancel(self):
        self.write({'state': "cancelled"})

    def renew(self):
        self.write({'state': "new"})

    def patient_birthdate_wizard(self):
        return {
            'name': _('Patient birthdate'),
            'type': 'ir.actions.act_window',
            'res_model': 'patient.birthdate',
            'view_mode': 'form',
            'target': 'new'
        }
