from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',

                       # sessions
                       url(r'^login/$', views.LoginView.as_view(), name='login'),
                       url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

                       # register
                       url(r'^register/$', views.RegisterView.as_view(), name='register'),
                       url(r'^register/success/$',
                           views.RegisterSuccessView.as_view(
                           ), name='register-success'),

                       )
