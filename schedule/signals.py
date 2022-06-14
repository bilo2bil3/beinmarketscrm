import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from schedule.models import ReminderNotification
from django_celery_beat.models import PeriodicTask, CrontabSchedule

@receiver(post_save, sender=ReminderNotification)
def notification_handler(sender, instance, created, **kwargs):
    if created:
        date = instance.reminder_on
        
        schedule = CrontabSchedule.objects.create(
            hour=date.hour,
            minute=date.minute,
            day_of_month=date.day,
            month_of_year=date.month,
            timezone='Asia/Riyadh'
        )
        
        task = PeriodicTask.objects.create(
            crontab=schedule,
            name="reminder-notification-" + str(instance.id),
            task='schedule.tasks.reminder_notification',
            args=json.dumps((instance.id,))
        )