from django import forms
from django.shortcuts import render

example_choices = [
    ("yes", "We are so back!"),
    ("no", "It's so over."),
    ("maybe", "I'm not sure."),
]


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=100)
    are_we_back = forms.ChoiceField(label="Are we back?", choices=example_choices)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name.lower() == "fred":
            raise forms.ValidationError("NO Freds allowed!")
        return name


def form_view(request):
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            form = SimpleForm()
            return render(
                request, "patterns/simple_forms/form_submitted.html", {"name": name}
            )
    else:
        form = SimpleForm()

    return render(request, "patterns/simple_forms/form.html", {"form": form})


def index_view(request):
    form = SimpleForm()
    return render(request, "patterns/simple_forms/index.html", {"form": form})
