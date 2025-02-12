import tkinter as tk
from tkinter import messagebox


def show_answer():
    if var.get() == 1:
        messagebox.showinfo("回应", "知道你是傻逼了！")
        root.destroy()
    else:
        messagebox.showerror("错误", "这都不敢承认吗")


def on_close():
    messagebox.showinfo("提示", "再给你一次机会")


root = tk.Tk()
root.title("恶搞")
# 设置窗口大小为宽 150 像素，高 125 像素
root.geometry("150x125")

var = tk.IntVar()
tk.Label(root, text="你是傻逼吗", font=("宋体", 10)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Radiobutton(frame, text="是的", variable=var, value=1, font=("宋体", 8)).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(frame, text="不是", variable=var, value=2, font=("宋体", 8)).pack(side=tk.LEFT, padx=5)

tk.Button(root, text="确定", command=show_answer, font=("宋体", 10)).pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()