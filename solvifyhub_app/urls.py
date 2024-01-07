from django.urls import path
from . import views


app_name = 'solvifyhub'

urlpatterns = [
    path('', views.index, name="index"),
    path('business_consulting/', views.business_consulting, name="business_consulting"),
    path('contact/', views.contact, name="contact"),
    path('service/', views.service, name="service"),
    path('service_details/', views.service_details, name="service_details"),
    path('about/', views.about, name="about"),
    path('partner/', views.partner, name="partner"),
    path('career/', views.career, name="career"),
    path('event/', views.event, name="event"),
    path('event_single/', views.event_single, name="event_single"),
    path('team/', views.team, name="team"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('overview/', views.overview, name="overview"),
    path('pricing/', views.pricing, name="pricing"),
    path('feature/', views.feature, name="feature"),
    path('case_studie/', views.case_studie, name="case_studie"),
    path('case_studie_single/', views.case_studie_single, name="case_studie_single"),
    path('new_release/', views.new_release, name="new_release"),
    path('solution/', views.solution, name="solution"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio_details/', views.portfolio_details, name="portfolio_details"),
    path('faq/', views.faq, name="faq"),
    path('company/', views.company, name="company"),
    path('how_we_do/', views.how_we_do, name="how_we_do"),
    path('how_we_do_single/', views.how_we_do_single, name="how_we_do_single"),
    path('our_field_details/', views.our_field_details, name="our_field_details"),
]
