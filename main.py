# import win32gui

# def get_window_titles():
#     def callback(hwnd, titles):
#         if win32gui.IsWindowVisible(hwnd):
#             titles.append(win32gui.GetWindowText(hwnd))

#     titles = []
#     win32gui.EnumWindows(callback, titles)
#     return titles

# # Получаем все названия окон
# window_titles = get_window_titles()

# # Выводим названия окон
# for title in window_titles:
#     print(title)


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



# Координаты клика: X=384, Y=657




from pywinauto import Desktop, Application
from pywinauto.mouse import click
import time
import win32gui
import win32api
import win32con
# time.sleep(8)
# app = Application().connect(title='Albion Online Client')  # Замени 'Название окна' на актуальное название скрытого окна
# window = app['Albion Online Client']  # Замени 'Название окна' на актуальное название скрытого окна

hWnd = win32gui.FindWindow("Albion Online Client", None)
x = 384  # Координата X
y = 657  # Координата Y
# Переводим окно в фокус
# win32gui.SetForegroundWindow(hWnd)
# Получаем экранные координаты окна
# window_left, window_top, window_right, window_bottom = win32gui.GetWindowRect(hWnd)

# Вычисляем относительные координаты
click_x =  x
click_y =  y

# Нажимаем левую кнопку мыши на указанных координатах
win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click_y << 16 | click_x)
win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, 0, click_y << 16 | click_x)
# click(coords=(x, y))
