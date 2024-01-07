from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def business_consulting(request):
    return render(request, 'business_consulting.html')


def contact(request):
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
