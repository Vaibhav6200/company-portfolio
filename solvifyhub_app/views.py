from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def business_consulting(request):
    return render(request, 'business_consulting.html')


def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        state = request.POST.get('state')
        country = request.POST.get('country')
        message = request.POST.get('message')

        mail_subject = "Solvify Hub: GOT a LEAD !!!"
        print("WE are in Contact form")
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=True,
        )
        return redirect('solvifyhub:index')
    return render(request, 'contact.html')


def service(request):
    return render(request, 'service.html')


def service_details(request):
    return render(request, 'service_details.html')


def about(request):
    return render(request, 'about.html')


def partner(request):
    return render(request, 'partner.html')


def career(request):
    return render(request, 'career.html')


def event(request):
    return render(request, 'event.html')


def event_single(request):
    return render(request, 'event_single.html')


def team(request):
    return render(request, 'team.html')


def blog(request):
    return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def overview(request):
    return render(request, 'overview.html')


def pricing(request):
    return render(request, 'pricing.html')


def feature(request):
    return render(request, 'feature.html')


def case_studie(request):
    return render(request, 'case_studie.html')


def case_studie_single(request):
    return render(request, 'case_studie_single.html')


def new_release(request):
    return render(request, 'new_release.html')


def solution(request):
    return render(request, 'solution.html')


def career(request):
    return render(request, 'career.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def portfolio_details(request):
    return render(request, 'portfolio_details.html')


def faq(request):
    return render(request, 'faq.html')


def company(request):
    return render(request, 'company.html')


def how_we_do(request):
    return render(request, 'how_we_do.html')


def how_we_do_single(request):
    return render(request, 'how_we_do_single.html')


def our_field_details(request):
    return render(request, 'our_field_details.html')
