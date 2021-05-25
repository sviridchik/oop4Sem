from sqlite3 import ProgrammingError

from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.views.generic.base import View

from .models import *
from .forms import RegistrForm
from django.contrib import messages
import random


# 1
def start(request):
    return render(request, 'start.html', {'title': 'Start'})


def home(request):
    return render(request, 'home.html', {'title': 'Home'})


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def definite(request):
    return render(request, 'definite.html')


# def signin(request):
#     return render(request, 'signin.html')

# def signup(request):
#     return render(request, 'signup.html')

def indefinite(request):
    return render(request, 'indefinite.html')


def country_page(request):
    countries = Country.objects.all()
    return render(request, "test.html", {'countries': countries})


def home(request):
    return render(request, 'home.html', {'title': 'Home'})


def country_info(request):
    return render(request, 'country_info.html')


def contacts(request):
    if request.method == 'POST':
        send_mail(
            f'Вопрос от клиента {request.POST["name"]}',
            f'''Почта клиента: {request.POST["email"]}
Вопрос клиента: {request.POST["message"]} ''',
            'avivasite007@gmail.com',
            ['viccisviri@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, 'Ваше письмо отправлено, ожидайте ответа')
    return render(request, 'contacts.html')


def get_info(request):
    countries = Country.objects.all()
    photos = ["media/10.jpeg", "media/11.jpeg", "media/12.jpeg", "media/13.jpeg", "media/14.jpeg", "media/15.jpeg",
              "media/16.jpeg"]
    if request.method == 'POST':
        person = request.user.person_set.get()
        try:
            promocode = PromoCode.objects.get(content=request.POST['promocode'].strip())
        except PromoCode.DoesNotExist:
            messages.error(request, f'Промокод {request.POST["promocode"]} не найден')
        else:
            if promocode.discount < person.discount:
                messages.error(request, f'У Вас уже активирован промокод на больший процент')
            else:
                person.discount = promocode.discount
                person.save()
                messages.success(request,
                                 f'Вы ввели промокод {promocode.content}. Теперь у Вас скидка - {person.discount}%')
    return render(request, 'country_info_template.html', {'countries': countries, 'photos': photos})


def climate_info(request):
    climates = Climate.objects.all()
    countries = Country.objects.filter()
    return render(request, 'climate.html', {'climates': climates})


def language_info(request):
    languages = Language.objects.all()
    # countries = Country.objects.filter()
    return render(request, 'language_teplate.html', {'languages': languages})


def religion_info(request):
    religions = Religion.objects.all()
    return render(request, 'religion.html', {'religions': religions})


def med_info(request):
    meds = Med.objects.all()
    return render(request, 'med.html', {'meds': meds})


def trans_info(request):
    translators = Translator.objects.all()
    return render(request, 'translators.html', {'translators': translators})


def hotels_info(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})


def entertain_info(request):
    entertains = Entertainment.objects.all()
    return render(request, 'entertain.html', {'entertains': entertains})


def attraction_info(request):
    attractions = Attractions.objects.all()
    return render(request, 'attractions.html', {'attractions': attractions})


def restriction_info(request):
    restrictions = Restriction.objects.all()
    return render(request, 'restrictions.html', {'restrictions': restrictions})


def currency_info(request):
    currencies = Currency.objects.all()
    return render(request, 'currency.html', {'title': 'Currency page', 'currencies': currencies})


def login_form(request, form):
    user = form.get_user()
    login(request, user)


def signin(request):
    data = {}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # form.save()
            login_form(request, form)
            # user = form.get_user()
            # login(request, user)
            messages.success(request, "success")
            data['form'] = form

            # data['res'] = "Всё прошло успешно"
            return redirect('/home')
        else:
            data['form'] = form
            messages.error(request, "user-durak")
            # form = UserCreationForm()
            # return render(request, 'auth.html', data)
    else:
        form = AuthenticationForm()
        data['form'] = form
    return render(request, 'auth.html', data)


def signup(request):
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "success")
            data['form'] = form
            # data['res'] = "Всё прошло успешно"
            return redirect('/home')
        else:
            data['form'] = form
            messages.error(request, 'user-durak')
            # form = UserCreationForm()
            # return render(request, 'auth.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
    return render(request, 'registr.html', data)


