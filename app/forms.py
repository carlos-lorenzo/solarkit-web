from django.forms import ModelForm
from .models import Viewer_Data

class Viewer_Form(ModelForm):
    class Meta:
        model = Viewer_Data
        fields = "__all__"