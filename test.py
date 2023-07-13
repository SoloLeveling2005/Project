import time

import win32con
import win32gui
import win32ui
from autoit import properties
from pywinauto import Application


def get_window_titles():
    def callback(hwnd, titles):
        if win32gui.IsWindowVisible(hwnd):
            titles.append(win32gui.GetWindowText(hwnd))

    titles = []
    win32gui.EnumWindows(callback, titles)
    return titles


# Получаем все названия окон
window_titles = get_window_titles()

# Выводим названия окон
for title in window_titles:
    print(title)

# time.sleep(6)
# def example_write_text():
#     window_name = "Project – test.py"
#     # Инициализация объекта Application
#     app = Application()
#
#     # Подключение к существующему окну по его названию
#     window = app.connect(title=window_name).window()
#
#     window.click_input(coords=(50, 50))
#
#
#
# example_write_text()





# time.sleep(7)
# Создание объекта окна
# window = app.window(handle=hwnd)

# Получение координат окна
# window_rect = window.rectangle()

# Вычисление координаты точки внутри окна
# x = window_rect.left + 100  # Замените на фактическую координату x
# y = window_rect.top + 100   # Замените на фактическую координату y

# # Имитация нажатия на указанную координату в окне
# window.click_input(coords=(x, y))


# # Опциональное сворачивание окна обратно в исходное состояние
# autoit.win_set_state(window_title, "@SW_MINIMIZE")
#
# def list_window_names():
#     def winEnumHandler(hwnd, ctx):
#         if win32gui.IsWindowVisible(hwnd):
#             print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
#     win32gui.EnumWindows(winEnumHandler, None)
#
#
# def get_inner_windows(whndl):
#     def callback(hwnd, hwnds):
#         if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#             hwnds[win32gui.GetClassName(hwnd)] = hwnd
#         return True
#     hwnds = {}
#     win32gui.EnumChildWindows(whndl, callback, hwnds)
#     return hwnds
#
# main()


# import cv2
# import numpy as np
# import win32gui
# import win32ui
# import win32con
#
# # Получение хендл окна
# hwnd = win32gui.FindWindow(None, "Albion Online Client")  # Здесь указывается название окна
#
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
# photo = cv2.imread("images/stone/Screenshot_2.png")  # Здесь указывается путь к фото
# # Примените необходимую обработку к фото, например, изменение размера, фильтры и т.д.
#
# # Поиск координат места, совпадающего с фото
# result = cv2.matchTemplate(screenshot, photo, cv2.TM_CCOEFF_NORMED)
# _, max_val, _, max_loc = cv2.minMaxLoc(result)
# if max_val > 0.8:  # Здесь можно настроить порог совпадения
#     x, y = max_loc[0] + photo.shape[1] // 2, max_loc[1] + photo.shape[0] // 2
#     print("Найдены координаты:", x, y)
#     # Имитация нажатия на найденные координаты
#     # simulate_click(hwnd, x, y)
#     # ctypes.windll.user32.PostMessageW(None, 0x201, 0, y << 16 | x)
#
# # Отображение скриншота и фото (для отладки)
# cv2.imshow("Screenshot", screenshot)
# cv2.imshow("Photo", photo)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


fourcc = cv2.