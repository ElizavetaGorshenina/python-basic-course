import tkinter
from _tkinter import TclError
import time
import sys


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        light_box = tkinter.Tk()
        light_box.title('Светофор')
        light_box.geometry('230x560')
        light_box.resizable(False, False)
        canvas = tkinter.Canvas()
        canvas.create_rectangle(1, 1, 229, 559, fill="#808080")
        canvas.create_oval([40, 40], [190, 190], outline="#C0C0C0", width=3)
        canvas.create_oval([40, 205], [190, 355], outline="#C0C0C0", width=3)
        canvas.create_oval([40, 370], [190, 520], outline="#C0C0C0", width=3)
        canvas.pack(fill=tkinter.BOTH, expand=1)
        if self.__color in ['желтый', 'жёлтый', 'Жёлтый', 'Желтый', 'yellow', 'Yellow']:
            canvas.create_oval([40, 205], [190, 355], outline="#C0C0C0", fill="#FFFF00", width=3)
            light_box.update()
            time.sleep(2)
            self.__color = 'зеленый'
        if self.__color in ['зеленый', 'зелёный', 'Зеленый', 'Зелёный', 'green', 'Green']:
            try:
                canvas.create_oval([40, 205], [190, 355], outline="#C0C0C0", fill="#808080", width=3)
                canvas.create_oval([40, 370], [190, 520], outline="#C0C0C0", fill="#008000", width=3)
                light_box.update()
                time.sleep(5)
                self.__color = 'красный'
            except TclError:
                print("\033[31m{}".format('Работа светофора остановлена'))
                sys.exit(0)
        if self.__color in ['красный', 'Красный', 'red', 'Red']:
            while True:
                try:
                    canvas.create_oval([40, 40], [190, 190], outline="#C0C0C0", fill="#FF0000", width=3)
                    canvas.create_oval([40, 370], [190, 520], outline="#C0C0C0", fill="#808080", width=3)
                    light_box.update()
                    time.sleep(7)
                    self.__color = 'желтый'
                    canvas.create_oval([40, 40], [190, 190], outline="#C0C0C0", fill="#808080", width=3)
                    canvas.create_oval([40, 205], [190, 355], outline="#C0C0C0", fill="#FFFF00", width=3)
                    light_box.update()
                    time.sleep(2)
                    self.__color = 'зеленый'
                    canvas.create_oval([40, 205], [190, 355], outline="#C0C0C0", fill="#808080", width=3)
                    canvas.create_oval([40, 370], [190, 520], outline="#C0C0C0", fill="#008000", width=3)
                    light_box.update()
                    time.sleep(5)
                    self.__color = 'красный'
                except TclError:
                    print("\033[31m{}".format('Работа светофора остановлена'))
                    sys.exit(0)
        else:
            print('Неверно задан цвет')


stop_light = TrafficLight('желтый')
stop_light.running()
