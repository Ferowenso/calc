from sys import platform
import shelve, os.path, math, datetime, random, time,os, sys, json
from pprint import pprint
try:
    import requests
except:
    print("Кхем, у вас нет requests, без него калькулятор не совсем работать буит. Напишите андрею\поставьте сами через pip")
    sys.exit()
#Класс для работы с именем и фамилией
class Ti():
    def __init__(self, name, age, money=0, job=None):
        self.name = name
        self.age = age
        self.money = money
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def __str__(self):
        return "Ваше имя: {}, ваша фамилия {}, ваш возраст: {}".format(bob.name.split()[0], bob.name.split()[-1],
                                                                       bob.age)
    def loggin(self):
        while True:
            self.name = input("Введите имя  и фамилию ")
            if not self.name:
                print("ВВЕДИ ИМЯ И ФАМЛИИЮ, СУКА")
                continue
            else:
                break
        while True:
            try:
                self.age = int(input("Введите возраст "))
            except ValueError:
                print("А-та-та, цука вводи цифры")
                continue
            else:
                break
    def res(self):
        while True:
            self.name = input("Ведите новое имя и фамилию")
            if not self.name:
                print("ТЕБЕ СУКА СКАЗАЛИ, ВВОДИ ИМЯ И ФАМИЛИЮ. Кхм")
                continue
            else:
                break
        while True:
            try:
                self.age = int(input("Введите новый возраст "))
            except ValueError:
                print("А-та-та, цука вводи цифры")
                continue
            else:
                bob = Ti(name=self.name, age=self.age)
                with shelve.open("db66") as states:
                    states["боб"] = bob
                break
    def rmdb(self):
        print("Удаление данных о тебе, товарищ {}".format(bob.name))
        while 1:
            print("Y/N")
            vopros = input()
            if vopros =="Y":
                print("ок, ща")
                if platform == "win32":
                    os.remove("db66.dat")
                    os.remove("db66.bak")
                    os.remove("db66.dir")
                else:
                    os.remove("db66")
                sys.exit()
                break
            if vopros == "N":
                print("ну как хош")
                break



#проверка, запускалось ли раньше
if platform == "win32":
    x = os.path.isfile("db66.dat")
else:
    x = os.path.isfile("db66")
if x:
    with shelve.open("db66") as states:
        bob = states["боб"]
        print("А вы, товарищ {}, не новичок" .format(bob.name))
if x == False:
    bob = Ti(name=None, age=None)
    bob.loggin()
    bob = Ti(name=bob.name, age=bob.age)
    with shelve.open("db66") as states:
        states["боб"] = bob
        print("Атлишна, терь, {}, мы напишем о тебе в фсб".format(bob.name))
spravka = """Значт щас буит перечень всего, чо умеет эта прога  и как этим пользоваться
Щобы сбросить свое имя и возраст - напишите сбросить
Щобы увидеть автора сие дичи - напишите автор
Щобы усе закончить - напишите стоп
Щобы узнать ваше имя и возраст - я
Щобы изменить свое имя или возраст - изменить
Щобы открыть калькулятор - калькулятор
Щобы удалить данные о себе - удалить
Щобы очистить терминал/строку где вы пишите - очистить
Щобы подбросить монетку - монета
Щобы узнать шанс чего либо - шанс
Щобы узнать прогноз погоды - погода
"""
#удалить бд и вырубить калькулятор
#калькулятор
def calc1():
    while True:
        print("Для выхода из калькулятора - stop, во время выбора действия с цифрами")
        print("це калькулятор, что можно с ним сделать: \n Деление, Умножение, Сложение, Вычитание, Степень, Корень, Косинус, Синус")
        try:
            x = int(input("Введите первое число "))
            y = int(input("Введите второе число "))
        except ValueError:
            print("А-та-та, цука вводи цифры")
        else:
            f = input("Что вам нужно? ")
            if f.lower() == "синус":
                print("Результат: {} и {}".format(math.sin(x), math.sin(y)))
            if f.lower() == "степень":
                print("Результат: {}".format(x ** y))
            if f.lower() == "косинус":
                print("Результат: {} и {}".format(math.cos(x), math.cos(y)))
            if f.lower() == "корень":
                try:
                    print("Результат: {} и {}".format(math.sqrt(x), math.sqrt(y)))
                except ValueError:
                    print("У сука, вселенную разрушить хочешь?")
                    continue
            if f.lower() == "умножение":
                print("Результат: {}" .format(x*y))
            elif f.lower() == "сложение":
                print( "Результат: {}".format(x + y))
            elif f.lower() == "вычитание":
                print ("Результат: {}".format(x - y))
            elif f.lower() == "деление":
                try:
                    print("Результат: {}".format(x/y))
                except (ValueError, ZeroDivisionError):
                    print("НА НОЛЬ ДЕЛИТЬ НИЗЯ, ЧО ТЫ НАТВОРИЛ, ПЛАНЕТА УНИЧТОЖАЕТСЯ")
            elif f.lower() == "stop":
                break
# портирование
def clrclear():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
#данные
vkk = "https://vk.com/slava_a_i_r"
cozdal = "Андрей Марков"
betat = "Виктория Антонец"
betatv = "https://vk.com/starozhilam_slava"
def seckretfunc():
    global avtorsiepizdeca
    print("Ибать, как ты это нашел? Возможно ты андрей, или копался в коде")
    vkk = input("Новый вк создателя" )
    cozdal = input("Новое имя создателя" )
    betat = input("Новый бета тестер" )
    betatv = input("Новый вк бета-тестера")
    avtorsiepizdeca = "Создал: {}, вк: {}, бета-тестер: {},  вк бета-тестера: {} ".format(cozdal, vkk, betat, betatv)
