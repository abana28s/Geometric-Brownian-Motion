from django import forms
from django.forms import ModelForm
from .models import Graph

class BrownianForm(ModelForm):
    mu = forms.DecimalField(
        required=True, widget=forms.widgets.NumberInput(), label="μ"
    )
    sigma = forms.DecimalField(
        required=True, widget=forms.widgets.NumberInput(), label="σ"
    )
    s_0 = forms.DecimalField(
        required=True, widget=forms.widgets.NumberInput(), label="S[0]"
    )
    t = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(), label="T")
    n = forms.DecimalField(required=True, widget=forms.widgets.NumberInput(), label="N")
    no_of_paths = forms.IntegerField(required=True, widget=forms.widgets.NumberInput(), label="No. Of Paths")

    class Meta:
        model = Graph
        fields = "__all__"
