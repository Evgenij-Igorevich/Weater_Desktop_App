import eel
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. Portuguese
owm = OWM('920e2db9be67ebd77576e913394b42b1', config_dict)

# Инициализируем библиотеку eel dsadsadsa
eel.init('web')

# Вызываемая Python функция с помощью JS
@eel.expose
def get_weather(place): # Берем данные погоды с помощью библиотеки pyowm
    mgr = owm.weather_manager() # Подключаю погодный менеджер
    city = place # в переменную сити будет записываться название города
    observation = mgr.weather_at_place(city) # Передаю данные о название города
    w = observation.weather # Принимаю массив с данными о погоде в городе city
    temp = w.temperature('celsius') # Выбираю из массива значение которое в цельсиях
    temp_min = int(temp['temp_min'])
    temp_max = int(temp['temp_max'])
    feels_like = int(temp['feels_like'])
    # Скорость ветра
    speed = w.wind()['speed']
    speed = round(speed * 3.6)
    # Влажность
    humidity = w.humidity
    # Облачность
    clouds = w.clouds
    # Детальный статус
    detailed_status = w.detailed_status
    # Время когда последний раз брали данные о погоде
    reference_time = w.reference_time('iso')
    temp = int(temp['temp']) # Получаю значение какая температура
    three_h_forecaster = mgr.forecast_at_place(city, '3h')
    # Is it going to rain tomorrow?
    tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
    three = three_h_forecaster.will_be_rainy_at(tomorrow)  # True
    if three == True:
        three = 'Будет'
    else:
        three = 'Не будет'


    if detailed_status == 'ясно':
        detailed_status = 'ясное'
    elif detailed_status == 'пасмурно':
        detailed_status = 'пасмурное'


    return (
        "В городе " + city + " сейчас " + str(temp) + " ℃, " + "ощущается как " + str(feels_like)
         + " ℃, " + "</br>" + "Минимальная температура сегодня " + str(temp_min) + " ℃, " + " Максимальная "
         + str(temp_max) + " ℃, " + "<br>" + 'Скорость ветра ' + str(speed) + ' км/ч' + '<br>' " Влажность, "
         + str(humidity) + "% " + " Облачность " + str(clouds)+ "%, " + '<br>' + "Небо: " + detailed_status
         + "<br>" + "Данные за " + str(reference_time) + '<br>' + 'Будет ли завтра дождь? - ' + three )

# Запускаем main.html с помощью eel интерфейса
eel.start('main.html', size=(700, 550))
