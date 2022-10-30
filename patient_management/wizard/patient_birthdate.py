from odoo import fields, models

class PatientBirthdate(models.TransientModel):
    _name = 'patient.birthdate'
    _description = 'Description'

    birthdate = fields.Date(string='Birthdate')

    # def compute_age(self):