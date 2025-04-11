from odoo import models, fields, api

class HrShift(models.Model):
    _name = 'hr.shift'

    attendance_ids = fields.One2many("employee.attendance", "shift_id")
    name = fields.Char()
    start_time = fields.Float(string='Start from', required=True, index=True,
        help="Start and End time of working.\n"
             "A specific value of 24:00 is interpreted as 23:59:59.999999.")
    end_time = fields.Float(string='Start to', required=True)
    grace_period = fields.Float(string="Grace period (in minutes)")