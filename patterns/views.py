from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    template_name = "patterns/index.html"


example_choices = [
    ("yes", "We are so back!"),
    ("no", "It's so over."),
    ("maybe", "I'm not sure."),
]


class FredForm(forms.Form):
    name = forms.CharField(max_length=100)
    are_we_back = forms.ChoiceField(label="Are we back?", choices=example_choices)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name.lower() == "fred":
            raise forms.ValidationError("NO Freds allowed!")
        return name


def fred_form_view(request):
    if request.method == "POST":
        form = FredForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            form = FredForm()
            return render(
                request, "patterns/forms/fred_form_submitted.html", {"name": name}
            )
    else:
        form = FredForm()

    return render(request, "patterns/forms/fred_form.html", {"form": form})


class FormPatterns(View):
    async def get(self, request):
        form = FredForm()
        return render(request, "patterns/forms/formpatterns.html", {"form": form})
