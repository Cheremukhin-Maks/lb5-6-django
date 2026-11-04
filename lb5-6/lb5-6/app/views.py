from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import ContactForm

def home_view(request):
    context = {
        'page_title': 'Головна блогу',
        'main_heading': 'Вітаємо на нашому навчальному порталі!',
        'total_visitors': 150,
        'description': 'Це навчальний проєкт для вивчення вебфреймворку Django та роботи з шаблонами.',
        'links': {'Про нас': '/about/', 'Список статей': '/posts/'}
    }
    return render(request, 'app/home.html', context)

def posts_view(request):
    context = {
        'page_title': 'Список опублікованих статей',
        'posts': [
            {'title': 'Вступ до Django', 'views': 120},
            {'title': 'Робота з DTL шаблонами', 'views': 85},
            {'title': 'Міграції та БД', 'views': 45},
        ]
    }
    return render(request, 'app/posts_list.html', context)

def about_view(request):
    return render(request, 'app/home.html', {'page_title': 'Про нас', 'main_heading': 'Про проєкт', 'total_visitors': 1})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            messages.success(request, 'Дякуємо! Ваше повідомлення успішно відправлено.')
            return redirect('contact')  
    else:
        form = ContactForm()  

    return render(request, 'app/contact.html', {'form': form, 'page_title': 'Форма зворотного зв’язку'})