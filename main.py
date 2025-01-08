import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import os
import sys
import requests


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def send_webhook(data):
    # ดึงเวลาปัจจุบัน
    
    
    # URL ของ Webhook ที่คุณสร้างจาก Discord
    webhook_url = 'https://discord.com/api/webhooks/1297513755902607411/lOCc17ocDwXDA_mwGP8L41l2g2m_ptjcIaPYJ-ZOrZnuoafN_M0Uhiub7vd6_P9VC9xV'

    # ข้อความที่ต้องการส่ง
    data = {
        "content": data,
        "username": "Sapphxre 4.0 BETA"  # ชื่อผู้ส่งที่ต้องการแสดงใน Discord# "Python Version: {python_version}")
    }

    # ส่ง POST request ไปยัง Discord Webhook
    response = requests.post(webhook_url, json=data)

    # # ตรวจสอบผลลัพธ์การส่งข้อมูล
    # if response.status_code == 204:
    #     # print('ส่งข้อความสำเร็จ!')
    # else:
    #     # print(f'ส่งข้อความไม่สำเร็จ: {response.status_code}')


class App :

        def __init__(self,root):

                self.root = root
                self.root.title("Sapphxre 4.0")
                self.root.geometry("500x500") #size oof windows
                self.root.resizable(False, False)

                self.image = Image.open(resource_path("icons/Sapphxre_main.png")) #background picture
                self.bg_image = ImageTk.PhotoImage(self.image.resize((500, 500)))#size of background picture

                # # ใส่ Label เป็นพื้นหลัง
                self.background_label = tk.Label(self.root, image=self.bg_image)
                self.background_label.place(x=0, y=0, relwidth=1, relheight=1)  # ปรับขนาดให้เต็มหน้าต่าง

                self.add_menu_frame()
                self.add_delete_temp()
                self.add_bottle_menu()
                self.add_pool_menu()
                self.add_bug_report_menu()




        # สร้างฟังก์ชันโหลดรูปภาพและแปลงเป็นรูปภาพสำหรับ Tkinter
        def load_image(self,image_path, size=None):
                image = Image.open(image_path)
                if size:
                        image = image.resize(size, Image.ANTIALIAS)  # ปรับขนาด
                        return ImageTk.PhotoImage(image)

        def add_menu_frame(self):
                #menu frame
                self.menu_frame = tk.Frame(self.root, bg="#000000", relief="sunken", borderwidth=0)#2f3542 to debug
                # กำหนดตำแหน่งและขนาดด้วย place
                self.menu_frame.place(x=230, y=70, width=250, height=350)


        def add_delete_temp(self):
                
                self.delete_pic = Image.open(resource_path("icons/delete_icons.png")) #background picture
                self.delete_logo = ImageTk.PhotoImage(self.delete_pic.resize((50, 50)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.delete_logo,
                                        text="DELETE TEMP FILE",
                                        compound="left", 
                                        command=self.show_confirm_delete_temp,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=55, width=240, height=50)
         

        def add_bottle_menu(self):
                self.bottle_pic = Image.open(resource_path("icons/bottle_logo.png")) #background picture
                self.bottle_logo = ImageTk.PhotoImage(self.bottle_pic.resize((50, 50)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.bottle_logo,
                                        text="BOTTLE SETTING",
                                        compound="left", 
                                        command=self.bottle_mode,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=110, width=240, height=50)

        def add_pool_menu(self):
                self.pool_pic = Image.open(resource_path("icons/pool_logo.png")) #background picture
                self.pool_logo = ImageTk.PhotoImage(self.pool_pic.resize((50, 50)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.pool_logo,
                                        text="POOL CUE SETTING",
                                        compound="left", 
                                        command=self.pool_mode,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=165, width=240, height=50)

        def add_bug_report_menu(self):
                self.bug_pic = Image.open(resource_path("icons/bug_report_icons.png")) #background picture
                self.bug_logo = ImageTk.PhotoImage(self.bug_pic.resize((50, 50)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.bug_logo,
                                        text="BUG REPORT",
                                        compound="left", 
                                        command=self.bug_report_pass,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=250, width=240, height=50)

        def clear_content_frame(self):
                """ ลบเนื้อหาทั้งหมดใน content_frame """
                for widget in self.menu_frame.winfo_children():
                        widget.destroy()

        def show_confirm_delete_temp(self):
                self.clear_content_frame()

                self.label_confirm_delete = tk.Label(
                                                        self.menu_frame,
                                                        text="Confirm Delete?",
                                                        font=("Segoe UI", 24, "bold"),
                                                        fg="white",  # สีตัวหนังสือ
                                                        bg="black"   # สีพื้นหลัง
                                                        )
                self.label_confirm_delete.place(x=5, y=60)



                self.confirm_delete = Image.open(resource_path("icons/check_white.png")) #background picture
                self.confirm_logo = ImageTk.PhotoImage(self.confirm_delete.resize((25, 25)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.confirm_logo,
                                        text=" Delete temp",
                                        compound="left", 
                                        command=self.confrim_delete_pass,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=150, width=240, height=50)

                self.cancel_delete_pic = Image.open(resource_path("icons/cross_white.png")) #background picture
                self.cancel_delete_logo = ImageTk.PhotoImage(self.cancel_delete_pic.resize((25, 25)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.cancel_delete_logo,
                                        text=" Cencel",
                                        compound="left", 
                                        command=self.show_home_menu,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=205, width=240, height=50)

        def show_home_menu(self):
                self.clear_content_frame()
                self.add_delete_temp()
                self.add_bottle_menu()
                self.add_pool_menu()
                self.add_bug_report_menu()

        def bottle_mode(self):
                self.clear_content_frame()

                self.label_bottle_mode = tk.Label(
                                                        self.menu_frame,
                                                        text="Bottle Mode",
                                                        font=("Segoe UI", 24, "bold"),
                                                        fg="white",  # สีตัวหนังสือ
                                                        bg="black"   # สีพื้นหลัง
                                                        )
                self.label_bottle_mode.place(x=30, y=60)

                self.run_bottle_pic = Image.open(resource_path("icons/cmd_icon.png")) #background picture
                self.run_bottle_logo = ImageTk.PhotoImage(self.run_bottle_pic.resize((50, 50)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.run_bottle_logo,
                                        text=" Run cmd bottle",
                                        compound="left", 
                                        command=self.run_cmd_bottle,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=150, width=240, height=50)

                self.cancel_pic = Image.open(resource_path("icons/cross_white.png")) #background picture
                self.cancel_logo = ImageTk.PhotoImage(self.cancel_pic.resize((25, 25)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.cancel_logo,
                                        text=" Cencel",
                                        compound="left", 
                                        command=self.show_home_menu,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=205, width=240, height=50)
                

        def confrim_delete_pass(self):
                path = resource_path("./source/Clear_temp.bat")
                os.system(path)
                messagebox.showinfo("Sapphxre 4.0", "Delete temp complete.")
                # exit()
                self.show_home_menu()
                

        def run_cmd_bottle(self):
                path = resource_path("./source/base_cmd.bat")
                cmd_path = resource_path("./source/bottle_rum.bat")
                os.system(path)
                os.system(cmd_path)
                messagebox.showinfo("Sapphxre 4.0", "Run cmd bottle complete.")
                self.show_home_menu()

        def pool_mode(self):
                self.clear_content_frame()

                self.label_pool_mode = tk.Label(
                                                        self.menu_frame,
                                                        text="Pool cue Mode",
                                                        font=("Segoe UI", 24, "bold"),
                                                        fg="white",  # สีตัวหนังสือ
                                                        bg="black"   # สีพื้นหลัง
                                                        )
                self.label_pool_mode.place(x=10, y=60)

                self.run_pool_pic = Image.open(resource_path("icons/cmd_icon.png")) #background picture
                self.run_pool_logo = ImageTk.PhotoImage(self.run_pool_pic.resize((50, 50)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.run_pool_logo,
                                        text=" Run cmd pool",
                                        compound="left", 
                                        command=self.run_cmd_pool,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=150, width=240, height=50)

                self.cancel_pic = Image.open(resource_path("icons/cross_white.png")) #background picture
                self.cancel_logo = ImageTk.PhotoImage(self.cancel_pic.resize((25, 25)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.cancel_logo,
                                        text=" Cencel",
                                        compound="left", 
                                        command=self.show_home_menu,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=205, width=240, height=50)

        def run_cmd_pool(self):
                path = resource_path("./source/base_cmd.bat")
                cmd_path = resource_path("./source/pool_rum.bat")
                os.system(path)
                os.system(cmd_path)
                messagebox.showinfo("Sapphxre 4.0", "Run cmd bottle complete.")
                self.show_home_menu()

        def submit_data_report(self):
                # ดึงข้อมูลจาก Text Box
                user_input = self.text_box.get("1.0", tk.END).strip()  # ดึงข้อความตั้งแต่แถวที่ 1 คอลัมน์ที่ 0 ถึงจบ
                #print("ข้อมูลที่กรอก:\n", user_input)
                send_webhook(user_input)
                messagebox.showinfo("Sapphxre 4.0", "Send report complete.")
                self.show_home_menu()

        def bug_report_pass(self):
                self.clear_content_frame()
                self.bug_report_lable = tk.Label(
                                                        self.menu_frame,
                                                        text="Report",
                                                        font=("Segoe UI", 24, "bold"),
                                                        fg="white",  # สีตัวหนังสือ
                                                        bg="black"   # สีพื้นหลัง
                                                        )
                self.bug_report_lable.place(x=10, y=20)
                # สร้าง Text Box (5 บรรทัด, ความกว้าง 40 ตัวอักษร)
                self.text_box = tk.Text(self.menu_frame, height=7, width=28)
                self.text_box.place(x=5, y=80)

                self.submit_pic = Image.open(resource_path("icons/check_white.png")) #background picture
                self.submit_logo = ImageTk.PhotoImage(self.submit_pic.resize((25, 25)))

                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.submit_logo,
                                        text=" Send report",
                                        compound="left", 
                                        command=self.submit_data_report,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=210, width=240, height=50)

                self.cancel_pic = Image.open(resource_path("icons/cross_white.png")) #background picture
                self.cancel_logo = ImageTk.PhotoImage(self.cancel_pic.resize((25, 25)))
                
                # สร้างปุ่มที่มีรูปภาพ
                self.button = tk.Button(self.menu_frame, 
                                        image=self.cancel_logo,
                                        text=" Cencel",
                                        compound="left", 
                                        command=self.show_home_menu,
                                        bg="#000000",
                                        fg="#FFFFFF", 
                                        activebackground="#000000", 
                                        relief="flat", 
                                        borderwidth=0)
                self.button.place(x=5, y=265, width=240, height=50)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()