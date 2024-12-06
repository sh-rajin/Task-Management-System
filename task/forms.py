from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets ={
            'assign_date' : forms.DateInput(attrs={'type': 'date'}),
        }
        
        
    def __init__(self,*task_forms, **task):
        instance = task.get('instance', None)
        super().__init__( *task_forms, **task )
        
        
        if instance is None:
           self.fields.pop('is_complete')
        else:
            self.fields['is_complete'].required = True
            
