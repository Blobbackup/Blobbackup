from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from blobbackup.models import Backups


class Scheduler(BackgroundScheduler):
    def __init__(self, app):
        BackgroundScheduler.__init__(self)
        self.app = app
        self.start()
        self.reload()

    def reload(self):
        self.remove_all_jobs()
        backups = Backups.load_all()
        for backup in backups.values():
            trigger = None
            if backup.backup_daily_time is not None:
                trigger = CronTrigger(hour=backup.backup_daily_time.hour(),
                                      minute=backup.backup_daily_time.minute(),
                                      day_of_week=backup.backup_days)
            if backup.every_hour is not None and backup.every_min is not None:
                trigger = CronTrigger(hour=f'*/{backup.every_hour}',
                                      minute=backup.every_min)
            if self.get_job(backup.name) is not None and trigger is not None:
                self.reschedule_job(backup.name, trigger=trigger)
            elif trigger is not None:
                self.add_job(func=self.app.start_backup.emit,
                             args=(False, backup.name),
                             trigger=trigger,
                             id=backup.name,
                             misfire_grace_time=180)
            elif self.get_job(backup.name) is not None and trigger is None:
                self.remove_job(backup.name)
