from typing import re

from odoo import models, fields, api
from datetime import date

from odoo17.odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('o', 'O'),
        ('ab', 'AB'),
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
    logs_history = fields.One2many("log.history", "patient_id")
    department_id = fields.Many2one('hms.department', domain="[('is_opened', '=', True)]")
    capacity = fields.Integer(related="department_id.capacity")
    doctor_id = fields.Many2many("hms.doctor")
    email = fields.Char(required=True, unique=True)

    @api.onchange('email')
    def validation_email(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match is None:
                raise ValidationError('This Email Is Not Valid')
    @api.depends('birth_date')
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
            return {'pcr has been checked.'}

    def action_undetermined(self):
        for rec in self:
            rec.state = 'undetermined'
    def action_good(self):
        for rec in self:
            rec.state = 'good'
    def action_fair(self):
        for rec in self:
            rec.state = 'fair'
    def action_ferious(self):
        for rec in self:
            rec.state = 'ferious'

    @api.model
    def create(self, vals_list):
        record = super().create(vals_list)
        self.env['log.history'].create({
            'description': 'Created Patient',
            'patient_id': record.id
        })
        return record