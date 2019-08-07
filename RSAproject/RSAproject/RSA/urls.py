from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from RSA import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about', views.AboutPageView.as_view()),
    url(r'^action3', views.SpecifyFileNamesPageView),
    url(r'^action4', views.upload_file_encrypt),
    url(r'^action5', views.upload_file_to_decrypt)
]

# set up to use file-upload function
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

