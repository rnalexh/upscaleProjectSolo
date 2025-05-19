import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import os

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

    # Comando ffmpeg para fazer upscale 2x (multiplica resolução por 2)
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

# Interface Tkinter
root = tk.Tk()
root.title("Upscaler de Vídeo")
root.geometry("300x150")

label = tk.Label(root, text="Clique no botão para selecionar um vídeo")
label.pack(pady=10)

btn = tk.Button(root, text="Selecionar Vídeo", command=upscale_video)
btn.pack(pady=10)

root.mainloop()
