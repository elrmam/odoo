from odoo import models, fields, api
from datetime import date


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'

    first_name = fields.Char(required=1)
    last_name = fields.Char(required=1)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
        ('honey', 'Honey')
    ])
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute='_calc_patient_age')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('ferious', 'Ferious')
    ])

    department_id = fields.Many2one('hms.department')
    capacity = fields.Integer('department_id.capacity')
    doctor_id = fields.Many2many("hms.doctor")




    def _calc_patient_age(self):
        for rec in self:
            rec.age = date.today().year - rec.birth_date.year

    @api.onchange('birth_date')
    def _on_birth_date_change(self):
        if self.birth_date:
            self.age = date.today().year - self.birth_date.year



    @api.onchange('age')
    def _on_age_change(self):
        if self.age < 30:
            self.pcr = True
        else:
            self.pcr = False
