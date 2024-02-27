from django.urls import path
from . import views


app_name = "main"

urlpatterns=[
    
    path('',views.IndexView.as_view(),name="home"),
    path('contact/',views.ContactView.as_view(), name='contact'),
    path('portfoio/',views.PortfolioView.as_view(),name="portfolio"),
    path("portfolio/<slug:slug>",views.PortfolioDetailView.as_view(),name="slug"),
    path('blog/',views.BlogView.as_view(),name='blogs'),
    path('blog/<slug:slug>,',views.BlogDetail.as_view(), name='blogdetail')
] 