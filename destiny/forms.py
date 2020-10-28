from .models import Roulette, Category, Content
from django import forms



class RouletteCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Roulette
        fields = ("title", "category",)

ContentFormset = forms.inlineformset_factory(
    Roulette, Content, fields ='__all__',
    extra=10, max_num=10,
)


class CategoryCreateForm(forms.Form):

    class Meta:
        model = Category
        fields = ("category")

