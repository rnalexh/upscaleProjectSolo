import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def upscale_image():
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp")]
    )

    if not file_path:
        return

    try:
        img = Image.open(file_path)
        upscaled = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)

        # Criar nome do novo arquivo
        dir_name, file_name = os.path.split(file_path)
        name, ext = os.path.splitext(file_name)
        new_file = os.path.join(dir_name, f"upscaled_{name}.jpg")
        upscaled.save(new_file)

        messagebox.showinfo("Sucesso", f"Imagem upscalada salva como:\n{new_file}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criar interface
root = tk.Tk()
root.title("Upscaler de Imagem")
root.geometry("300x150")

label = tk.Label(root, text="Clique no botão para selecionar uma imagem")
label.pack(pady=10)

btn = tk.Button(root, text="Selecionar Imagem", command=upscale_image)
btn.pack(pady=10)

root.mainloop()
