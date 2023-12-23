import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image
import qrcode

ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

window = ctk.CTk()
window.geometry("300x475")
window.title("QR Code Generator")
window.iconbitmap("icon.ico")


def center_window(window1, width, height):
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window1.geometry(f"{width}x{height}+{x}+{y}")


def change_mode():
    if change_mode_switch.get():
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


def createQR():
    qr_text = "Empty"
    if phone_entry.get():
        qr_text = f"tel:{phone_entry.get()}"
    elif text_text_box.get(index1="1.0", index2="end-1c"):
        qr_text = text_text_box.get(index1="1.0", index2="end-1c")
    elif link_entry.get():
        qr_text = link_entry.get()
    elif wifi_entry_SSID.get() and wifi_entry_password.get():
        qr_text = f"WIFI:T:{wifi_segmented_buttons.get()};S:{wifi_entry_SSID.get()};P:{wifi_entry_password.get()};;"
    elif sms_phone_entry.get() and sms_text_box.get(index1="1.0", index2="end-1c"):
        qr_text = f"SMSTO:{sms_phone_entry.get()}:{sms_text_box.get(index1="1.0", index2="end-1c")}"
    elif email_address_entry.get() and email_subject_entry.get() and email_text_box.get(index1="1.0", index2="end-1c"):
        qr_text = (f"mailto:{email_address_entry.get()}?subject={email_subject_entry.get()}&body="
                   f"{email_text_box.get(index1="1.0", index2="end-1c")}")

    if qr_text != "Empty":
        new_window = ctk.CTkToplevel(window)
        new_window.title("QR Code")
        new_window.iconbitmap("icon.ico")
        center_window(new_window, width=300, height=370)

        new_frame_3 = ctk.CTkFrame(master=new_window, width=280, height=280)
        new_frame_3.pack(padx=10, pady=(10, 5))

        new_frame_4 = ctk.CTkFrame(master=new_window, width=280, height=40)
        new_frame_4.pack(padx=10, pady=(5, 10))

        new_qr = qrcode.make(qr_text, box_size=100)
        new_qr.save("new.png")
        img = ctk.CTkImage(light_image=Image.open("new.png"), size=(259, 259))

        new_image_label = ctk.CTkLabel(master=new_frame_3, text="", image=img)
        new_image_label.pack(padx=10, pady=10)

        new_button_1 = ctk.CTkButton(master=new_frame_4, text="Save", width=79, command=saveQR)
        new_button_1.pack(side="left", padx=(49, 10), pady=10)

        new_button_2 = ctk.CTkButton(master=new_frame_4, text="Close", width=79, command=new_window.destroy)
        new_button_2.pack(side="right", padx=(10, 49), pady=10)


def saveQR():
    input_path = filedialog.asksaveasfilename(title="Save QR Code",
                                              filetypes=(("PNG File", ".png"),
                                                         ("All Files", "*.*")))
    if input_path:
        if input_path.endswith(".png"):
            img = Image.open("new.png")
            img.save(input_path)
        else:
            input_path = f"{input_path}.png"
            img = Image.open("new.png")
            img.save(input_path)


