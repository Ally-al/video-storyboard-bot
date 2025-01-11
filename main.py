import telebot
from moviepy.editor import *
import cv2
from numpy import double

bot = telebot.TeleBot('your_token')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Вот что я могу:\nstoryboard_video - разделить видео покадрово')

@bot.message_handler(commands=["storyboard_video"])
def start_video_save(message):
    bot.send_message(message.chat.id, 'Отправь мне видео файлом, размер до 20 MB')
    bot.register_next_step_handler(message, video_save)

def video_save(message):
    if not message.document:
        bot.send_message(message.chat.id, 'Ошибка: отправьте видео файлом')
        return

    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("video.mp4", "wb") as f:
        f.write(downloaded_file)

    bot.send_message(message.chat.id, 'Напишите время начала и конца обрабатываемого участка в формате "start end"\nнапример: 0.1 1.5\nвыбирайте отрезок времени до 10 секунд')
    bot.register_next_step_handler(message, cut_video)

def cut_video(message):
    start_time, end_time = message.text.split()

    video = VideoFileClip("video.mp4")

    new_video = video.subclip(double(start_time), double(end_time))
    new_video.write_videofile("trimmed_video.mp4")

    storyboard(message)

def storyboard(message):
    if not os.path.exists("frames"):
        os.makedirs("frames")

    videoCapture = cv2.VideoCapture()
    videoCapture.open("trimmed_video.mp4")
    videoC = cv2.VideoCapture()
    videoC.open("video.mp4")
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

    width = videoC.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = videoC.get(cv2.CAP_PROP_FRAME_HEIGHT)

    for i in range(int(frames)):
        ret, frame = videoCapture.read()

        resized_frame = cv2.resize(frame, (int(width), int(height)))

        cv2.imwrite("frames/%d.jpg" % (i), resized_frame)
        bot.send_document(message.chat.id, open("frames/%d.jpg" % (i), 'rb'))
        os.remove("frames/%d.jpg" % (i))


bot.polling(none_stop=True)
