import tkinter as tk
from tkinter import font
from tkinter import ttk

from controller.input_controller import InputController

class MainGui(tk.Frame):

    SEX = ("Male", "Female")

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.pack()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.str_name = tk.StringVar()
        self.str_sex = tk.StringVar()
        self.str_title = tk.StringVar()
        self.str_date = tk.StringVar()

        FONT = font.Font(family="Helvetica", size=16)
        self.option_add("*Font", FONT)

        lbl_speaker = tk.Label(self, text="Speaker Fullname with prefix (Mr./Ms.)")
        self.ent_speaker = ttk.Entry(self, textvariable=self.str_name)
        lbl_sex = tk.Label(self, text="Sex")
        self.cmb_sex = ttk.Combobox(self, values=self.SEX, state="readonly", textvariable=self.str_sex)
        lbl_title = tk.Label(self, text="Webinar Title")
        self.ent_title = ttk.Entry(self, textvariable=self.str_title)
        lbl_date = tk.Label(self, text="Webinar Date")
        self.ent_date = ttk.Entry(self, textvariable=self.str_date)

        lbl_speaker.grid(row=0, column=0, sticky="nsw")
        self.ent_speaker.grid(row=1, column=0, sticky="nsew")
        lbl_sex.grid(row=2, column=0, sticky="nsw")
        self.cmb_sex.grid(row=3, column=0, sticky="nsew")
        lbl_title.grid(row=4, column=0, sticky="nsw")
        self.ent_title.grid(row=5, column=0, sticky="nsew")
        lbl_date.grid(row=6, column=0, sticky="nsw")
        self.ent_date.grid(row=7, column=0, sticky="nsew")

        frame_button = tk.Frame(self)

        self.btn_generate = ttk.Button(frame_button, text="Generate Certificate", command=self.generate_certificate)
        self.btn_clear = ttk.Button(frame_button, text="Clear", command=self.clear_fields)
        self.btn_exit = ttk.Button(frame_button, text="Exit", command=self.quit)

        self.btn_generate.grid(row=0, column=0, sticky="nsew")
        self.btn_clear.grid(row=0, column=1, sticky="nsew")
        self.btn_exit.grid(row=0, column=2, sticky="nsew")

        frame_button.grid(row=8,column=0, sticky="nsew")
        frame_button.grid_rowconfigure(0, weight=1)
        frame_button.grid_columnconfigure(0, weight=1)

        for i in self.winfo_children():
            i.grid_configure(padx=8, pady=3, ipadx=3, ipady=3)
            if i.winfo_class() == "Frame":
                if i.winfo_name() == "frame_button":
                    i.grid_configure(padx=(100, 10))
                for j in i.winfo_children():
                    j.grid_configure(padx=10, pady=(50, 5), ipadx=5, ipady=5)
            if i.winfo_class() == "TEntry" or i.winfo_class() == "TCombobox":
                i['width'] = 50


    def clear_fields(self):
        self.str_name.set("")
        self.str_sex.set("")
        self.str_title.set("")
        self.str_date.set("")

    def generate_certificate(self):
        cert_info = {'name': self.str_name.get(), 'sex': self.str_sex.get(), 'title': self.str_title.get(),
                     'date': self.str_date.get()}

        cert = InputController()
        cert.name = cert_info['name']
        cert.sex = cert_info['sex']
        cert.title = cert_info['title']
        cert.date = cert_info['date']
        cert.submit_to_process()
