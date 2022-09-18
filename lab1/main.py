import cv2


# Вывод фотографии, лежащей в директории проекта
def print_img():
    img = cv2.imread(r'1.jpg', flags=cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('Display', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Display', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Вывод видео, лежащее в директории проекта
def show_video():
    cap = cv2.VideoCapture(r'1.mp4', cv2.CAP_ANY)   # Создать объект захвата видео
    while True:
        ret, frame = cap.read()                     # вытаскиваеет 1 кадр из cap
        if not (ret):
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(33) & 0xFF == 27:
            break
    cap.release()  # очистка VideoCapture
    cv2.destroyAllWindows()


def write_to_file():
    video = cv2.VideoCapture(r'1.mp4', cv2.CAP_ANY)
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.mov", fourcc, 25, (w, h))
    while True:
        ok, img = video.read()
        cv2.imshow('img', img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    video.release()
    cv2.destroyAllWindows()


# Получение видео с вебки
def print_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()  # очистка VideoCapture
    cv2.destroyAllWindows()


# Получение видео с телефона
# c помощью DroidCam
def phone_video():
    cap = cv2.VideoCapture(1)
    cap.set(5, 640)
    cap.set(7, 480)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()  # очистка VideoCapture
    cv2.destroyAllWindows()


# print_img()
# show_video()
# readIPWriteTOFile()
# print_webcam()
# phone_video()
