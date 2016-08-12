from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

from gpauth.models import User

__author__ = "Gilson Paulino"
__copyright__ = "Copyright 2016"
__email__ = "gilsonbp@gmail.com"

AuthenticationForm.base_fields['username'].widget.attrs['autocomplete'] = 'off'
AuthenticationForm.base_fields['password'].widget.attrs['autocomplete'] = 'off'


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('login', 'name',)

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords are not equal.")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text="There is no way to see the user's password, "
                                                   "but you can change the password using "
                                                   "<a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = ('login', 'password', 'name', 'email', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]


class UserCustomAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('login', 'get_full_name', 'email', 'is_superuser', 'is_active',)
    list_display_links = list_display
    list_filter = ('is_superuser', 'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('login', 'name', 'email', 'password',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('date_joined', 'last_login',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('login', 'name', 'password1', 'password2',)}),
    )
    search_fields = ('name', 'login', 'email',)
    ordering = ('name',)
    filter_horizontal = ('user_permissions',)

    list_per_page = 30

    actions_on_top = True
    actions_on_bottom = True


admin.site.register(User, UserCustomAdmin)
