import tkinter as tk
from tkinter import messagebox
from login import login
from testnet import test_network

def show_message(title, message):
    messagebox.showinfo(title, message)

def show_error(title, message):
    messagebox.showerror(title, message)

def start_gui():
    root = tk.Tk()
    root.title("登录界面")
    root.geometry("300x150")

    def on_login():
        response_data, wlanuserip = login()
        if response_data:
            if response_data['code'] == '0':
                show_message("成功", f"登录成功 局域网ip: {wlanuserip}")
                test_network()              # 测试网络
            else:
                show_error("失败", f"登录失败，错误信息: {response_data['message']}")
        else:
            show_error("请求失败", wlanuserip)

    login_button = tk.Button(root, text="登录", command=on_login)
    login_button.pack(pady=20)


    root.mainloop()
