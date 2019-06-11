from django import forms
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)


from django import forms

class FormularioContacto(forms.Form):


    asunto= forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter your asunto'}))


    usuario= forms.CharField(max_length=100, label ='E-Mail', 
                           widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email'}))

    mensaje = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
	