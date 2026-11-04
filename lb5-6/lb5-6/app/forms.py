from django import forms

class ContactForm(forms.Form):
    # 1. Текстове поле з обмеженням довжини (10-50 символів)
    name = forms.CharField(
        label='Ім’я та прізвище',
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Іван Іванов'})
    )

    # 2. Поле електронної пошти
    email = forms.EmailField(
        label='Електронна пошта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'})
    )

    # 3. Поле вибору зі списку варіантів (ChoiceField)
    topic = forms.ChoiceField(
        label='Тема звернення',
        choices=[
            ('general', 'Загальне запитання'),
            ('tech', 'Технічна підтримка'),
            ('feedback', 'Відгук або пропозиція'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # 4. Багаторядкове текстове поле
    message = forms.CharField(
        label='Повідомлення',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введіть ваше повідомлення...'})
    )

    # Кастомна валідація для поля 'name' через метод clean_name()
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Ім’я не повинно містити цифр!')
        return name

    # Додаткова валідація для 'message' (мінімум 2 слова)
    def clean_message(self):
        message = self.cleaned_data.get('message')
        words = message.split()
        if len(words) < 2:
            raise forms.ValidationError('Повідомлення має містити щонайменше 2 слова!')
        return message