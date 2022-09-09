from django import forms

from .models import Album, Musician


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=100, widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class MusicianForm(forms.ModelForm):

    class Meta:
        model = Musician

        fields = [
            'first_name',
            'last_name',
            'birth_date',
            'instrument',
            'salary',
        ]