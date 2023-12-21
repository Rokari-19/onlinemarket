from django import forms
from .models import Item


CLASSES = 'w-full py-4 px-6 rounded-xl border mb-2'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'pricing', 'image')

        widgets = {
            'category':forms.Select(attrs={
                'class':CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':CLASSES
            }),
            'pricing':forms.TextInput(attrs={
                'class':CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':CLASSES
            })
        }


from django import forms
from .models import Item


CLASSES = 'w-full py-4 px-6 rounded-xl border mb-2'

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'pricing', 'image', 'is_sold')

        widgets = {
            'name':forms.TextInput(attrs={
                'class':CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':CLASSES
            }),
            'pricing':forms.TextInput(attrs={
                'class':CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':CLASSES
            })
        }