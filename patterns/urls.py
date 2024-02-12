from django.urls import path

from patterns.views import FormPatterns, IndexView, fred_form_view

app_name = "patterns"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("forms/", FormPatterns.as_view(), name="form-patterns"),
    path("forms/fred", fred_form_view, name="fred-form"),
]
