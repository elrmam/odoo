from odoo import fields, models, api


class Ticket(models.Model):
    _name = 'todo.ticket'
    _description = 'Todo'

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    state = fields.Selection([
        ('new', 'New'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    ])
    file = fields.Binary()
    description = fields.Char()