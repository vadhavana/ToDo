from django import forms

class inputForm(forms.Form):
    List = forms.CharField(
        widget=forms.TextInput(
            
            attrs={
                "class":"form form-control col-md-6",
                "placeholder":"Type What To Do!!"
                }    
            )
        )