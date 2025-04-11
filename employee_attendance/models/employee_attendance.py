from odoo import models, fields, api

from pytz import timezone

import datetime
import logging

_logger = logging.getLogger(__name__)

class EmployeeAttendance(models.Model):
    _inherit = 'hr.attendance'
    _name = 'employee.attendance'

    def _time_to_float(self, time: datetime.time) -> float:
        """convert time to float(in hour)"""
        # extract hour, minute and second in string
        hour_str, minute_str, second_str = time.strftime("%H:%M:%S").split(":")

        # convert h,m,s to float and hour and sum everything
        hour = float(hour_str) + (float(minute_str) / 60) + (float(second_str) / 60 / 60)

        return hour


    def check_in_action(self):
        for attendance in self:
            attendance.write({
                "check_in": datetime.datetime.now(),
                "check_in_status": True
            })

    def check_out_action(self):
        for attendance in self:
            attendance.write({
                "check_out": datetime.datetime.now()
            })

    def automatic_check_out(self):
        for attendance in self:
            attendance.write({
                "check_out": 23.59
            })
    def test_cron(self):
        _logger.info("TEST CRON")

    def _get_user_tz(self):
        user_tz = self.env.user.tz or 'UTC'
        user_tz = timezone(user_tz)
        return user_tz

    check_in_status = fields.Boolean(string="Check in status")
    shift_id = fields.Many2one('hr.shift', string='Shift', required=True, ondelete='cascade', index=True)
    late_minutes = fields.Float(string="Late minutes", compute="_compute_late_minutes")
    overtime_hours = fields.Float(string="Overtime hours", compute="_compute_overtime_hours_override", store=False)
    attendance_status = fields.Selection([('late', 'Late'), ('working', 'Working'), ('check_out', "Check Out")], string="Attendance Status", compute="_compute_attendance_status", store=True)

    @api.depends('check_in', 'shift_id.start_time', 'shift_id.grace_period')
    def _compute_late_minutes(self):
        user_tz = self._get_user_tz()
        for attendance in self:
            # set default late_minutes
            attendance.late_minutes = 0

            if attendance.check_in:
                check_in_hour = self._time_to_float(attendance.check_in.astimezone(user_tz).time())
                # convert to hour and get the diff
                check_in_diff_hour = check_in_hour - (attendance.shift_id.start_time + (attendance.shift_id.grace_period / 60))

                if check_in_diff_hour > 0:
                    attendance.late_minutes = check_in_diff_hour * 60

    @api.depends('check_in', 'check_out', 'late_minutes')
    def _compute_attendance_status(self):
        for attendance in self:
            if attendance.late_minutes > 0 and not attendance.check_out:
                attendance.attendance_status = 'late'
            elif attendance.check_in and not attendance.check_out:
                attendance.attendance_status = 'working'
            elif attendance.check_out:
                attendance.attendance_status = 'check_out'

    @api.depends('check_out', 'shift_id.end_time')
    def _compute_overtime_hours_override(self):
        user_tz = self.env.user.tz or 'UTC'
        user_tz = timezone(user_tz)
        for attendance in self:
            # set default overtime_hours
            attendance.overtime_hours = 0

            if attendance.check_out:
                check_out_hour = self._time_to_float(attendance.check_out.astimezone(user_tz).time())
                check_out_diff_hour = check_out_hour - (attendance.shift_id.end_time)

                if check_out_diff_hour > 0:
                    attendance.overtime_hours = check_out_diff_hour