from django.forms import ModelForm
from .models import mypeople,ytvideos

class pform(ModelForm):
    class Meta:
        model = mypeople
        fields = ['name','description','files','pmage']



class yform(ModelForm):
    class Meta:
        model = ytvideos
        fields = ['yname','ydesc','ylink','ytmage']