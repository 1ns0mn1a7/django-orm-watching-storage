from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import Visit


SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f"{hours}ч {minutes}мин"


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime(
                "%d %B %Y г. %H:%M"
            ),
            'duration': format_duration(visit.get_duration()),
        }
        for visit in active_visits
    ]

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
