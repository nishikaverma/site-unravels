from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View # for using Class based views
from .forms import SuggessionForm
from .models import SiteContent
import smtplib
from email.message import EmailMessage
import imghdr
from validate_email import validate_email

############## Site Content ######################################

def All_About_A_Website(request): 
    return render( request,"Site_content/ABOUT_WEBSITE.html")

def Cyber_security(request):
    return render( request,"Site_content/CYBER_SECURITY.html")


####################################################################

def home(request):

    return render(request, "home.html")
    

def contact_us(request):

    return render(request, "contact_us.html")


def about_us(request):
    
    return render(request, "about_us.html")

def suggessions(request):
    if request.method =="POST":
        filled_form = SuggessionForm(request.POST)

        if filled_form.is_valid():
            s_name =filled_form.cleaned_data['name'] # name of person
            mail_id = filled_form.cleaned_data['email'] # email of person 
            recived_suggession = filled_form.cleaned_data['suggession'] # suggession of person
            
            is_valid = validate_email( mail_id ,verify=True)

            if (is_valid== None) :
                status = Sending_mail(s_name, mail_id , recived_suggession)

                if status == True:
                    filled_form.save()
                    note = "%s, thanks for your suggession!" %(filled_form.cleaned_data['name'].capitalize())
                    filled_form= SuggessionForm()
                else:
                    note= "Sorry, your suggession didn't reached! Try again."

            else:
                note= "Please provide valid information !"

        else:
            note= "Please provide valid information !"
        
        return render(request, 'suggession_form.html',{'suggestform': filled_form, 'note': note})

    else:
        form = SuggessionForm(request.POST)
        return render(request, 'suggession_form.html',{'suggestform': form})


def Sending_mail(s_name,mail_id, recived_suggession):

    Email_address = 'unravel.site@gmail.com' # Sender's mail
    Email_password = 'nfnwequevzvmhoxt'  # Generated App password

    msg = EmailMessage()
    msg['Subject'] ='Thanks for your suggession!'
    msg ['From'] =Email_address
    msg['To'] = mail_id
    msg.set_content('Your suggession successfully reached us.')

    msg.add_alternative('''\
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <p>%s </p>
    </body>
    </html>

    ''' %(recived_suggession), subtype='html')
    
    try:

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Email_address,Email_password) # logging in to mail server
            smtp.send_message(msg) #Sending the message 
    
    except smtplib.SMTPServerDisconnected:
        print('Failed to connect to the server. Wrong user/password?')

    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
        return False

    return True


obj = SiteContent()