from odoo import models, fields, api

class EmployeeAttendance(models.Model):
    _inherit = 'hr.attendance'
    _name = 'employee.attendance'

    def _compute_late_minutes(self):
        pass

    shift_id = fields.Many2one('hr.shift', string='Shift', required=True, ondelete='cascade', index=True)
    late_minutes = fields.Float(string="Late minutes", compute=_compute_late_minutes)