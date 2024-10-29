from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    email_address = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    category = forms.ChoiceField(label='Услуга', choices=(("Автомойка", "Автомойка"), ("Техобслуживание", "Техобслуживание"), ("Шиномонтаж", "Шиномонтаж")))
    message = forms.CharField(label='Описание проблемы', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), max_length=1000)


class ReviewForm(forms.Form):
    name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    review = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }), max_length=150)
    # slug = forms.SlugField(max_length=100, label='url_reviews')
    # created_at = forms.DateTimeField(label="Дата создания комментария", widget=forms.DateTimeField())


# class ContactForm(forms.Form):
#     email_address = forms.EmailField(max_lenght=150)
#     first_name = forms.CharField(max_length=50)
#     phone_number = forms.IntegerField(max_length=11)
#     last_name = forms.CharField(max_length=50)
#     category = forms.ChoiceField(choises=((1, "Автомойка"), (2, "Техобслуживание"), (3, "Шиномонтаж")))


