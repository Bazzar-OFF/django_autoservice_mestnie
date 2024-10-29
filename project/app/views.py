from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Service, Reviews

from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, ReviewForm
from django.contrib import messages


def index(request):
    return render(request, 'app/index.html')

def car_wash(request):
    return render(request, 'app/car_wash.html')

def mainenance(request):
    return render(request, 'app/mainenance.html')

def tire_service(request):
    return render(request, 'app/tire_service.html')



# def reviews(request):
#     review = Reviews
#     return render(request, 'app/reviews.html', {'reviews': reviews})


def add_review(request):
    if request.method == 'POST':
        re_form = ReviewForm(request.POST)
        if re_form.is_valid():
            # print(re_form.cleaned_data)
            Reviews.objects.create(**re_form.cleaned_data)
            return redirect('reviews')
    else:
        re_form = ReviewForm()
    return render(request, 'app/add_review.html', {'form': re_form})


def reviews(request):
    rev = Reviews.objects.order_by("-created_at")
    return render(request, 'app/reviews.html', {'rev': rev})


# def form(request):
#     return render(request, 'app/form.html')


def form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Test message"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
                'category': form.cleaned_data['category'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@examle.com'])
            except BadHeaderError:
                return HttpResponse('Ошибка отправки. Проверьте правильно ли введены поля')
            # return redirect("app:home")
            messages.success(request, 'Заявка отправлена! Ожидайте ответа на Почту')

    form = ContactForm()
    return render(request, "app/form.html", {'form': form})


#send_mail(subject, message,
#           'admin@example.com',
#           ['admin@examle.com'])

# send_mail(subject, message,
#         'san_sere_san03@mail.ru',
#         ['bazzar-off123@mail.ru'])



# class Home(ListView):
#     model = Category
#     template_name = 'app/index.html'
#     context_object_name = 'category'
#     paginate_by = 3
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Autoservice'
#         return context

