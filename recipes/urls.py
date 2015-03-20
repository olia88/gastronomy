__author__ = 'user'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'gastronomy.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^page/all/$', 'recipes.views.recipes'),
                       url(r'^page/(?P<recipe_id>\d+)/$', 'recipes.views.recipe'),
                       )
