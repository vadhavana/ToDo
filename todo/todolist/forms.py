from django import forms  
from todolist.models import post

# class taskList(forms.ModelForm): 
#     class Meta:
#         model = post
#         # fields ="__all__"
#         fields = ["task"]
#         labels = {
#             'task':' '
#         }

class taskList(forms.Form):
    task = forms.CharField()
