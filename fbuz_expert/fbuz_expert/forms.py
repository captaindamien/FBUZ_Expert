from django.forms import ModelForm, DateInput
from expert.models import Expertises
from django import forms
from datetime import date


class ExpForm(ModelForm):
    class Meta:
        model = Expertises
        fields = [
            'doc_type',
            'object_name',
            'exp_basis',
            'exp_subject',
            'exp_result',
            'executor_name',
            'recipient_name',
            'note',
            'media',
            'created',
        ]
        # widgets = {
        #     'created': DateInput(),
        # }

    def __init__(self, *args, **kwargs):
        super(ExpForm, self).__init__(*args, **kwargs)
        # добавление классов ко всем инпутам
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form_input'
        # self.fields['created'].widget = forms.DateInput(attrs={'type': 'date'})
        # добавление доп класа к инпуту
        self.fields['created'].widget.attrs.update({
            'class': 'date_form',
        })
        # лейблы для FileField
        self.fields['media'].widget.initial_text = "Текущий файл"
        self.fields['media'].widget.input_text = "Выбрать другой файл"


class ExportForm(forms.Form):
    from_date = forms.DateField(label='С какой даты', initial=date.today)
    after_date = forms.DateField(label='По какую дату', initial=date.today)

    def __init__(self, *args, **kwargs):
        super(ExportForm, self).__init__(*args, **kwargs)
        # добавление классов ко всем инпутам
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form_input'

