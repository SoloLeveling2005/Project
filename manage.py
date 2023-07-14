import time
import ctypes
from keyboard_keys import KEYBOARD
import cv2
import numpy as np
import win32api
import win32ui, win32gui, win32con
from PIL import Image
import cv2
import numpy as np
import pyautogui
import ctypes
from pywinauto import Application, findwindows
import pywinauto.keyboard as keyboard


# time.sleep(2)


# Получение хендл окна по названию.
def get_hwnd(window_title: str) -> str:
    """
    Получение хендл окна по названию.
    """

    # Инициализация объекта Application
    app = Application().connect(title=window_title)

    # Получение дескриптора окна
    hwnd = findwindows.find_windows(title=window_title)[0]
    print(hwnd)
    return hwnd


# Записываем.
hwnd = get_hwnd("Albion Online Client")


# Функция для имитации нажатия на определенные координаты (x, y) в указанном окне
def simulate_click(hwnd, x, y):
    """
    Пример использования:
    x = 500
    y = 770
    simulate_click(hwnd, x, y)
    """

    print('click')

    # Константы и структуры из Windows API
    WM_LBUTTONDOWN = 0x0201
    WM_LBUTTONUP = 0x0202
    l_param = win32api.MAKELONG(x, y)
    # x = 212
    # y = 66
    win32gui.PostMessage(hwnd, win32con.BM_CLICK, 0, l_param)
    # win32gui.PostMessage(hwnd, win32con.BM_CLICK, 0, l_param)


# Функция для имитации нажатия клавиши клавиатуры
def simulate_key_press(key_code):
    """
    Имитация нажатия клавиши по key_code.
    """
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key_code, 0)


# Функция для имитации ввода текста.
def simulate_text_input(key_code):
    """
    Имитация ввода текста.
    """
    win32api.SendMessage(hwnd, win32con.WM_CHAR, key_code, 0)


# left, top, right, bot = win32gui.GetWindowRect(hwnd)
# w = right - left
# h = bot - top
#
# hwndDC = win32gui.GetWindowDC(hwnd)
# mfcDC = win32ui.CreateDCFromHandle(hwndDC)
# saveDC = mfcDC.CreateCompatibleDC()
#
# saveBitMap = win32ui.CreateBitmap()
# saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
#
# saveDC.SelectObject(saveBitMap)
#
# result = ctypes.windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
# print(result)
#
# bmpinfo = saveBitMap.GetInfo()
# bmpstr = saveBitMap.GetBitmapBits(True)
#
# im = Image.frombuffer(
#     'RGB',
#     (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
#     bmpstr, 'raw', 'BGRX', 0, 1)
#
# win32gui.DeleteObject(saveBitMap.GetHandle())
# saveDC.DeleteDC()
# mfcDC.DeleteDC()
# win32gui.ReleaseDC(hwnd, hwndDC)
#
# if result == 1:
#     #PrintWindow Succeeded
#     im.save("test.png")

