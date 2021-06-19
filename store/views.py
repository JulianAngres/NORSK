from django.shortcuts import render, redirect
from .models import Time
from users.models import Profile
import datetime
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from xhtml2pdf import pisa
import os
from django.core.mail import send_mail, EmailMessage
from NORSK.settings import EMAIL_HOST_USER
from django.urls import reverse
from django.http import JsonResponse
import stripe
import random
import string

stripe.api_key = 'sk_test_51IzkfCGbhvTsDgfjvhRsPhXsBF5M2TnZP4hTqoBQLVjgxNP4p6bnLJMPjoGATCPqcX6EmcvyA2rBT9OwoLYvG2cb00kV6hULs1'

#from .models import whatever


@login_required(login_url='login')
def GoToCalendar(request):
    current_user = request.user
    valgt_bruker = Profile.objects.get(user = current_user)

    if valgt_bruker.sixty_left == True:
        rabatt = '60'
    if valgt_bruker.fifteen_left == True:
        rabatt = '15'
    if valgt_bruker.zero_left == True:
        rabatt = '0'

    alle_timer = Time.objects.all
    all_fields = [f.name for f in Time._meta.get_fields()][1:]
    #all_fields = Time._meta.get_fields()
    now = datetime.date.today()
    #now = now.__str__()
    #day_difference = days_between(now, "2021-05-13")

    tag1 = Time.objects.filter(date=(now + datetime.timedelta(1)).__str__())
    tag2 = Time.objects.filter(date=(now + datetime.timedelta(2)).__str__())
    tag3 = Time.objects.filter(date=(now + datetime.timedelta(3)).__str__())
    tag4 = Time.objects.filter(date=(now + datetime.timedelta(4)).__str__())
    tag5 = Time.objects.filter(date=(now + datetime.timedelta(5)).__str__())
    tag6 = Time.objects.filter(date=(now + datetime.timedelta(6)).__str__())
    tag7 = Time.objects.filter(date=(now + datetime.timedelta(7)).__str__())
    tag1_date = (now + datetime.timedelta(1)).__str__()
    tag2_date = (now + datetime.timedelta(2)).__str__()
    tag3_date = (now + datetime.timedelta(3)).__str__()
    tag4_date = (now + datetime.timedelta(4)).__str__()
    tag5_date = (now + datetime.timedelta(5)).__str__()
    tag6_date = (now + datetime.timedelta(6)).__str__()
    tag7_date = (now + datetime.timedelta(7)).__str__()

    return render(request, 'calendar.html', {
        'all': alle_timer,
        'all_fields': all_fields,
        #'day_difference': day_difference,
        'now': now,
        'tag1': tag1,
        'tag2': tag2,
        'tag3': tag3,
        'tag4': tag4,
        'tag5': tag5,
        'tag6': tag6,
        'tag7': tag7,
        'tag1_date': tag1_date,
        'tag2_date': tag2_date,
        'tag3_date': tag3_date,
        'tag4_date': tag4_date,
        'tag5_date': tag5_date,
        'tag6_date': tag6_date,
        'tag7_date': tag7_date,
        'rabatt': rabatt,
        })

