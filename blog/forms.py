from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    def __str__(self):
        return self.title


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name.', max_length=100)

    def __str__(self):
        return self.your_name


class ContactForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def __str__(self):
        return self.subject
