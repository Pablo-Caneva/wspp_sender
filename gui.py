import tkinter as tk
from tkinter import messagebox
from send_messages import send_messages
from file_loader import load_csv_file

# Global variables
csv_path = ""
num_count = 0
text_box = None
csv_info_label = None  # Label to display CSV info

def run_app():
    global text_box, csv_path, csv_info_label

    # GUI Setup
    root = tk.Tk()
    root.title("WhatsApp Sender")

    # Load CSV Button
    btn_csv = tk.Button(root, text="Cargar CSV", command=set_csv_path)
    btn_csv.pack(pady=5)

    # Label to show CSV info
    csv_info_label = tk.Label(root, text="", fg="green")
    csv_info_label.pack()

    # Frame for Text Box and Scrollbar
    text_frame = tk.Frame(root)
    text_frame.pack(pady=5)

    # Scrollbar
    text_scroll = tk.Scrollbar(text_frame)
    text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    # Message Text Box
    text_box = tk.Text(text_frame, height=50, width=200, yscrollcommand=text_scroll.set)
    text_box.pack()

    # Attach Scrollbar to Text Box
    text_scroll.config(command=text_box.yview)


    # Send Messages Button
    btn_send = tk.Button(root, text="Enviar Mensajes", command=lambda: send_messages(csv_path, text_box))
    btn_send.pack(pady=10)

    root.mainloop()

def set_csv_path():
    global csv_path, num_count, csv_info_label
    csv_path, num_count = load_csv_file()
    if csv_path:
        csv_info_label.config(text=f"Números cargados: {num_count}")