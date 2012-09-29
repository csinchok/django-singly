============================
django-singly
============================

Built for the app chicago hackathon.

#### Installation

Install singly

    > pip install -e git+https://github.com/csinchok/django-singly.git#egg=singly
	
Add 'singly' to your installed apps
 
    INSTALLED_APPS += ('singly',)
 
Add 'singly.backends.SinglyBackend' to your AUTHENTICATION_BACKENDS
 
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'singly.backends.SinglyBackend',
    )
 
Add your singly keys to your settings.py:
 
    SINGLY_CLIENT_ID = "MY SINGLY CLIENT ID"
    SINGLY_CLIENT_SECRET = "MY SINGLY CLIENT SECRET"
	
Add singly to your urls.py:
 	
    url(r'^singly/', include('singly.urls')),

Make sure you've added "django.core.context_processors.request" to your TEMPLATE_CONTEXT_PROCESSORS.
 
Define settings.SINGLY_CALLBACK_REDIRECT (Or keep the default of "/")

#### Usage

    {% load singly %}
    {% if user.is_authenticated %}
    Welcome, {{user.username}}
    {% else %}
    <a href="{% singly_login_url 'facebook' %}">Login With Facebook</a>
    <a href="{% singly_login_url 'twitter' %}">Login With Twitter</a>
    {% endif %}