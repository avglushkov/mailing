from django import forms
from django.forms import BooleanField
from catalog.models import Product, Contact, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin,forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        clean_data = self.cleaned_data['name']
        clean_data_words = clean_data.split()
        bad_words = ['казино',
                     'криптовалюта',
                     'крипта',
                     'биржа',
                     'дешево',
                     'бесплатно',
                     'обман',
                     'полиция',
                     'радар']

        for word in clean_data_words:
            if word.lower() in bad_words:
                raise forms.ValidationError(f'Слово {word} не может содержаться в названии продукта')

        return clean_data

    def clean_description(self):
        clean_data = self.cleaned_data['description']
        clean_data_words = clean_data.split()
        bad_words = ['казино',
                     'криптовалюта',
                     'крипта',
                     'биржа',
                     'дешево',
                     'бесплатно',
                     'обман',
                     'полиция',
                     'радар']

        for word in clean_data_words:
            if word.lower() in bad_words:
                raise forms.ValidationError(f'Слово {word} не может содержаться в описании продукта')

        return clean_data



class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

class ContactForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


