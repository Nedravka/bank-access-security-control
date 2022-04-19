from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
  hours, remainder = divmod(duration.seconds, 3600)
  minutes, remainder = divmod(remainder, 60)
  formated_duration = '{:02d}:{:02d}'.format(hours, minutes)
  return formated_duration


def storage_information_view(request):
    serialized_active_visits = []
  
    active_visits = Visit.objects.filter(leaved_at=None)
    
    for active_visit in active_visits:
      name = active_visit.passcard  
      duration = active_visit.duration()
      entered_time = active_visit.entered_at
      serialized_active_visits.append(
        {
        'who_entered': name,
        'entered_at': entered_time,
        'duration': format_duration(duration),
        'is_strange': active_visit.is_visit_long()
      }
      )

    context = {
        'non_closed_visits': serialized_active_visits,
    }
    return render(request, 'storage_information.html', context)
