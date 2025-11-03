from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse

from django.conf import settings
from django.http import HttpRequest
from django.core.exceptions import SuspiciousOperation
from twilio.request_validator import RequestValidator
request_validator = RequestValidator(settings.TWILIO_AUTH_TOKEN)

import datetime
from django.utils import timezone

def home(request):
    return render(request, 'home.html')


def validate_django_request(request: HttpRequest):
   try:
       signature = request.META['HTTP_X_TWILIO_SIGNATURE']
   except KeyError:
       is_valid_twilio_request = False
   else:
       is_valid_twilio_request = request_validator.validate(
           signature = signature,
           uri = request.get_raw_uri(),
           params = request.POST,
       )
   if not is_valid_twilio_request:
       # Invalid request from Twilio
       raise SuspiciousOperation()

@csrf_exempt
def answer(request: HttpRequest) -> HttpResponse:
    # validate_django_request(request)
    vr = VoiceResponse()
    # vr.say('Welcome, Michael! How are you?', voice='alice', language='en-US')
    vr.say('Welcome, Michael! How are you?', voice='Polly.Matthew-Generative', language='en-US')
    return HttpResponse(str(vr), content_type='text/xml')