# # Получение размеров окна
# window_rect = win32gui.GetWindowRect(hwnd)
# window_width = window_rect[2] - window_rect[0]
# window_height = window_rect[3] - window_rect[1]
#
# # Получение контекста устройства окна
# window_dc = win32gui.GetWindowDC(hwnd)
# window_dc_obj = win32ui.CreateDCFromHandle(window_dc)
#
# # Создание контекста памяти для сохранения изображения
# mem_dc = window_dc_obj.CreateCompatibleDC()
# bitmap = win32ui.CreateBitmap()
# bitmap.CreateCompatibleBitmap(window_dc_obj, window_width, window_height)
# mem_dc.SelectObject(bitmap)
#
# # Копирование содержимого окна в контекст памяти
# mem_dc.BitBlt((0, 0), (window_width, window_height), window_dc_obj, (0, 0), win32con.SRCCOPY)
#
# # Извлечение данных из контекста памяти в массив numpy
# bmp_info = bitmap.GetInfo()
# image = np.frombuffer(bitmap.GetBitmapBits(True), dtype=np.uint8)
# image = image.reshape((window_height, window_width, 4))
#
# # Освобождение ресурсов
# win32gui.DeleteObject(bitmap.GetHandle())
# mem_dc.DeleteDC()
# window_dc_obj.DeleteDC()
# win32gui.ReleaseDC(hwnd, window_dc)
#
# # Преобразование изображения из формата BGRA в BGR
# image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
#
# # Обработка изображения с помощью OpenCV
# # Ваш код для обработки изображения
#
# # Отображение обработанного изображения
# cv2.imshow("Processed Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# def invisible(window_name):
#     """Функция работает только в ОС Windows. Возвращает скриншот окна в виде массива PIL Image."""
#     hwnd = win32gui.FindWindow(None, window_name)
#     f = ctypes.windll.dwmapi.DwmGetWindowAttribute
#     rect = ctypes.wintypes.RECT()
#     dwma_extended_frame_bounds = 9
#     f(ctypes.wintypes.HWND(hwnd),
#       ctypes.wintypes.DWORD(dwma_extended_frame_bounds),
#       ctypes.byref(rect),
#       ctypes.sizeof(rect)
#       )
#     width = rect.right - rect.left  # noqa
#     height = rect.bottom - rect.top  # noqa
#     hwnddc = win32gui.GetWindowDC(hwnd)
#     mfcdc = win32ui.CreateDCFromHandle(hwnddc)
#     savedc = mfcdc.CreateCompatibleDC()
#     savebitmap = win32ui.CreateBitmap()
#     savebitmap.CreateCompatibleBitmap(mfcdc, width, height)
#     savedc.SelectObject(savebitmap)
#     ctypes.windll.user32.PrintWindow(hwnd, savedc.GetSafeHdc(), 1)
#     bmpinfo = savebitmap.GetInfo()
#     bmpstr = savebitmap.GetBitmapBits(True)
#     im_scr = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
#     win32gui.DeleteObject(savebitmap.GetHandle())
#     savedc.DeleteDC()
#     mfcdc.DeleteDC()
#     win32gui.ReleaseDC(hwnd, hwnddc)
#     return im_scr
#
# invisible("Albion Online Client").show()