def GoToCalendarResults(request):
    day_humanized = request.POST.get('day_humanized')
    hour_start_humanized = request.POST.get('hour_start_humanized')
    hour_end_humanized = request.POST.get('hour_end_humanized')
    dauer_h_humanized = request.POST.get('dauer_h_humanized')
    unt_preis_humanized = request.POST.get('unt_preis_humanized')
    friggin_old_date = request.POST.get('friggin_old_date')
    final_red_array_string = request.POST.get('final_red_array')
    context = {
        'day_humanized': day_humanized,
        'hour_start_humanized': hour_start_humanized,
        'hour_end_humanized': hour_end_humanized,
        'dauer_h_humanized': dauer_h_humanized,
        'unt_preis_humanized': unt_preis_humanized,
        'friggin_old_date': friggin_old_date,
        'final_red_array': final_red_array_string,
    }
    '''
    friggin_old_date = request.POST.get('friggin_old_date')
    final_red_array_string = request.POST.get('final_red_array')
    final_red_array = final_red_array_string.split(',')
    valgt_dato = Time.objects.get(date=friggin_old_date)

    if 'acht_1' in final_red_array:
        valgt_dato.acht_1 = False
        valgt_dato.save()
    
    if 'acht_2' in final_red_array:
        valgt_dato.acht_2 = False
        valgt_dato.save()
    
    if 'acht_3' in final_red_array:
        valgt_dato.acht_3 = False
        valgt_dato.save()
    
    if 'acht_4' in final_red_array:
        valgt_dato.acht_4 = False
        valgt_dato.save()

    if 'neun_1' in final_red_array:
        valgt_dato.neun_1 = False
        valgt_dato.save()
    
    if 'neun_2' in final_red_array:
        valgt_dato.neun_2 = False
        valgt_dato.save()
    
    if 'neun_3' in final_red_array:
        valgt_dato.neun_3 = False
        valgt_dato.save()
    
    if 'neun_4' in final_red_array:
        valgt_dato.neun_4 = False
        valgt_dato.save()

    if 'zehn_1' in final_red_array:
        valgt_dato.zehn_1 = False
        valgt_dato.save()
    
    if 'zehn_2' in final_red_array:
        valgt_dato.zehn_2 = False
        valgt_dato.save()
    
    if 'zehn_3' in final_red_array:
        valgt_dato.zehn_3 = False
        valgt_dato.save()
    
    if 'zehn_4' in final_red_array:
        valgt_dato.zehn_4 = False
        valgt_dato.save()

    if 'elf_1' in final_red_array:
        valgt_dato.elf_1 = False
        valgt_dato.save()
    
    if 'elf_2' in final_red_array:
        valgt_dato.elf_2 = False
        valgt_dato.save()
    
    if 'elf_3' in final_red_array:
        valgt_dato.elf_3 = False
        valgt_dato.save()
    
    if 'elf_4' in final_red_array:
        valgt_dato.elf_4 = False
        valgt_dato.save()

    if 'zwölf_1' in final_red_array:
        valgt_dato.zwölf_1 = False
        valgt_dato.save()
    
    if 'zwölf_2' in final_red_array:
        valgt_dato.zwölf_2 = False
        valgt_dato.save()
    
    if 'zwölf_3' in final_red_array:
        valgt_dato.zwölf_3 = False
        valgt_dato.save()
    
    if 'zwölf_4' in final_red_array:
        valgt_dato.zwölf_4 = False
        valgt_dato.save()

    if 'dreizehn_1' in final_red_array:
        valgt_dato.dreizehn_1 = False
        valgt_dato.save()
    
    if 'dreizehn_2' in final_red_array:
        valgt_dato.dreizehn_2 = False
        valgt_dato.save()
    
    if 'dreizehn_3' in final_red_array:
        valgt_dato.dreizehn_3 = False
        valgt_dato.save()
    
    if 'dreizehn_4' in final_red_array:
        valgt_dato.dreizehn_4 = False
        valgt_dato.save()

    if 'vierzehn_1' in final_red_array:
        valgt_dato.vierzehn_1 = False
        valgt_dato.save()
    
    if 'vierzehn_2' in final_red_array:
        valgt_dato.vierzehn_2 = False
        valgt_dato.save()
    
    if 'vierzehn_3' in final_red_array:
        valgt_dato.vierzehn_3 = False
        valgt_dato.save()
    
    if 'vierzehn_4' in final_red_array:
        valgt_dato.vierzehn_4 = False
        valgt_dato.save()

    if 'fünfzehn_1' in final_red_array:
        valgt_dato.fünfzehn_1 = False
        valgt_dato.save()
    
    if 'fünfzehn_2' in final_red_array:
        valgt_dato.fünfzehn_2 = False
        valgt_dato.save()
    
    if 'fünfzehn_3' in final_red_array:
        valgt_dato.fünfzehn_3 = False
        valgt_dato.save()
    
    if 'fünfzehn_4' in final_red_array:
        valgt_dato.fünfzehn_4 = False
        valgt_dato.save()

    if 'sechzehn_1' in final_red_array:
        valgt_dato.sechzehn_1 = False
        valgt_dato.save()
    
    if 'sechzehn_2' in final_red_array:
        valgt_dato.sechzehn_2 = False
        valgt_dato.save()
    
    if 'sechzehn_3' in final_red_array:
        valgt_dato.sechzehn_3 = False
        valgt_dato.save()
    
    if 'sechzehn_4' in final_red_array:
        valgt_dato.sechzehn_4 = False
        valgt_dato.save()

    if 'siebzehn_1' in final_red_array:
        valgt_dato.siebzehn_1 = False
        valgt_dato.save()
    
    if 'siebzehn_2' in final_red_array:
        valgt_dato.siebzehn_2 = False
        valgt_dato.save()
    
    if 'siebzehn_3' in final_red_array:
        valgt_dato.siebzehn_3 = False
        valgt_dato.save()
    
    if 'siebzehn_4' in final_red_array:
        valgt_dato.siebzehn_4 = False
        valgt_dato.save()

    if 'achtzehn_1' in final_red_array:
        valgt_dato.achtzehn_1 = False
        valgt_dato.save()
    
    if 'achtzehn_2' in final_red_array:
        valgt_dato.achtzehn_2 = False
        valgt_dato.save()
    
    if 'achtzehn_3' in final_red_array:
        valgt_dato.achtzehn_3 = False
        valgt_dato.save()
    
    if 'achtzehn_4' in final_red_array:
        valgt_dato.achtzehn_4 = False
        valgt_dato.save()

    if 'neunzehn_1' in final_red_array:
        valgt_dato.neunzehn_1 = False
        valgt_dato.save()
    
    if 'neunzehn_2' in final_red_array:
        valgt_dato.neunzehn_2 = False
        valgt_dato.save()
    
    if 'neunzehn_3' in final_red_array:
        valgt_dato.neunzehn_3 = False
        valgt_dato.save()
    
    if 'neunzehn_4' in final_red_array:
        valgt_dato.neunzehn_4 = False
        valgt_dato.save()

    if 'zwanzig_1' in final_red_array:
        valgt_dato.zwanzig_1 = False
        valgt_dato.save()
    
    if 'zwanzig_2' in final_red_array:
        valgt_dato.zwanzig_2 = False
        valgt_dato.save()
    
    if 'zwanzig_3' in final_red_array:
        valgt_dato.zwanzig_3 = False
        valgt_dato.save()
    
    if 'zwanzig_4' in final_red_array:
        valgt_dato.zwanzig_4 = False
        valgt_dato.save()'''

    return render(request, 'store.html', context)

