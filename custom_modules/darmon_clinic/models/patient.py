from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital patient"

    name = fields.Char(string="Ismi")
    age = fields.Integer(string="Yoshi")
    address = fields.Text(string="Manzil")
    gender = fields.Selection([('male', "Erkak"), ('female', 'Ayol')], string="Gender")