# # Получение размеров окна
# window_rect = win32gui.GetWindowRect(hwnd)
# window_width = window_rect[2] - window_rect[0]
# window_height = window_rect[3] - window_rect[1]
#
# # Получение контекста устройства окна
# window_dc = win32gui.GetWindowDC(hwnd)
# window_dc_obj = win32ui.CreateDCFromHandle(window_dc)
#
# # Создание контекста памяти для сохранения изображения
# mem_dc = window_dc_obj.CreateCompatibleDC()
# bitmap = win32ui.CreateBitmap()
# bitmap.CreateCompatibleBitmap(window_dc_obj, window_width, window_height)
# mem_dc.SelectObject(bitmap)
#
# # Копирование содержимого окна в контекст памяти
# mem_dc.BitBlt((0, 0), (window_width, window_height), window_dc_obj, (0, 0), win32con.SRCCOPY)
#
# # Извлечение данных из контекста памяти в массив numpy
# bmp_info = bitmap.GetInfo()
# screenshot = np.frombuffer(bitmap.GetBitmapBits(True), dtype=np.uint8)
# screenshot = screenshot.reshape((window_height, window_width, 4))
#
# # Освобождение ресурсов
# win32gui.DeleteObject(bitmap.GetHandle())
# mem_dc.DeleteDC()
# window_dc_obj.DeleteDC()
# win32gui.ReleaseDC(hwnd, window_dc)
#
# # Преобразование изображения из формата BGRA в BGR
# screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
#
# # Загрузка и обработка фото
# photo = cv2.imread("images/stone/Screenshot_2.png")  # Здесь нужно указать путь к фото
# # Примените необходимую обработку к фото, например, изменение размера, фильтры и т.д.
#
# # Поиск координат места, совпадающего с фото
# result = cv2.matchTemplate(screenshot, photo, cv2.TM_CCOEFF_NORMED)
# _, max_val, _, max_loc = cv2.minMaxLoc(result)
# if max_val > 0.8:  # Здесь можно настроить порог совпадения
#     x, y = max_loc[0] + photo.shape[1] // 2, max_loc[1] + photo.shape[0] // 2
#     print("Найдены координаты:", x, y)
#     # Имитация нажатия на найденные координаты
#     simulate_click(hwnd, x, y)
#     # ctypes.windll.user32.PostMessageW(None, 0x201, 0, y << 16 | x)
#
# # Отображение снимка экрана и фото (для отладки)
# cv2.imshow("Screenshot", screenshot)
# cv2.imshow("Photo", photo)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# def find_objects(query_image_paths, target_image_path):
#     # Загрузка изображений
#     target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)
#
#     # Инициализация детектора SURF
#     surf = cv2.xfeatures2d.SURF_create()
#
#     # Обнаружение особенностей на целевом изображении
#     keypoints_target, descriptors_target = surf.detectAndCompute(target_image, None)
#
#     # Создание объекта BFMatcher для сопоставления особенностей
#     bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
#
#     for query_image_path in query_image_paths:
#         # Загрузка запросов изображений
#         query_image = cv2.imread(query_image_path, cv2.IMREAD_GRAYSCALE)
#
#         # Обнаружение особенностей на запросов изображениях
#         keypoints_query, descriptors_query = surf.detectAndCompute(query_image, None)
#
#         # Сопоставление особенностей между изображениями
#         matches = bf.match(descriptors_query, descriptors_target)
#
#         # Сортировка сопоставлений по расстоянию
#         matches = sorted(matches, key=lambda x: x.distance)
#
#         # Удаление повторяющихся координат
#         filtered_matches = [matches[0]]  # Первое сопоставление всегда добавляем
#         for i in range(1, len(matches)):
#             current_match = matches[i]
#             previous_match = matches[i - 1]
#             if current_match.distance != previous_match.distance:
#                 filtered_matches.append(current_match)
#
#         # Отображение сопоставлений на изображении
#         matched_image = cv2.drawMatches(query_image, keypoints_query, target_image, keypoints_target, filtered_matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
#
#         # Отображение результатов
#         cv2.imshow("Matches", matched_image)
#         cv2.waitKey(0)
#
#     cv2.destroyAllWindows()
#
# # Пример использования
# query_image_paths = ["Screenshot_2.png", "query_image2.jpg", "query_image3.jpg"]  # Пути к изображениям объектов для поиска
# target_image_path = "target_image.jpg"  # Путь к изображению, на котором выполняется поиск
# find_objects(query_image_paths, target_image_path)

import pyautogui
import time

time.sleep(2)
path = "images/stone/Screenshot_"
# time.sleep(3)
while True:
    time.sleep(1)
    buttons = []
    for i in range(2, 6):
        # Получение снимка экрана
        # Загрузка скриншота экрана
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)  # Преобразование в массив NumPy
        screenshot = cv2.cvtColor(screenshot,
                                  cv2.COLOR_RGB2BGR)  # Преобразование цветового пространства в BGR (для cv2)

        # Загрузка изображения, которое нужно найти
        image_path = path + str(i) + ".png"
        image = cv2.imread(image_path)

        # Применение шаблонного сопоставления
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)

        # Нахождение положения максимального значения
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Определение порогового значения
        threshold = 0.65 * max_val  # Примерный порог: 80% от максимального значения сопоставления

        if max_val > threshold:  # Проверка порогового значения
            # Извлечение координат максимального значения
            x, y = max_loc

            # Центр найденного изображения
            center_x = x + image.shape[1] // 2
            center_y = y + image.shape[0] // 2

            # Производим сбор
            print("Есть контакт")
            print(hwnd, x, y)
            simulate_click(hwnd=hwnd, x=x, y=y)
            time.sleep(3)
            break

        else:
            print('Изображение не найдено на экране')
