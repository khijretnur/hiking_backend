from django import forms
from .models import PrivacyStatement


class PrivacyStatementAdminForm(forms.ModelForm):
    class Meta:
        model = PrivacyStatement
        fields = '__all__'

    def clean(self):
        # Check if an instance already exists
        existing_instances = PrivacyStatement.objects.count()
        if existing_instances >= 1 and self.instance.pk is None:
            raise forms.ValidationError('Разрешен только один файл.')