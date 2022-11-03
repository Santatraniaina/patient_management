from datetime import date

from odoo import fields, models, api


class PatientBirthdate(models.TransientModel):
    _name = 'patient.birthdate'
    _description = 'Description'

    birthdate = fields.Date(string='Birthdate')

    @api.depends('birthdate')
    def compute_age(self):
        patient_ids = self.env['patient.list']
        active_id = self.env.context.get('active_id')
        patient_id = patient_ids.search([('id', '=', active_id)])
        today = date.today()
        patient_id.age = today.year - self.birthdate.year - (
                    (today.month, today.day) < (self.birthdate.month, self.birthdate.day))
