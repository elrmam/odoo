from odoo import models, fields

class LogHistory(models.Model):
    _name = 'hms.log.history'
    _description = 'Log History'

    patient_id = fields.Many2one("hms.patient")
    action = fields.Char(readonly=True)
    date = fields.Datetime(default=fields.Datetime.now)
    description = fields.Text()