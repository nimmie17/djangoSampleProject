from django.shortcuts import render,redirect
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
# Create your views here.

def index(request):
    return render(request,'index.html')

def validate_num(request):
    context = {}
    if request.method == 'POST':
        ph_num = request.POST.get('phone_number','')
        try:
            parsed_num = phonenumbers.parse(ph_num,None)
            if phonenumbers.is_valid_number(parsed_num):
                context['is_valid'] = True
                context['formatted_num'] = phonenumbers.format_number(parsed_num,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                context['country_code'] = parsed_num.country_code
                context['national_num'] = parsed_num.national_number
                context['region'] = phonenumbers.region_code_for_number(parsed_num)
                context['country'] = geocoder.description_for_number(parsed_num, "en")
                context['carrier'] = carrier.name_for_number(parsed_num,"en")
                context['timezone'] = timezone.time_zones_for_number(parsed_num)
        except phonenumbers.NumberParseException:
                context['is_valid'] = False
                context['error'] = "Invalid phone number,Enter with country code"
        return render(request, 'index.html', context)
    return redirect('index')