from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserCreateForm(UserCreationForm):

    
    class Meta:
        profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
        fields = ("username", "email", "password1", "password2",)
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
