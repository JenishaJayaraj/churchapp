from django import forms  
from churchapp.models import Subsribers  
  
class SubForm(forms.ModelForm):  
    class Meta:  
        model = Subsribers  
        fields = "__all__"  