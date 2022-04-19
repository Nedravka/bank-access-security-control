from django.utils import timezone
from django.db import models

import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
      return f'{self.passcard.owner_name} entered at {self.entered_at}' + f'leaved at {self.leaved_at}' if self.leaved_at else 'not leaved'

    def duration(self):
      if self.leaved_at:
        duration = self.leaved_at - self.entered_at
        return duration
      
      time_of_enter = datetime.datetime.strptime(str(self.entered_at),
                                                      '%Y-%m-%d %H:%M:%S%z')
      formated_time_of_enter = timezone.localtime(
          value=time_of_enter, 
          timezone=timezone.get_current_timezone()
        )
      duration = timezone.localtime() - formated_time_of_enter
      return duration

    def is_visit_long(self, minutes=60):    
      return self.duration().seconds > minutes * 60
    
 
  
