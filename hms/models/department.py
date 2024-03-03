from odoo import models, fields


class Department(models.Model):
    _name = 'hms.department'
    _description = 'Dept'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients = fields.One2many('hms.patient', 'department_id')