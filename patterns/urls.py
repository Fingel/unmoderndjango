from django.urls import path
from django.views.generic import TemplateView

from patterns.views.simple_forms import fred_form_view, simple_form_view

app_name = "patterns"
urlpatterns = [
    path("", TemplateView.as_view(template_name="patterns/index.html"), name="index"),
    path("simple_forms/", simple_form_view, name="simple-forms"),
    path("simple_forms/fred", fred_form_view, name="fred-form"),
]
