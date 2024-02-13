from django.urls import path
from django.views.generic import TemplateView

from patterns.views import simple_forms

app_name = "patterns"
urlpatterns = [
    path("", TemplateView.as_view(template_name="patterns/index.html"), name="index"),
    path("simple_forms/", simple_forms.index_view, name="simple-form-index"),
    path("simple_forms/form", simple_forms.form_view, name="simple-form"),
]
