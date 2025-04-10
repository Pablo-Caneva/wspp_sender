import pandas as pd
from tkinter import messagebox
from sender import message_sender
from message_formatter import format_message

def send_messages(csv_path, text_box):
    if not csv_path:
        messagebox.showwarning("Advertencia", "Debe cargar el CSV antes de enviar los mensajes.")
        return

    try:
        df = pd.read_csv(csv_path, dtype=str)  # Ensure numbers stay as strings
        numbers = df["numbers"].astype(str).tolist()  # Convert to list
        names = df["names"].tolist()
        message = text_box.get("1.0", "end-1c")
        formatted_messages = [format_message(name, message) for name in names]
        message_sender(numbers, formatted_messages)
        messagebox.showinfo("Éxito", "Mensajes enviados correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))