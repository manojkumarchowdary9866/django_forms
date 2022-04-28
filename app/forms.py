from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('django','DJANGO'),('sql',"SQL")]
class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18,max_value=55)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

class TopicForm(forms.Form):
    tn=forms.CharField(max_length=100)