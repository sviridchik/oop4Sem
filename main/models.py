# from django.contrib.contenttypes.models import ContentType
from django.contrib import admin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from django.contrib.contenttypes import *
from django.db.models import CASCADE
from django.contrib.auth.models import User


#
# class Latest_countries_manager:
#
#     def get_contry_for_page(self,*args, **kwargs):
#         countries = []
#         ct_models = ContentType.object.filter(model_in=args)
#         for ct_model in ct_models:
#
#
# class Latest_countries:
#
#     objects = None


# Create your models here.
class p:
    pass


class Entertainment(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Цена за сутки')
    requirments = models.TextField("Требования")
    risk_of_trauma = models.IntegerField("Вероятность получения травмы")
    description = models.TextField("Описание")
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def show_requirments(self):
        return str(self.requirments).split()

    def __str__(self):
        return self.title

    def Check_ability(self, person):
        return set(self.requirments).intersection(person.abilities)

    class Meta:
        verbose_name = 'Развлечение'
        verbose_name_plural = 'Развлечения'


class Hotel(models.Model):
    entertainment = models.ForeignKey(Entertainment, verbose_name="Развлечение", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Цена')
    stars = models.IntegerField(verbose_name="Количество звезд")
    food_options = models.TextField("варианты питания")
    people_in_room = models.TextField("Сколько местные номера есть")
    swimming_pool = models.BooleanField("Наличие бассейна")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    link = models.CharField("ссылка", blank=True, max_length=255)

    # Hotel.o
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class Translator(models.Model):
    # выбор генлера
    gender_choce = [
        ("definite", (("woman", "woman"),
                      ("man", "man"),
                      )),
        ("indefinite", (("trans", "trans"),
                        ("other", "other"),))
    ]
    gender = models.CharField(max_length=100, choices=gender_choce, verbose_name="Пол")
    name = models.CharField(max_length=255, verbose_name="Имя")
    price = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Цена за час')
    experience = models.IntegerField(verbose_name="Лет опыта")
    languages = models.CharField(verbose_name="Языки", max_length=255)
    recommendation = models.TextField("Описание")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    link = models.CharField("ссылка", blank=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Переводчик'
        verbose_name_plural = 'Переводчики'


class Climate(models.Model):
    humidity = models.FloatField(max_length=2, verbose_name="влажность")
    t = models.FloatField("Температура ")
    amount_sunny_days = models.IntegerField("Количество солнечных дней в году")
    v_wind = models.FloatField("Скорость ветра")
    type_choice = [
        ("приятный", (("умеренный", "умеренный"),
                      ("тропический", "тропический")
                      )),
        ("не самый приятный", (("полярный", "полярный"),
                               ("экваториальный", "экваториальный"))
         )
    ]
    type = models.CharField(max_length=255, choices=type_choice)
    pres = models.FloatField("Атмосферное давление")
    recommendation = models.TextField("Описание")
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Климат'
        verbose_name_plural = 'Климаты'


class Language(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    family_choice = [
        ("наиболее распространенные", (
            ("Нигер – Конго", "Нигер – Конго"),
            ("Австронезийский", "Австронезийский"),
            ("Транс-новогвинейский", "Транс-новогвинейский"),
            ("Сино-тибетский", "Сино-тибетский"),
            ("Индоевропейский", "Индоевропейский"),
            ("Австралийский", 'Австралийский'),
        )),
        ("менее распространенные", (
            ("Араваканский", "Араваканский"),
            ("Манде", "Манде "),
            ("Тупиан", "Тупиан"),
        ))
    ]
    family = models.TextField("семейство", choices=family_choice, max_length=255)
    a_dial = models.IntegerField("Количество диалектов")
    speed_choice = [
        ("fast", "fast"),
        ("medium", "medium"),
        ("slow", "slow")
    ]
    speed_lern = models.CharField("Скорость освоения", choices=speed_choice, max_length=255)
    users = models.IntegerField("Количество носителей")
    price = models.FloatField(verbose_name='Цена за сутки')
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    alphabet = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.title

    def Person_lang(self, person):
        return set(self.family).intersection(person.languages)

    # ?????????????????
    # def __mul__(self, other:int):
    #     self.price*other
    #
    # def count_price_for_duration(self,duration):
    #     return (self.price.)*duration

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Med(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    av_price = models.FloatField("Средняя цена")
    working_days = models.CharField("Дни работы", max_length=255)
    link = models.CharField("ссылка", blank=True, max_length=255)
    description = models.TextField("Описание", blank=True, null=True, default=None)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мед учреждение'
        verbose_name_plural = 'Мед учреждения'


class Currency(models.Model):
    ratio = {}
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    #     converter
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'


class Restriction(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    necessary_vaccation = models.CharField("Необходитмве прививки", max_length=255)
    phobias = models.CharField("фобии", max_length=255)
    desiase = models.CharField("Заболевания", max_length=255)
    medical_institution = models.ForeignKey(Med, on_delete=models.CASCADE, verbose_name="Медицинское учреждение")

    def Person_rest(self, person):
        return set(self.necessary_vaccation).intersection(person.vaccination)

    def __str__(self):
        return self.title

    def warnings(self):
        return "Be carefull"

    class Meta:
        verbose_name = 'Ограничение'
        verbose_name_plural = 'Ограничения'


class Religion(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    monoteism = models.BooleanField("Монотеизм")
    neg_atitude = models.CharField("Недружелюбные", max_length=255)
    fasting = models.BooleanField("Пост")
    description = models.TextField("Описание", blank=True, null=True, default=None)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def Person_rest(self, person):
        return set(self.neg_atitude).intersection(person.religion)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Религия'
        verbose_name_plural = 'Религии'


class Attractions(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=9, decimal_places=3, verbose_name='Цена')
    connected_historical_facts = models.TextField("Исторические события")
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    link = models.CharField("ссылка", blank=True, max_length=255)

    # country = models.ForeignKey(Country, verbose_name="country", on_delete=models.CASCADE,
    #                                 blank=True, null=True)

    def get_tags(self):
        return str(self.tags).split()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


class Country(models.Model):
    # content_type = models.ForeignKey(ContentType,on_delete=CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    tags = models.TextField("Теги", max_length=255)
    climate = models.ForeignKey(Climate, on_delete=models.CASCADE, verbose_name="Климат")
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE, verbose_name="Ограничение")
    list_of_hotels = []
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Язык")
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, verbose_name="Религия")
    currency = models.ForeignKey(Currency, verbose_name="Валюта", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    hotel = models.ForeignKey(Hotel, verbose_name="Отель", on_delete=models.CASCADE, blank=True, null=True)
    attractions = models.ForeignKey(Attractions, verbose_name="Достопримечательности", on_delete=models.CASCADE,
                                    blank=True, null=True)

    def get_more_info(self):
        return self.tags

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


#
# class AuditEntryAdmin(admin.ModelAdmin):
#     list_display = ('timestamp', 'title')

class Packet(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    idPacket = models.PositiveIntegerField(unique=True, primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")
    duration = models.PositiveIntegerField("Продолжительность в днях")
    price = models.FloatField(verbose_name='Цена за сутки')
    amount = models.PositiveIntegerField("Количество")
    photo = models.ImageField("Изображение", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'


class Order(models.Model):
    idOrder = models.PositiveIntegerField(unique=True, primary_key=True)
    # clients = models.ForeignKey(Person, on_delete=models.CASCADE)
    status_choice = [("p", "inprogress"),
                     ("c", "canceled"),
                     ("clo", "closed")
                     ]
    status = models.CharField(choices=status_choice, max_length=255)
    price = models.FloatField(verbose_name='Общая стоимость')
    packet = models.ForeignKey(Packet, on_delete=CASCADE, blank=True)

    def __str__(self):
        return str(self.idOrder)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class QuizQuestion(models.Model):
    content = models.CharField(verbose_name='Содержание', max_length=255, unique=True)
    image = models.ImageField("Изображение", blank=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'вопрос викторины'
        verbose_name_plural = 'вопросы викторины'


class QuizAnswer(models.Model):
    content = models.CharField(verbose_name='Содержание', max_length=255)
    question = models.ForeignKey(QuizQuestion, on_delete=CASCADE, verbose_name='Вопрос')
    is_right = models.BooleanField(verbose_name='Правильный')

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'ответ викторины'
        verbose_name_plural = 'ответы викторины'


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class Quiz(SingletonModel):
    questions = models.ManyToManyField(QuizQuestion, verbose_name='Вопросы')

    def __str__(self):
        return 'Викторина авива'

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'


class Person(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    family_name = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    age = models.IntegerField("Возраст")
    gender_choce = [
        ("definite", (("w", "woman"),
                      ("m", "man"),
                      )),
        ("indefinite", (("t", "trans"),
                        ("o", "other"),))
    ]
    gender = models.CharField(max_length=100, choices=gender_choce, verbose_name="Пол", null=True, blank=True)
    # password = models.CharField(max_length=255, verbose_name="Паспорт")
    # validation re
    email = models.CharField(max_length=255, verbose_name="email", default='')
    amount_members = models.IntegerField(verbose_name="количество членов семьи", null=True, blank=True)
    abilities = models.CharField(max_length=255, verbose_name="Навыки", default='', blank=True)
    desease = models.CharField(max_length=255, verbose_name="Заболевания", default='', blank=True)
    phobias = models.CharField(max_length=255, verbose_name="Фобия", default='', blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ", null=True, blank=True)
    languages = models.CharField(max_length=255, verbose_name="Языки", default='', blank=True)
    vaccition = models.CharField(max_length=255, verbose_name="Прививки", default='', blank=True)
    phone = models.CharField(max_length=255, verbose_name="телефон", default='', blank=True)
    photo = models.ImageField("Изображение", null=True, blank=True)
    user = models.ForeignKey('auth.User', verbose_name='Пользователь', on_delete=models.CASCADE)
    discount = models.IntegerField(verbose_name="Скидка", default=0)
    quiz_answers = models.ManyToManyField(QuizAnswer, verbose_name='Ответы в викторине')
    quiz = models.ForeignKey(Quiz, verbose_name='Викторина', on_delete=models.CASCADE, null=True)

    # defs
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class CartProduct(models.Model):
    user = models.ForeignKey('Person', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE,
                             related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    person = models.ForeignKey('Person', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    packet = models.ManyToManyField(Packet, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


# class PacketWarning(models.Model):
#     person = models.ForeignKey('Person', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
#     content = models.CharField(max_length=250, verbose_name='Содержание')
#     useful_link = models.CharField(max_length=30, verbose_name='Полезная ссылка')
#     link_text = models.CharField(max_length=30, verbose_name='Текст ссылки')
# class Customer(models.Model):
#     user = models.ForeignKey(Person, verbose_name='Пользователь', on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
#     address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
#     orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')
#
#     def __str__(self):
#         return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)

class PromoCode(models.Model):
    content = models.CharField(max_length=100, unique=True)
    discount = models.IntegerField()

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
