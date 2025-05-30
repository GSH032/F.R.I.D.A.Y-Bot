import telebot
from telebot import types

TOKEN = "7068411440:AAHlYRU9lYYqP3zC5catjpACKcH-UbosB7o"#Токен

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start']) #Старт бота
def start(message):
	bot.send_message(message.chat.id, '<b>Привет {0.first_name}!</b> Я бот созданый командой CyberStalkers! '
									  'Напиши /help для получения информации а данном Чат-Боте'
									  '\n<b>{0.first_name}</b>!'
					 				.format(message.from_user, bot.get_me()), parse_mode='HTML')
	photos = bot.get_user_profile_photos(message.chat.id)
	bot.send_photo(message.chat.id , photos.photos[0][0].file_id) #Получение имени и аватара пользователя
	reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn_hello = types.KeyboardButton('Привет')
	btn_2 = types.KeyboardButton('Что ты умеешь?')
	reply.add(btn_hello,btn_2)
	bot.send_message(message.chat.id,"Чем я могу вам помочь?", reply_markup=reply)


@bot.message_handler(commands=['creators'])
def creators(message):
    bot.send_message(message.chat.id,
                     'Бот создан командой CyberStalkers! Шляковым Георгием, Царой Даниилом и Дзвонитским Дмитрием')


@bot.message_handler(commands=['aboutcard'])
def aboucard(message):
	Hi = open('Card.png', 'rb')
	bot.send_photo(message.chat.id,  Hi, 'Универса́льная электро́нная ка́рта (УЭК) — это российская пластиковая карта, объединяющая в себе идентификационное и платёжное средство, также это ключ доступа к широкому спектру электронных услуг и сервисов – государственных, муниципальных и коммерческих.'
						   '\nС помощью карты УЭК можно будет получить государственные, региональные и коммерческие услуги в электронном виде с использованием банкоматов, инфокиосков, персональных компьютеров, мобильных устройств.'
							   '\n Карта УЭК также будет приниматься в метро, автобусах, троллейбусах и трамваях. Подобно обычной банковской карте картой УЭК можно будет пользоваться для оплаты товаров и услуг в магазинах и любых других организациях')
	bot.send_message(message.chat.id,
					 '\n Возможности применения карты:'
					 '\n• Идентификационное приложение — позволяет идентифицировать себя для получения государственных, муниципальных и коммерческих услуг, в том числе в медицинских учреждениях и в пенсионной системе.'
					 '\n• Электронная подпись — позволяет подписывать электронные документы он-лайн усиленной квалифицированной электронной подписью при совершении юридически значимых действий в электронном виде. Электронная подпись позволяет создавать между пользователем и поставщиками услуг защищенное соединение, которое в отличие от обычных логина и пароля обеспечивает защиту передаваемой информации от перехвата, прочтения и подмены.'
					 '\n• Платёжное приложение — позволяет осуществлять обычные банковские операции с расчётным счетом: оплата товаров и услуг, оплата государственных услуг, снятие денежных средств, перевод денежных средств и т. п. Держатель карты УЭК может совершать оплату дистанционно через Интернет, а также в более 100 000 торговых и сервисных предприятиях в России, которые обслуживаются банками, входящими в российскую платежную систему ПРО100. Для активации банковского приложения необходимо посетить выбранный банк, чтобы открыть расчётный счет. Комиссия за использование расчётного счета не взимается.'
					 '\n• Держатель карты имеет возможность просматривать записанные на карту идентификационные данные (фамилия, имя, отчество, дата рождения и т. п.) и редактировать свои данные, предназначенные для заполнения различных электронных документов: почтовый адрес, номер телефона, адрес электронной почты. Наличие этих данных на карте УЭК позволяет мгновенно заполнять заявления при обращении в многофункциональный центр или при подаче заявлений через Интернет.')
	about = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
	btn_hello = types.KeyboardButton('Больше о карте')
	btn_2 = types.KeyboardButton('Расписание')
	btn3 = types.KeyboardButton('Пока')
	btn4 = types.KeyboardButton('О Создателях')
	btn5 = types.KeyboardButton('Получить карту')
	about.add(btn_hello, btn_2, btn3, btn4,btn5)
	bot.send_message(message.chat.id, "Что-то еще?", reply_markup=about)


