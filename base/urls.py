from django.urls import path
from django.views.generic import TemplateView


app_name = "base"
urlpatterns = [
    path("", TemplateView.as_view(template_name="base/index.html"), name="index"),
    path(
        "libraries",
        TemplateView.as_view(template_name="base/libraries.html"),
        name="libraries",
    ),
]
