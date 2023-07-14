import time

import cv2
import numpy as np
import mss
import mss.tools
import pyautogui

# # Создание объекта MSS для захвата экрана
# with mss.mss() as sct:
#     # Определение области для захвата экрана (здесь захватывается весь экран)
#     monitor = sct.monitors[1]  # Если у тебя один монитор, используй sct.monitors[0]
#     capture_area = (monitor['left'], monitor['top'], monitor['width'], monitor['height'])
#
#     while True:
#         # Захват текущего кадра из видеопамяти
#         frame = np.array(sct.grab(capture_area))
#
#         # Преобразование цветовой схемы из BGR в RGB
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         for i in range(2, 6):
#
#             # Загрузка изображения объекта, который мы хотим обнаружить
#             object_image = cv2.imread(
#                 'images/stone/Screenshot_'+str(i)+'.png')  # Замени 'object.png' на путь к изображению объекта
#
#             # Поиск объекта на текущем кадре
#             result = cv2.matchTemplate(frame_rgb, object_image, cv2.TM_CCOEFF_NORMED)
#             _, max_val, _, max_loc = cv2.minMaxLoc(result)
#
#             # Установка порога для обнаружения объекта
#             threshold = 0.45
#
#             # Если найденное совпадение превышает порог, считаем, что объект обнаружен
#             print(i, max_val)
#             if max_val >= threshold:
#                 # Получение координат верхнего левого угла и размеров объекта
#                 top_left = max_loc
#                 height, width, _ = object_image.shape
#
#                 # Вывод сообщения в консоль
#                 print(f"Объект обнаружен: координаты ({top_left[0]}, {top_left[1]}), ширина {width}, высота {height}")
#
#             # Отображение текущего кадра на экране
#             # cv2.imshow('Screen', frame_rgb)
#
#             # Прерывание цикла, если нажата клавиша 'q'
#             if cv2.waitKey(1) == ord('q'):
#                 break
#
# # Закрытие всех окон после выхода из цикла
# cv2.destroyAllWindows()
#
import cv2
import numpy as np
import pyautogui
import time
import threading

path = "images/stone/Screenshot_"

# Загрузка изображений
images = []
for i in range(2, 13):
    image_path = path + str(i) + ".png"
    image = cv2.imread(image_path)
    images.append(image)

while True:
    found = False
    # Предварительное выполнение цветового преобразования для скриншота
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

    # Общий массив для хранения успешных результатов
    finds_object = []


    def find_stone(image):
        # Применение шаблонного сопоставления
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)

        # Нахождение положения максимального значения
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Определение порогового значения
        threshold = 0.65

        if max_val >= threshold:

            # Извлечение координат максимального значения
            x, y = max_loc

            # Центр найденного изображения
            center_x = x + image.shape[1] // 2
            center_y = y + image.shape[0] // 2

            if [center_x, center_y] not in finds_object:
                finds_object.append([center_x, center_y])


    # Создание и запуск потоков
    threads = []
    for i, image in enumerate(images):  # Пример: запуск 5 потоков
        thread = threading.Thread(target=find_stone, args=(image,))
        thread.start()
        threads.append(thread)

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()


    if len(finds_object) > 1:
        pyautogui.click(finds_object[0][0], finds_object[0][1])


    # Задержка между итерациями (если необходимо)
    time.sleep(1)