avtorsiepizdeca = "Создал: {}, вк: {}, бета-тестер: {},  вк бета-тестера: {} ".format(cozdal, vkk, betat, betatv)

if platform == "win32":
    print("Таки вы на винде, всо с вами ясна")
elif platform == "linux":
    print("Таки вы на линуксе, мое увожение")
    os.system("cowsay во славу аир")
else:
    print("у вас, возможно, не буит работать clear")
print("{}, для вызова справки - напишите хелп\n" .format(bob.name))
#меин меню
def randomorgmain(random1, random2):
    global random
    url = "https://api.random.org/json-rpc/2/invoke"
    mykey = "cb5861a7-60c0-4513-af5b-f8df81aa8e7e"
    headers = {'content-type': 'application/json'}
    data = {'jsonrpc':'2.0',
           'method':'generateIntegers','params':
           {'apiKey':mykey,
           'n':1
           ,'min':random1
           ,'max':random2}
          ,'id':24565}
    params = json.dumps(data)
    try:
        r = requests.post(url, params, headers=headers, timeout=5)
        encode = r.json()
        random = encode["result"]["random"]["data"]
    except:
        print("""{}, рандом орг не смог прислать нам рандом, причин на это может быть много
Например вы пустили программу тор, или увас нет инета, или у нас закончился лимит на запросы.
Ну, собсна: Не так важно. На этот раз используем программный рандом \n """ .format(bob.name))
        import random
        randomrecue = random.randint(random1, random2)
        random = []
        random.append(randomrecue)

def orelireshka():
    print("""Весь рандом предоставляет - https://www.random.org/ ,
андрей тут неприделах. Хотите убедиться - смотрите код\n""")
    print("Подбрасываем монетку..")
    randomorgmain(0, 2)
    if random[0] == 0:
        print("Орел")
    elif random[0] == 1:
        print("Решка")
    else:
        print("Карась")
def chanc():
    print("""Весь рандом предоставляет - https://www.random.org/ ,
андрей тут неприделах.Хотите убедиться - смотрите код\n""")
    b = input("Шанс чего? ")
    randomorgmain(0, 100)
    print("Шанс {}: {}%" .format(b, random[0]))
def titry():
    print("Проект меттатон на питоне, так же известный как калькулятор")
    time.sleep(1)
    print("Идея и реализация: Андрей Марков")
    time.sleep(1)
    print("Бета-тестер: Виктория Антонец")
    time.sleep(1)
    print("Помощь с рандомом в монетке: Челик из беседы по линуксу, в душе не ебу как его зовут")
    time.sleep(1)
    print("Помощь с калькулятором: Данила Марков\Комаров")
    time.sleep(1)
    print("А так же..Вы, " + bob.name)
money = 0
def jobmain():
    global money
    with shelve.open ("db66") as states:
        try:
            money = states["бабло"]
        except KeyError:
            states["бабло"] = money
    print("Напишите << работать >>, чтобы работать")
    jobtest = input()
    if jobtest == "работать":
        money = money +1
        print("Ваше бабло: {}" .format(money))
        with shelve.open ("db66") as states:
            states["бабло"] = money
    else:
        print("ТЕ СКАЗАЛИ ПИСАТЬ РАБОТАТЬ - ЗНАЧТ ПИШИ")
def pogoda():

    apikey = "22c7bf8e593c47b0cf88f390e8e5376a"
    print("Бета-версия прогноза погоды на сегодняшний день, возможно есть баги")
    city = input("введите город на английском:" )
    city = city.lower()
    mainurl = "http://api.openweathermap.org/data/2.5/find"
    payload = {"q": city, "APPID": apikey, "units": "metric", "lang": "ru"}
    r = requests.get(mainurl, params=payload)
    encode = r.json()
    try:
        temp = encode["list"][0]["main"]["temp"]
        vlaga = encode["list"][0]["main"]["humidity"]
        nacia = encode["list"][0]["sys"]["country"]
        pagoda = encode["list"][0]["weather"][0]["description"]
        speedveta = encode["list"][0]["wind"]["speed"]
    except:
        print("Такого города нет в базе, или же вы сделали шота не так")
        sys.exit()
    print("""Температура в {}: {},
влажность: {},
скорость ветра: {}м/с
погода\облачность: {} """ .format(city, temp, vlaga, speedveta, pagoda))
    if nacia == "RU":
        print("РУССКИЕ ВПЕРЕД")
    if nacia == "UA":
        print("слава украине \n хероям сала")

while True:
    text = input("\n Вашъ запрос?")
    if text.lower() == "стоп":
        titry()
        break
    elif text.lower() == "хелп":
        print(spravka)
    elif text.lower() == "я":
        print(bob)
    elif text.lower() == "калькулятор":
        calc1()
    elif text.lower() == "изменить":
        bob.res()
    elif text.lower() == "сбросить":
        bob.rmdb()
    elif text.lower() == "очистить":
        clrclear()
    elif text.lower() == "slavaair":
        seckretfunc()
    elif text.lower() == "автор":
        print(avtorsiepizdeca)
    elif text.lower() == "монета":
        orelireshka()
    elif text.lower() == "шанс":
        chanc()
    elif text.lower() == "работа":
        jobmain()
    elif text.lower() == "погода":
        pogoda()

    else:
        print("Чел, ты неправильно запрос ввел")
