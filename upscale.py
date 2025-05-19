import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import subprocess
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

        dir_name, file_name = os.path.split(file_path)
        name, ext = os.path.splitext(file_name)
        new_file = os.path.join(dir_name, f"upscaled_{name}.jpg")
        upscaled.save(new_file)

        messagebox.showinfo("Sucesso", f"Imagem upscalada salva como:\n{new_file}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def upscale_video():
    file_path = filedialog.askopenfilename(
        title="Selecione um vídeo",
        filetypes=[("Vídeos", "*.mp4 *.avi *.mov *.mkv")]
    )

    if not file_path:
        return

    dir_name, file_name = os.path.split(file_path)
    name, ext = os.path.splitext(file_name)
    output_path = os.path.join(dir_name, f"upscaled_{name}.mp4")

    command = [
        "ffmpeg",
        "-i", file_path,
        "-vf", "scale=iw*2:ih*2",
        "-c:a", "copy",
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Sucesso", f"Vídeo upscalado salvo como:\n{output_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Erro ao executar FFmpeg:\n{e}")
    except FileNotFoundError:
        messagebox.showerror("Erro", "FFmpeg não encontrado. Verifique se está instalado e no PATH.")

# Interface unificada
root = tk.Tk()
root.title("Upscaler de Imagem e Vídeo")
root.geometry("350x200")

label = tk.Label(root, text="Selecione uma das opções para upscalar:")
label.pack(pady=15)

btn_image = tk.Button(root, text="Upscalar Imagem", command=upscale_image, width=25)
btn_image.pack(pady=10)

btn_video = tk.Button(root, text="Upscalar Vídeo", command=upscale_video, width=25)
btn_video.pack(pady=10)

root.mainloop()
