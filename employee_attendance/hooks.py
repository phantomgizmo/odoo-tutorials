from odoo import fields, api, SUPERUSER_ID
import pytz
import datetime

def _set_cron_nextcall(env):
    def _get_nextcall() -> datetime.datetime:
        user_tz = "Asia/Jakarta"
        user_tz = pytz.timezone(user_tz)
        now = fields.Datetime.now().astimezone(user_tz)
        target_nextcall = now.replace(hour=23, minute=59, second=0)
        if now > target_nextcall: # Check if today nextcall already passed
            target_nextcall = target_nextcall + datetime.timedelta(hours=24)
        return target_nextcall.astimezone(pytz.UTC)
    
    auto_check_out_cron = env.ref("employee_attendance.automatic_check_out_cron")
    auto_check_out_cron.nextcall = _get_nextcall().strftime('%Y-%m-%d %H:%M:%S')