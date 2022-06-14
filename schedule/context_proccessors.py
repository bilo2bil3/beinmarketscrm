from datetime import datetime
from schedule.models import ReminderNotification

def notifications(request):
    if request.user.is_authenticated:
        all_notifications = ReminderNotification.objects.filter(user=request.user, reminder_on__lte=datetime.now())
        return {'notifications': all_notifications}
    return []