from django import forms

from .models import Profile


# class ProfileForm(forms.Form):
#     id = forms.CharField(max_length=100)
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=100)
#     role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
#     phone = forms.IntegerField(required=False)
#     house_name = forms.CharField(max_length=100)
#     street = forms.CharField(max_length=100)
#     landmark = forms.CharField(max_length=100)
#     pincode = forms.CharField(max_length=10)
#     city = forms.CharField(max_length=100)
#     state = forms.CharField(max_length=100)
#     country = forms.CharField(max_length=100)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["created_at", "updated_at", "is_active", "is_verified"]
