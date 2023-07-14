# import win32gui
#
# def get_window_titles():
#     def callback(hwnd, titles):
#         if win32gui.IsWindowVisible(hwnd):
#             titles.append(win32gui.GetWindowText(hwnd))
#
#     titles = []
#     win32gui.EnumWindows(callback, titles)
#     return titles
#
# # Получаем все названия окон
# window_titles = get_window_titles()
#
# # Выводим названия окон
# for title in window_titles:
#     print(title)
import cv2
import numpy as np
# import win32gui
# import win32api
# import win32con

# def handle_window(hwnd, extra):
#     if win32gui.GetWindowText(hwnd) == "Albion Online Client":  # Замените "Название окна" на фактическое название окна
#         win32gui.SetForegroundWindow(hwnd)

#         while True:

#             def handle_message(hwnd, msg, wparam, lparam):
#                 if msg == win32con.WM_LBUTTONDOWN:
#                     x = win32api.LOWORD(lparam)
#                     y = win32api.HIWORD(lparam)
#                     print(f"Координаты клика: X={x}, Y={y}")

#             win32gui.SetWindowLong(hwnd, win32con.GWL_WNDPROC, handle_message)
#             win32gui.PumpMessages()


# # Запускаем цикл перечисления окон и обработки событий
# while True:
#     win32gui.EnumWindows(handle_window, None)





# from pynput import mouse
# import win32gui

# def on_click(x, y, button, pressed):
#     if pressed:
#         active_window = win32gui.GetForegroundWindow()
#         window_title = win32gui.GetWindowText(active_window)

#         if window_title == "Albion Online Client":  # Замените "Albion Online Client" на фактическое название окна
#             print(f"Координаты клика: X={x}, Y={y}")

# # Создаем экземпляр слушателя кликов мыши
# listener = mouse.Listener(on_click=on_click)

# # Запускаем слушателя в отдельном потоке
# listener.start()

# # Запускаем основной цикл
# while True:
#     pass











import pyautogui
import time 
time.sleep(2)
path = "images/stone/Screenshot_"
# time.sleep(3)
while True:
    time.sleep(1)
    buttons = []
    for i in range(2,6):
        # Получение снимка экрана
        # Загрузка скриншота экрана
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)  # Преобразование в массив NumPy
        screenshot = cv2.cvtColor(screenshot,
                                  cv2.COLOR_RGB2BGR)  # Преобразование цветового пространства в BGR (для cv2)

        # Загрузка изображения, которое нужно найти
        image_path = path+str(i)+".png"
        image = cv2.imread(image_path)

        # Применение шаблонного сопоставления
        result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)

        # Нахождение положения максимального значения
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Определение порогового значения
        threshold = 0.8 * max_val  # Примерный порог: 80% от максимального значения сопоставления

        if max_val > threshold:  # Проверка порогового значения
            # Извлечение координат максимального значения
            x, y = max_loc

            # Центр найденного изображения
            center_x = x + image.shape[1] // 2
            center_y = y + image.shape[0] // 2

            # Производим сбор

            time.sleep(6)
            break

        else:
            print('Изображение не найдено на экране')
