from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data.get('message')

        # Validar si hay patrones maliciosos
        dangerous_patterns = ["'", "--", ";", "SELECT", "DROP", "INSERT", "DELETE", "UPDATE"]
        for pattern in dangerous_patterns:
            if pattern in message.upper():
                raise forms.ValidationError("SQL injection attempt detected.")
        
        return message
