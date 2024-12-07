from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from app.models import *
from app.email import *
import feedparser

def home(request):
    person = Person.objects.all()
    about = About.objects.all()
    skills = Skills.objects.all()
    cap = Capabilities.objects.all().order_by('-id')
    education = Education.objects.all().order_by('-id')
    exp = Experience.objects.all().order_by('-id')
    proj_heading = Projects_Headings.objects.all()
    projects = Projects.objects.prefetch_related('media_project').all().order_by('-id')
    certificates = Certificates_Headings.objects.all()
    cer = Certificates.objects.all().order_by('-id')
    hire = Hire_Button_Picture.objects.all()
    head_contact = Contct_heading_Info.objects.all()
    blog_headming = Blog_Heading_Info.objects.all()
    # medium_articles = scrape_medium_articles_rss()
    medium_articles = Blog.objects.all().order_by('-id')

    return render(request, 'index-video.html', {'person': person,'about': about,'skills': skills,'cap': cap,'education': education,'exp': exp,'proj_heading': proj_heading,'proj': projects,'certificates': certificates,'cer': cer,'hire': hire,
    'head_contact': head_contact,'blog_headming': blog_headming,'medium_articles': medium_articles})

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([name, email, subject, message]):
            return JsonResponse({'message': 'All fields are required.'}, status=400)
        try:   
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            Thanks(request, name, email, subject, message)
            Trigger(request, name, email, subject, message)
            return JsonResponse({'message': 'success'})
        
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'error'}, status=400)

def scrape_medium_articles_rss():
    rss_url = 'https://medium.com/feed/@ahmadbilalssg'
    feed = feedparser.parse(rss_url)
    article_list = []
    for entry in feed.entries:
        full_description = entry.summary
        truncated_description = ' '.join(full_description.split()[:112]) + ('...' if len(full_description.split()) > 112 else '')
        article_list.append({'title': entry.title,'url': entry.link,'author': entry.author if 'author' in entry else 'Unknown','type': 'Article','platform': 'Medium', 'description': truncated_description, })
    return article_list