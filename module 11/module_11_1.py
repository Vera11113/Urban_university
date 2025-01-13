import requests
from pprint import pprint

#запрос
r = requests.get('https://api.github.com/events')
r = requests.get('https://jsonplaceholder.typicode.com/posts')
print(r.status_code)# возвращает 200 если все в порядке
print(r.headers) #возвращает http заголовки
pprint(r.text)
print(r.json())
res = requests.options('https://api.github.com/events')
r1 = requests.post('https://api.github.com/events', data={'key': 'value'}) #для данного сайта статус 404
r2 = requests.post('https://httpbin.org/post', json={'key': 'value'}) #если передаем в data, то наши данные будут в form,
#                                                                         # если в json, то наши данные будут в json
print(r1.status_code)
print(r2.status_code)
pprint(r2.json())


#сохранение фотографии с сайта
r = requests.get('https://sun1-86.userapi.com/impg/OyGxBF7Wt8exwoaNUxEInHtrShCAO3AiXQPhZw/CsxeJjuiojM.jpg?size=963x921&quality=95&sign=062c93d002e6b3a46152bc8db59e147a&type=album')

with open('test_image.png', 'wb') as file:
    file.write(r.content)

#файлы-cookie
url = 'https://music.yandex.ru/home'
r = requests.get(url)
print(r.status_code)
print(r.cookies)

cookies =  dict(cookies_are = 'working')
res = requests.get(url, cookies=cookies)
pprint(res.cookies)