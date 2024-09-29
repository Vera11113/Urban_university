def checking_email(recepient, sender):

    domains = ['.net', '.com', '.ru']

    if ('@' in recepient) and ('@' in sender):
        if any((val in recepient) for val in domains) and any((val in sender) for val in domains):
            return True
        else: return False

    else: return False

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if checking_email(recipient, sender) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else: print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки', recipient='vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', recipient= 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


