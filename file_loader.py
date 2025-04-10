import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from loader_csv import load_csv

def load_csv_file():
    csv_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if csv_path:
        try:
            df = load_csv(csv_path)  # Validate and load CSV (modify if needed)
            num_count = df.shape[0]  # Number of rows (assuming each row has a number)
            messagebox.showinfo("Éxito", f"CSV cargado correctamente\nNúmeros: {num_count}")
            return csv_path, num_count
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return None, 0
    return None, 0