from django.urls import path
from django.views.generic import TemplateView

from patterns.views import inline_validation, simple_forms

app_name = "patterns"
urlpatterns = [
    path("", TemplateView.as_view(template_name="patterns/index.html"), name="index"),
    path("simple_forms/", simple_forms.index_view, name="simple-form-index"),
    path("simple_forms/form", simple_forms.form_view, name="simple-form"),
    path(
        "inline_validation/",
        inline_validation.index_view,
        name="inline-validation-index",
    ),
    path(
        "inline_validation/form",
        inline_validation.form_view,
        name="inline-validation-form",
    ),
    path(
        "inline_validation/username",
        inline_validation.username_validation_view,
        name="inline-validation-username",
    ),
]
