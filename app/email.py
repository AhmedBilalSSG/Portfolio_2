from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import render

def Thanks(request, name, email, subject, message):
    subject = 'Thank you for contacting'
    from_email = 'ahmadbilalssg@gmail.com'
    to_email = email
    text_content = f"Thank you for contacting us. We will get back to you as soon as possible. \n"
    html_content = render_to_string('Thanks.html', {'name': name, 'email': email, 'subject': subject, 'message': message})

    try:
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        email.attach_alternative(html_content, "text/html")
        email.send()
    except:
        return render(request, 'error.html', {'error': 'Failed to send email. Check your internet connection.'})

def Trigger(request, name, email, subject, message):
    subject = 'Someone contacted you'
    from_email = 'ahmadbilalssg@gmail.com'
    to_email = 'ahmadbilalssg@gmail.com'
    text_content = f"Someone contacted you. \n"
    html_content = render_to_string('My.html', {'name': name, 'email': email, 'subject': subject, 'message': message})

    try:
        email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        email.attach_alternative(html_content, "text/html")
        email.send()
    except:
        return render(request, 'error.html', {'error': 'Failed to send email. Check your internet connection.'})