def GoToResults(request):
    kunde_adr_1 = request.POST.get('kunde_adr_1_id')
    kunde_adr_2 = request.POST.get('kunde_adr_2_id')
    day_humanized = request.POST.get('day_humanized')
    hour_start_humanized = request.POST.get('hour_start_humanized')
    hour_end_humanized = request.POST.get('hour_end_humanized')
    dauer_h_humanized = request.POST.get('dauer_h_humanized')
    unt_preis_humanized = request.POST.get('unt_preis_humanized')
    møtemåte = request.POST.get('møtemåte')
    læremåte = request.POST.get('læremåte')
    kunnskapsnivå = request.POST.get('kunnskapsnivå')
    gesamtpreis_humanized = request.POST.get('gesamtpreis_humanized')
    friggin_old_date = request.POST.get('friggin_old_date')
    final_red_array_string = request.POST.get('final_red_array')
    if møtemåte == 'Vor Ort':
        munnbind = request.POST.get('munnbind')
        selbsttest = request.POST.get('selbsttest')
    else:
        munnbind = ""
        selbsttest = ""

    if møtemåte == 'Digital':
        videocall = request.POST.get('videocall')
    else:
        videocall = ""
    context = {
        'day_humanized': day_humanized,
        'hour_start_humanized': hour_start_humanized,
        'hour_end_humanized': hour_end_humanized,
        'dauer_h_humanized': dauer_h_humanized,
        'unt_preis_humanized': unt_preis_humanized,
        'møtemåte': møtemåte,
        'læremåte': læremåte,
        'kunnskapsnivå': kunnskapsnivå,
        'munnbind': munnbind,
        'selbsttest': selbsttest,
        'videocall': videocall,
        'gesamtpreis_humanized': gesamtpreis_humanized,
        'friggin_old_date': friggin_old_date,
        'final_red_array': final_red_array_string,
        'kunde_adr_1': kunde_adr_1,
        'kunde_adr_2': kunde_adr_2,
    }
    return render(request, 'results.html', context)