def clicker(value):
    text_text_box.delete(index1="1.0", index2="end")
    phone_entry.delete(first_index=0, last_index="end")
    link_entry.delete(first_index=0, last_index="end")
    wifi_entry_password.delete(first_index=0, last_index="end")
    wifi_entry_SSID.delete(first_index=0, last_index="end")
    sms_phone_entry.delete(first_index=0, last_index="end")
    sms_text_box.delete(index1="1.0", index2="end")
    email_address_entry.delete(first_index=0, last_index="end")
    email_subject_entry.delete(first_index=0, last_index="end")
    email_text_box.delete(index1="1.0", index2="end")

    if value == "Text":
        link_entry.pack_forget()
        phone_entry.pack_forget()
        wifi_entry_SSID.pack_forget()
        wifi_entry_password.pack_forget()
        wifi_segmented_buttons.pack_forget()
        sms_phone_entry.pack_forget()
        sms_text_box.pack_forget()
        email_address_entry.pack_forget()
        email_subject_entry.pack_forget()
        email_text_box.pack_forget()

        text_text_box.pack(padx=10, pady=10)

    elif value == "Link":
        text_text_box.pack_forget()
        phone_entry.pack_forget()
        wifi_entry_SSID.pack_forget()
        wifi_entry_password.pack_forget()
        wifi_segmented_buttons.pack_forget()
        sms_phone_entry.pack_forget()
        sms_text_box.pack_forget()
        email_address_entry.pack_forget()
        email_subject_entry.pack_forget()
        email_text_box.pack_forget()

        link_entry.configure(placeholder_text="Put your link here")
        link_entry.pack(pady=10, padx=10)

    elif value == "Call":
        text_text_box.pack_forget()
        link_entry.pack_forget()
        wifi_entry_SSID.pack_forget()
        wifi_entry_password.pack_forget()
        wifi_segmented_buttons.pack_forget()
        sms_phone_entry.pack_forget()
        sms_text_box.pack_forget()
        email_address_entry.pack_forget()
        email_subject_entry.pack_forget()
        email_text_box.pack_forget()

        phone_entry.configure(placeholder_text="Phone number")
        phone_entry.pack(pady=10, padx=10)

    elif value == "Wi-Fi":
        text_text_box.pack_forget()
        link_entry.pack_forget()
        phone_entry.pack_forget()
        sms_phone_entry.pack_forget()
        sms_text_box.pack_forget()
        email_address_entry.pack_forget()
        email_subject_entry.pack_forget()
        email_text_box.pack_forget()

        wifi_segmented_buttons.pack(pady=(10, 5), padx=10)
        wifi_entry_SSID.configure(placeholder_text="Wi-Fi SSID (Name)")
        wifi_entry_SSID.pack(pady=5, padx=10)
        wifi_entry_password.configure(placeholder_text="Password")
        wifi_entry_password.pack(pady=(5, 10), padx=10)

    elif value == "SMS":
        text_text_box.pack_forget()
        link_entry.pack_forget()
        wifi_entry_SSID.pack_forget()
        wifi_entry_password.pack_forget()
        wifi_segmented_buttons.pack_forget()
        phone_entry.pack_forget()
        email_address_entry.pack_forget()
        email_subject_entry.pack_forget()
        email_text_box.pack_forget()

        sms_phone_entry.configure(placeholder_text="Phone number")
        sms_phone_entry.pack(pady=(10, 5), padx=10)
        sms_text_box.pack(pady=(5, 10), padx=10)

    elif value == "Email":
        link_entry.pack_forget()
        phone_entry.pack_forget()
        wifi_entry_SSID.pack_forget()
        wifi_entry_password.pack_forget()
        wifi_segmented_buttons.pack_forget()
        sms_phone_entry.pack_forget()
        sms_text_box.pack_forget()
        text_text_box.pack_forget()

        email_address_entry.configure(placeholder_text="Email address")
        email_address_entry.pack(pady=(10, 5), padx=10)
        email_subject_entry.configure(placeholder_text="Email subject")
        email_subject_entry.pack(pady=5, padx=10)
        email_text_box.pack(pady=(5, 10), padx=10)


frame_1 = ctk.CTkFrame(master=window, width=280, height=40)
frame_1.pack(padx=10, pady=(10, 5))

frame_2 = ctk.CTkFrame(master=window, width=280, height=40)
frame_2.pack(padx=10, pady=5)

frame_3 = ctk.CTkFrame(master=window)
frame_3.pack(padx=10, pady=5)

frame_4 = ctk.CTkFrame(master=window, width=280, height=40)
frame_4.pack(padx=10, pady=(5, 10))

change_mode_switch = ctk.CTkSwitch(master=frame_1, text="", onvalue=1, offvalue=0, command=change_mode)
change_mode_switch.place(x=235, y=9)

change_mode_switch_label = ctk.CTkLabel(master=frame_1, text="Dark mode", font=("Arial", 13))
change_mode_switch_label.place(x=10, y=6)

menu_segmented_buttons = ctk.CTkSegmentedButton(master=frame_2,
                                                values=["Text", "Link", "Wi-Fi", "Call", "Email", "SMS"],
                                                command=clicker)
menu_segmented_buttons.place(x=17, y=6)
menu_segmented_buttons.set(value="Text")

text_text_box = ctk.CTkTextbox(master=frame_3, width=260, font=("Arial", 15))
text_text_box.pack(pady=10, padx=10)

link_entry = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))

phone_entry = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))

wifi_segmented_buttons = ctk.CTkSegmentedButton(master=frame_3, values=["WPA", "WPA2", "WPA3", "WEP", ])
wifi_segmented_buttons.set(value="WPA2")
wifi_entry_SSID = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))
wifi_entry_password = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))

sms_phone_entry = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))
sms_text_box = ctk.CTkTextbox(master=frame_3, width=260, font=("Arial", 15))

email_address_entry = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))
email_subject_entry = ctk.CTkEntry(master=frame_3, width=260, font=("Arial", 17))
email_text_box = ctk.CTkTextbox(master=frame_3, width=260, font=("Arial", 15))

entry_2 = ctk.CTkEntry(master=frame_4, width=260, font=("Arial", 17))
entry_2.pack(pady=(10, 5), padx=10)
entry_2.destroy()

entry_3 = ctk.CTkEntry(master=frame_4, width=260, font=("Arial", 17))
entry_3.pack(pady=(10, 5), padx=10)
entry_3.destroy()

qrcode_create_button = ctk.CTkButton(master=frame_4, text="Create", width=79, command=createQR)
qrcode_create_button.pack(side="right", padx=(190, 10), pady=(10, 10))

window.mainloop()
