from tkinter import *
from tkinter.messagebox import *


class Calculator:
    def __init__(self):
        self.frame = Tk()
        self.frame.title("计算")
        showinfo("系统消息", "Hello world")
        # self.frame.input("请输入元的半径")

    def show(self):
        self.frame.mainloop()


if __name__ == "__main__":
    this_gui = Calculator()
    this_gui.show()
