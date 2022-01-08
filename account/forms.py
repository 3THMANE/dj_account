from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(Registerform,self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class Profileform(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','email','username','bio']

    def __init__(self, *args, **kwargs):
        super(Profileform, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
