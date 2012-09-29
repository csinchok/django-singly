from django.conf.urls import patterns, include, url

urlpatterns = patterns('singly.views',
    (r'^callback$', 'callback'),
)