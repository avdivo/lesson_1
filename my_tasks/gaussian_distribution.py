from tkinter import Tk, Canvas, Frame, BOTH
from random import randint

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Рисуем линии")
        self.pack(fill=BOTH, expand=1)

        point = [0] * 300
        for i in range(3000):
            cou = 0
            for j in range(len(point)-1):
                cou += randint(0, 1)
            point[cou] += 1






        canvas = Canvas(self)


        for j in range(len(point)):
            canvas.create_oval(50+j, 300-point[j], 50+j, 300-point[j], width=2, fill='white')
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("400x300+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()