class AddToCartView(View):

    def get(self, request, *args, **kwargs):
        print(request)
        return HttpResponseRedirect('/cart')


class CartView(View):
    def get(self, request, *args, **kwargs):
        person = Person.objects.get(user=request.user)
        cart = Cart.objects.get()


def packets(request, title):
    country = Country.objects.get(title=title)
    return render(request, 'packets.html', {'packets': country.packet_set.all()})


def packet(request, pk):
    packet = Packet.objects.get(idPacket=pk)
    return render(request, 'packet.html', {'packet': packet, 'total_price': packet.duration * packet.price})


class Error:
    def __init__(self, content, useful_link='', link_text=''):
        self.id = None
        self.content = content
        self.useful_link = useful_link
        self.link_text = link_text


def error_iterator(packet, person):
    errors = []

    if packet.country.lang.title.lower() not in (lang.lower() for lang in person.languages.split()):
        errors.append(Error(
            content=f'Язык страны - {packet.country.lang} не был найден в Ваших языках',
            useful_link='/translators',
            link_text='Переводчики',
        ))

    phobias = []

    for person_phobia in person.phobias.split():
        for packet_phobia in packet.country.restriction.phobias.split():
            if person_phobia.lower() == packet_phobia.lower():
                phobias.append(person_phobia)

    for phobia in phobias:
        errors.append(Error(
            content=f'Фобия: {phobia}'
        ))

    person_vaccinations = set(person.vaccition.split())
    packet_vaccinations = set(packet.country.restriction.necessary_vaccation.split())

    for vaccination in packet_vaccinations.difference(person_vaccinations):
        errors.append(Error(
            content=f'Нет необходимой вакцинации: {vaccination}',
            useful_link=packet.country.restriction.medical_institution.link,
            link_text=packet.country.restriction.medical_institution,
        ))

    for i in range(len(errors)):
        errors[i].id = str(i)

    # return errors
    for error in errors:
        yield error


def packet_result(request, pk):
    packet = Packet.objects.get(idPacket=pk)
    person = request.user.person_set.get()
    ignored_id = []

    ignored_id.extend(request.GET.keys())

    errors = list(filter(lambda error: error.id not in ignored_id, error_iterator(packet, person)))

    if not errors:
        if person.order is not None:
            person.order.delete()
        order = Order.objects.create(idOrder=person.id, status='p',
                                     price=packet.price * packet.duration, packet=packet)
        person.order = order
        person.save()

        # Person.objects.filter(user=person.user).update(order=order)

    return render(request, 'packet_result.html',
                  {'packet': packet, 'errors': errors,
                   'ignored_id': '&'.join(ignored_id)})


def quiz(request):
    try:
        questions = Quiz.load().questions.all()
    except ProgrammingError:
        pass

    try:
        person = request.user.person_set.get()
    except Person.DoesNotExist:
        return render(request, 'quiz.html', {'questions': questions})

    if request.method == 'POST':
        for question, answer in request.POST.items():
            if question.startswith('question'):
                person.quiz_answers.add(QuizAnswer.objects.get(pk=answer))

        good_answers = list(person.quiz_answers.filter(is_right=True))
        random.seed(person.id * 1234 + len(good_answers))
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
        rand_str = "".join(random.choice(chars) for _ in range(15))
        promocode, is_created = PromoCode.objects.get_or_create(content=rand_str,
                                                                discount=len(good_answers))

        messages.success(request,
                         f'Вы ответили на {len(good_answers)} вопросов из {len(QuizQuestion.objects.all())}. Тем самым выиграли промокод {promocode} на {promocode.discount}% скидки.\nВведите его в поле промокодов чтобы активировать или поделитись им с друзьями.')

    person_answers = person.quiz_answers.all()
    answered_questions = [answer.question for answer in person_answers]
    # questions = QuizQuestion.objects.all()
    return render(request, 'quiz.html',
                  {'questions': questions, 'person_answers': person_answers, 'answered_questions': answered_questions})
