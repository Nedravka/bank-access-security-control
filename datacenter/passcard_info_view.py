from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

 
def passcard_info_view(request, passcode):
    this_passcard_visits = [
    ]

    picked_passcard = Passcard.objects.get(passcode=passcode)
    
    for visit in Visit.objects.filter(passcard=picked_passcard):
      session = {
      'entered_at': visit.entered_at,
      'duration': visit.duration(),
      'is_strange':visit.is_visit_long()
      }
      this_passcard_visits.append(session)
  
    context = {
        'passcard': picked_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