def send_mail_plain_with_stored_file(request):
    kunde_adr_1 = request.POST.get('kunde_adr_1')
    kunde_adr_2 = request.POST.get('kunde_adr_2')
    template_path = 'store/pdf1.html'
    day_humanized = request.POST.get('day_humanized')
    hour_start_humanized = request.POST.get('hour_start_humanized')
    hour_end_humanized = request.POST.get('hour_end_humanized')
    dauer_h_humanized = request.POST.get('dauer_h_humanized')
    unt_preis_humanized = request.POST.get('unt_preis_humanized')
    møtemåte = request.POST.get('møtemåte')
    læremåte = request.POST.get('læremåte')
    kunnskapsnivå = request.POST.get('kunnskapsnivå')
    gesamtpreis_humanized = request.POST.get('gesamtpreis_humanized')
    friggin_old_date = request.POST.get('friggin_old_date')
    final_red_array_string = request.POST.get('final_red_array')
    if møtemåte == 'Vor Ort':
        munnbind = request.POST.get('munnbind')
        selbsttest = request.POST.get('selbsttest')
    else:
        munnbind = ""
        selbsttest = ""

    if møtemåte == 'Digital':
        videocall = request.POST.get('videocall')
    else:
        videocall = ""

    rechnungsnr_length = 6
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,rechnungsnr_length)
    password = "".join(temp)

    heid = datetime.date.today()

    
    da1 = heid.strftime("%d.%m.%Y")
    
    context = {
        'day_humanized': day_humanized,
        'hour_start_humanized': hour_start_humanized,
        'hour_end_humanized': hour_end_humanized,
        'dauer_h_humanized': dauer_h_humanized,
        'unt_preis_humanized': unt_preis_humanized,
        'møtemåte': møtemåte,
        'læremåte': læremåte,
        'kunnskapsnivå': kunnskapsnivå,
        'munnbind': munnbind,
        'selbsttest': selbsttest,
        'videocall': videocall,
        'gesamtpreis_humanized': gesamtpreis_humanized,
        'kundenavn': request.user.get_full_name(),
        'kunde_adr_1': kunde_adr_1,
        'kunde_adr_2': kunde_adr_2,
        'kunde_email': request.user.email,
        'rechnungsnr': password,
        'rechnungsdatum': da1,#datetime.date.today.strftime("%d.%m.%Y"),
    }

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(float(gesamtpreis_humanized)*100)
    
        if amount > 0:
            #mail_id = request.POST.get('email', '')
            mail_id = request.user.email

            customer = stripe.Customer.create(
                email = mail_id,
                name = 'Max Mustermann',
                source = request.POST['stripeToken'],
            )

            charge = stripe.Charge.create(
                customer = customer,
                amount = amount,
                currency = 'eur',
                description = 'Test',
            )

    ##response = HttpResponse(content_type='application/pdf')
    # if download:
    ##response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #response['Content-Disposition'] = 'filename="report.pdf"'

    result_file = open('media/rechnung.pdf', 'w+b')

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=result_file)

    result_file.close()

    ################

    '''with open('media/rechnung.pdf') as f:
        self.license_file.save('rechnung.pdf', File(f))'''

    #instance = Bill(file_field=result_file)
    #instance.save()

    ################

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')


    '''message = request.POST.get('message', '')
    subject = request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')'''
    message = 'Hei,<br><br>vielen Dank für deine Buchung bei mir! Deine Unterrichtsstunde am <b>' + day_humanized + '</b> beginnt um <b>' + hour_start_humanized + '</b> Uhr und endet um <b>' + hour_end_humanized + '</b> Uhr (Dauer <b>' + dauer_h_humanized + '</b>).<br><br><br><br>Art des Treffens: <b>' + møtemåte + '</b><br><br>Ggf. Maske: <b>' + munnbind + '</b><br><br>Ggf. Selbsttest: <b>' + selbsttest + '</b><br><br>Ggf. Videocall: <b>' + videocall + '</b><br><br><br><br>Kenntnisstand:<br><br><b>' + kunnskapsnivå + '</b><br><br><br><br>Art zu lernen:<br><br><b>' + læremåte + '</b><br><br><br><br>Bei Fragen und Anregungen bzw. Terminänderungen stehe ich unter ja@julian-angres.no oder +4741397057 zur Verfügung.<br><br><br><br>Vi ses<br><br>Julian Angres'
    subject = 'Buchungsbestätigung Norsk i München'
    mail_id = request.user.email
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id, 'ja@julian-angres.no', 'ja@julian-angres.de'])
    email.content_subtype = 'html'

    anhang = open('media/rechnung.pdf', 'rb')
    email.attach('rechnung.pdf', anhang.read(), 'application/pdf')
    email.send()

    anhang.close()

    if os.path.exists('media/rechnung.pdf'):
        os.remove('media/rechnung.pdf')

    final_red_array = final_red_array_string.split(',')
    valgt_dato = Time.objects.get(date=friggin_old_date)

    if 'acht_1' in final_red_array:
        valgt_dato.acht_1 = False
        valgt_dato.save()
    
    if 'acht_2' in final_red_array:
        valgt_dato.acht_2 = False
        valgt_dato.save()
    
    if 'acht_3' in final_red_array:
        valgt_dato.acht_3 = False
        valgt_dato.save()
    
    if 'acht_4' in final_red_array:
        valgt_dato.acht_4 = False
        valgt_dato.save()

    if 'neun_1' in final_red_array:
        valgt_dato.neun_1 = False
        valgt_dato.save()
    
    if 'neun_2' in final_red_array:
        valgt_dato.neun_2 = False
        valgt_dato.save()
    
    if 'neun_3' in final_red_array:
        valgt_dato.neun_3 = False
        valgt_dato.save()
    
    if 'neun_4' in final_red_array:
        valgt_dato.neun_4 = False
        valgt_dato.save()

    if 'zehn_1' in final_red_array:
        valgt_dato.zehn_1 = False
        valgt_dato.save()
    
    if 'zehn_2' in final_red_array:
        valgt_dato.zehn_2 = False
        valgt_dato.save()
    
    if 'zehn_3' in final_red_array:
        valgt_dato.zehn_3 = False
        valgt_dato.save()
    
    if 'zehn_4' in final_red_array:
        valgt_dato.zehn_4 = False
        valgt_dato.save()

    if 'elf_1' in final_red_array:
        valgt_dato.elf_1 = False
        valgt_dato.save()
    
    if 'elf_2' in final_red_array:
        valgt_dato.elf_2 = False
        valgt_dato.save()
    
    if 'elf_3' in final_red_array:
        valgt_dato.elf_3 = False
        valgt_dato.save()
    
    if 'elf_4' in final_red_array:
        valgt_dato.elf_4 = False
        valgt_dato.save()

    if 'zwölf_1' in final_red_array:
        valgt_dato.zwölf_1 = False
        valgt_dato.save()
    
    if 'zwölf_2' in final_red_array:
        valgt_dato.zwölf_2 = False
        valgt_dato.save()
    
    if 'zwölf_3' in final_red_array:
        valgt_dato.zwölf_3 = False
        valgt_dato.save()
    
    if 'zwölf_4' in final_red_array:
        valgt_dato.zwölf_4 = False
        valgt_dato.save()

    if 'dreizehn_1' in final_red_array:
        valgt_dato.dreizehn_1 = False
        valgt_dato.save()
    
    if 'dreizehn_2' in final_red_array:
        valgt_dato.dreizehn_2 = False
        valgt_dato.save()
    
    if 'dreizehn_3' in final_red_array:
        valgt_dato.dreizehn_3 = False
        valgt_dato.save()
    
    if 'dreizehn_4' in final_red_array:
        valgt_dato.dreizehn_4 = False
        valgt_dato.save()

    if 'vierzehn_1' in final_red_array:
        valgt_dato.vierzehn_1 = False
        valgt_dato.save()
    
    if 'vierzehn_2' in final_red_array:
        valgt_dato.vierzehn_2 = False
        valgt_dato.save()
    
    if 'vierzehn_3' in final_red_array:
        valgt_dato.vierzehn_3 = False
        valgt_dato.save()
    
    if 'vierzehn_4' in final_red_array:
        valgt_dato.vierzehn_4 = False
        valgt_dato.save()

    if 'fünfzehn_1' in final_red_array:
        valgt_dato.fünfzehn_1 = False
        valgt_dato.save()
    
    if 'fünfzehn_2' in final_red_array:
        valgt_dato.fünfzehn_2 = False
        valgt_dato.save()
    
    if 'fünfzehn_3' in final_red_array:
        valgt_dato.fünfzehn_3 = False
        valgt_dato.save()
    
    if 'fünfzehn_4' in final_red_array:
        valgt_dato.fünfzehn_4 = False
        valgt_dato.save()

    if 'sechzehn_1' in final_red_array:
        valgt_dato.sechzehn_1 = False
        valgt_dato.save()
    
    if 'sechzehn_2' in final_red_array:
        valgt_dato.sechzehn_2 = False
        valgt_dato.save()
    
    if 'sechzehn_3' in final_red_array:
        valgt_dato.sechzehn_3 = False
        valgt_dato.save()
    
    if 'sechzehn_4' in final_red_array:
        valgt_dato.sechzehn_4 = False
        valgt_dato.save()

    if 'siebzehn_1' in final_red_array:
        valgt_dato.siebzehn_1 = False
        valgt_dato.save()
    
    if 'siebzehn_2' in final_red_array:
        valgt_dato.siebzehn_2 = False
        valgt_dato.save()
    
    if 'siebzehn_3' in final_red_array:
        valgt_dato.siebzehn_3 = False
        valgt_dato.save()
    
    if 'siebzehn_4' in final_red_array:
        valgt_dato.siebzehn_4 = False
        valgt_dato.save()

    if 'achtzehn_1' in final_red_array:
        valgt_dato.achtzehn_1 = False
        valgt_dato.save()
    
    if 'achtzehn_2' in final_red_array:
        valgt_dato.achtzehn_2 = False
        valgt_dato.save()
    
    if 'achtzehn_3' in final_red_array:
        valgt_dato.achtzehn_3 = False
        valgt_dato.save()
    
    if 'achtzehn_4' in final_red_array:
        valgt_dato.achtzehn_4 = False
        valgt_dato.save()

    if 'neunzehn_1' in final_red_array:
        valgt_dato.neunzehn_1 = False
        valgt_dato.save()
    
    if 'neunzehn_2' in final_red_array:
        valgt_dato.neunzehn_2 = False
        valgt_dato.save()
    
    if 'neunzehn_3' in final_red_array:
        valgt_dato.neunzehn_3 = False
        valgt_dato.save()
    
    if 'neunzehn_4' in final_red_array:
        valgt_dato.neunzehn_4 = False
        valgt_dato.save()

    if 'zwanzig_1' in final_red_array:
        valgt_dato.zwanzig_1 = False
        valgt_dato.save()
    
    if 'zwanzig_2' in final_red_array:
        valgt_dato.zwanzig_2 = False
        valgt_dato.save()
    
    if 'zwanzig_3' in final_red_array:
        valgt_dato.zwanzig_3 = False
        valgt_dato.save()
    
    if 'zwanzig_4' in final_red_array:
        valgt_dato.zwanzig_4 = False
        valgt_dato.save()

    current_user = request.user
    valgt_bruker = Profile.objects.get(user = current_user)
    if valgt_bruker.sixty_left == True:
        if dauer_h_humanized == '0 h 45 min':
            print('success')
            valgt_bruker.sixty_left = False
            valgt_bruker.fifteen_left = True
            valgt_bruker.zero_left = False
            valgt_bruker.save()
        else:
            valgt_bruker.sixty_left = False
            valgt_bruker.fifteen_left = False
            valgt_bruker.zero_left = True
            valgt_bruker.save()
    else:
        valgt_bruker.sixty_left = False
        valgt_bruker.fifteen_left = False
        valgt_bruker.zero_left = True
        valgt_bruker.save()

    return HttpResponse('Sent!')
