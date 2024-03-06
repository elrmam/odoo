from importlib.resources import _
from odoo import models,fields,api
from odoo.exceptions import ValidationError,UserError

class CrmCustomer(models.Model):
    _inherit = 'crm.customer'

    related_patient_id = fields.Many2one('hms.patient', string="Related Patient")

    @api.constrains('email')
    def _check_patient_email(self):
        for customer in self:
            if customer.email and self.env['hms.patient'].search_count([('email', '=', customer.email)]) > 0:
                raise ValidationError(_("Email already exists in patients."))