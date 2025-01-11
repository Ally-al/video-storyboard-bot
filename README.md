# video-storyboard-bot
Telegram бот для раскадровки видео. 
Позволяет пользователям отправлять видео, обрезать его по заданному времени и получать покадровую нарезку.

## Описание команд телеграм-бота:

- Команда **start** – запуск бота, приветственное сообщение.
- Команда **storyboard_video** – разделение заданного промежутка времени видео на кадры.

## Как использовать:

(для работы бота вставьте в код вместо 'your_token' свой токен бота, полученный в BotFather в Telegram, и запустите код)

- Отправьте команду /storyboard_video, чтобы начать обработку видео.
- Отправьте видео (до 20 MB) в чат с ботом.
- Укажите время начала и конца обрабатываемого участка видео в формате "start end", например: 0.1 1.5.
- Выбирайте отрезок до 10 секунд
- Получите покадровую нарезку видео, каждый кадр будет отправлен как изображение в формате jpg.

## Основные технологии:

- Telegram Bot API (python-telebot): Библиотека для создания и управления ботами в Telegram. Используется для общения с пользователем и обработки команд.
- MoviePy: Библиотека для работы с видео в Python. Используется для обрезки видео по указанным временным промежуткам.
- OpenCV (cv2): Библиотека для обработки изображений и видео. В проекте используется для извлечения кадров из видео и сохранения их в виде изображений.
