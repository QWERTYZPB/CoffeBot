




START_USER_TEXT = '''
<b>Приветственное сообщение пользователь!</b>

'''


START_BARISTA_TEXT = '''
<b>Приветственное сообщение бариста!</b>

'''


START_ADMIN_TEXT = '''
<b>Приветственное сообщение админ!</b>

'''




REFERRAL_SYSTEM_TEXT = '''
<b><i>Реферальная система «Стакан за друга»</i></b>

Пригласи человека и получи <b>стакан</b> на свой счет,
как только он купит Бабл ти и покажет свой QR-код!

Твоя реферальная ссылка:
    <code>{referral_link}</code>
'''


USER_PROFILE_TEXT = '''
👑 {name} {username}

☕️ Стаканов: <b>{cups}</b>
🎁 Осталось до бесплатного Бабл ти: <b>{cups_remain}</b>
🤝 Рефералов: <b>{referrals}</b>


'''

BARISTA_PROFILE_TEXT = '''
👑 {name} {username}

Ура! Вы бариста в этой MENS bubble tea!
'''



RULES_TEXT = '''
<b><i>Система лояльности MENS</i></b>

Приходи к нам, при покупке Бабл ти покажи QR-код нашему сотруднику и получай бонусный стакан. 

Накопи 9 стаканов и получи свой любимый <b>Бабл ти бесплатно!</b>

'''



MANY_CUPS_TEXT = '''
У пользователя <b>{name}</b> 

{cups} стаканов!

Выберите действие:
'''


ADD_A_CUP_TEXT = '''
Подтвердите начисление <b>одного стакана</b> для пользователя <b>{name}</b>

Кол-во стаканов: <b>{cups}</b>
'''





SUCCESS_ADD_A_CUP_TEXT='''
Пользователю успешно начислен

<b>+1 стакан</b>!

Кол-во стаканов теперь: <b>{cups}</b>
'''


SUCCESS_ADD_A_CUP_USER_TEXT='''
Вам успешно начислен

<b>+1 стакан</b>!

Кол-во ваших стаканов теперь: <b>{cups}</b>
Осталось стаканов до бесплатного Бабл ти: <b>{cups_remain}</b>

<span class="tg-spoiler">P.s. Собери 9 стаканов и получи десятый Бабл ти в подарок! 🎁</span>
'''


ALREADY_10_CUPS_USER_TEXT = '''
Поздравляем у вас достаточно стаканов, чтобы получить <b>БЕСПЛАТНЫЙ</b> Бабл ти! 

Кол-во ваших стаканов <b>{cups}</b>

Покажите ваш QR-код баристе для получения бесплатного Бабл ти!
'''




SUCCESS_DEDUCT_A_CUP_TEXT='''
Пользователю успешно списано 

<b>-9 стаканов</b>!

Кол-во стаканов теперь: <b>{cups}</b>
'''

SUCCESS_DEDUCT_A_CUP_USER_TEXT='''
С вас списаны стаканы за бесплатный Бабл ти! 

<b>-9 стаканов</b>

Кол-во стаканов теперь: <b>{cups}</b>
'''



NOT_BARISTA_TEXT = '''
Вы <b>не являетесь</b> баристой, если это не так - свяжитесь с поддержкой:

@{support}
'''


NO_SUCH_USER_TEXT = '''
Данного пользователя нет в боте!\nПользователь должен <b>обязательно</b> нажать на кнопку "START"
'''

WRONG_QR_TEXT = '''
Не правильный QR-код!
'''


CANT_INVITE_YOURSELF_TEXT = '''
Ты не можешь пригласить сам себя!
'''

ALREADY_REF_TEXT = '''
Вы уже были приглашены в реферальную программу пользователем <b>{name}</b>!
'''


REFERRER_TEXT = '''
Вы получите +1 стакан за приглашенного пользователя <b>{name}</b>, когда он(-а) купит Бабл ти!
'''

REFERRER_SUCCESS_TEXT = '''
Вы получили +1 стакан за приглашенного пользователя <b>{name}</b>, он(-а) только что купил(-а) Бабл ти!

Теперь у вас {cups} стаканов!
'''


REFERRAL_TEXT = '''
Вы были приглашенны пользователем <b>{name}</b>!

<span class="tg-spoiler">P.s. Приглашайте людей и получайте стаканы, после покупки Бабл ти!</span>

''' + START_USER_TEXT




CANCEL_A_CUP_TEXT = '''
Пользователю {name} отменено зачисление напитка в системе лояльности.
Количество напитков: {cups}'''
