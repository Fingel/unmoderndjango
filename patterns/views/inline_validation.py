from django import forms
from django.http import HttpResponse
from django.shortcuts import render


def valid_username(username: str) -> bool:
    """
    Validation logic would go here - most likely a database lookup.
    This example just compares the string to "fred".
    """
    return username.lower() == "fred"


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not valid_username(username):
            raise forms.ValidationError("That username is taken.")
        return username


def form_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            message = "Registration successful!"
            form = RegistrationForm()  # reset the form
        else:
            message = "Please correct the above errors to continue."
        return render(
            request,
            "patterns/inline_validation/form.html",
            {"form": form, "message": message},
        )


def username_validation_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if not valid_username(username):
            return HttpResponse(b"<li>That username is taken.</li>")
        else:
            return HttpResponse(b"")


def index_view(request):
    form = RegistrationForm()
    return render(request, "patterns/inline_validation/index.html", {"form": form})
