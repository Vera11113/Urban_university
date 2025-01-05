from time import sleep


class UrTube():

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None
    def log_in(self, nickname, password):
        if nickname in self.users.keys:
            if hash(self.users[nickname]) == hash(password):
                self.current_user = nickname
        else:
            print(f'Пользователь {nickname} не существует')

    def register(self, nickname, password, age):
        if nickname in self.users.keys():
            print(f'Пользователь {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users[user.nickname] = [hash(user.password), user.age]
            self.current_user = user.nickname

    def log_out(self):
        self.current_user = None

    def add(self, *args):

        for video in args:
            if video.title in self.videos.keys():
                print(f'Видео с названием {video.title} уже существует')
            else:
                self.videos[video.title] = [video.duration, video.time_now, video.adult_mode]

    def get_videos(self, name):

        searching_result = []
        for keys in self.videos.keys():
            if name.lower() in keys.lower():
                searching_result.append(keys)
        return searching_result


    def __le__(self,name, other):
        return self.videos[name][2] <= self.current_user[name][1]

    def watch_video(self, name):
        if self.current_user != None:
            if name in self.videos.keys():
                if self.videos[name][2]==True and self.users[self.current_user][1] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(self.videos[name][1], self.videos[name][0]):
                        print(i+1, end = " ")
                        sleep(0.3)
                    print('Конец видео')
            else: pass
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')



class Video():

    '''
    duration - продолжительность, сек
    time_now - секунда остновки
    adult_mode - ограничение по возрасту
    '''

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User():

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

#Добавление видео
ur.add(v1, v2)
#Проверка добавления видео
print(ur.videos)
print('Проверка добавления видео в список')
print('-----------------------')

#Проверка поиска
print('Проверка поиска')
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print('-----------------------')

#Проверка на вход пользователя и возрастное ограничение
print('Проверка на наличие аккаунта')
ur.watch_video('Для чего девушкам парень программист?')
print('Добавление пользователя')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

#Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)