@bot.message_handler(commands=['help']) # Помощь
def help(message):
   bot.send_message(message.chat.id, 'Я поддерживаю такие команды '
									 '\n /start- Перезапуск бота '
									 '\n /help - Помощь'
									 '\n /creators - О создаете'
									 '\n /aboutcard - О карте')

@bot.message_handler(content_types=['text']) # Реакция на слова и обработка сообщений
def echo1234(message):

	if message.text.__contains__('Привет'):
		bot.send_message(message.chat.id,'Привет!')
	elif message.text.__contains__('Пока'):
		bot.send_message(message.chat.id,'Пока!')
	elif message.text.__contains__('Что ты умеешь?'):
		bot.send_message(message.chat.id,'Я могу предоставлять информацию о "Универсальной электронной карты жителя Московской области"')


	elif 	message.text.__contains__('Больше о карте'):
		bot.send_message(message.chat.id,'Внедрение универсальных электронных карт призвано повысить качество, скорость и прозрачность взаимодействия граждан с государственными органами власти и учреждениями при запросе информации и получении услуг.Универсальная электронная карта действует на всей территории России, гарантируя единые стандарты обслуживания и безопасности карт каждому гражданину вне зависимости от региона проживания.'
										 '\n<b>1.Основными приложениями карты являются:</b> '
										 '\n<b>2.Федеральное электронное идентификационное приложение;</b> '
										 '\n<b>3.Электронное банковское приложение.</b>'
										 '\n<b>4.Федеральное электронное идентификационное приложение содержит область персональных данных (Ф.И.О., пол и дата рождения держателя карты, срок действия карты), области данных внебюджетных фондов Российской Федерации (страховой номер индивидуального лицевого счета в системе обязательного пенсионного страхования (СНИЛС) и номер полиса обязательного медицинского страхования (ОМС)). Идентификационное приложение формирует усиленную квалифицированную электронную подпись (ЭП). ЭП дает возможность получать государственные услуги, муниципальные и коммерческие услуги, требующие юридически значимой и достоверной идентификации и аутентификации гражданина, а также заверять данные гражданина.</b>'
										 '\n<b>5.Электронное банковское приложение карты обслуживают крупнейшие российские банки, чья деятельность отвечает установленным требованиям к работе с персональными данными и информационной безопасности. Электронное банковское приложение содержит данные, необходимые для осуществления банковских операций в платежной системе ПРО100.</b>' ,parse_mode='HTML')

	elif message.text.__contains__('Расписание'):
		inlinekey = types.InlineKeyboardMarkup(row_width=1)  #Кнопка для ссылок
		btn1 = types.InlineKeyboardButton('Расписание', url='https://rasp.yandex.ru/')
		inlinekey.add(btn1)
		bot.send_message(message.chat.id, 'Вот', reply_markup=inlinekey)

	elif message.text.__contains__('Получить карту'):
			bot.send_message(message.chat.id,'<b>!ВНИАМНИЕ!:</b>'
											 '\n<b>Прошу учесть что Выдача карт прекращены с 1 января 2017 года.</b> '
											 '\n<b>Приём заявлений на выпуск УЭК, в том числе на выпуск дубликатов, прекращен во всех субъектах Российской Федерации.</b>', parse_mode='HTML')
			file = open('Card.docx', 'rb') #Открытие файла и его чтение
			bot.send_message(message.chat.id, 'Но у нас остался файл с инструкциями'
											  '\n Вот он')
			bot.send_document(message.chat.id, file)

	elif message.text.__contains__('Что ты умеешь?'):
		bot.send_message(message.chat.id,'Я могу предоставлять информацию о "Универсальной электронной карты жителя Московской области"')

	elif message.text.__contains__('О Создателях'):
			bot.send_message(message.chat.id,
							 'По вопросам с ботом писать:'
							 '\ntsaradaniil2006@gmail.com'
							'\ndzvoniskiydm_ot@mail.ru'
							'\nshlyakovga_ot@mail.ru')

	else:
		bot.reply_to(message, f'Вы уверены что имели ввиду "<b>{message.text}</b>"?'
							  '\nКажется в моем арсенале нет такой команды...', parse_mode='HTML')


bot.polling(none_stop=True)