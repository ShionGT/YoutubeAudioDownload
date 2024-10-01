import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

# Function to download YouTube audio using yt-dlp
def download_audio():
    url = url_entry.get()
    download_path = path_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    if not download_path:
        messagebox.showerror("Error", "Please select a download path.")
        return

    try:
        # Options for yt-dlp to download only audio in mp3 format
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", f"Audio has been successfully downloaded to {download_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse and select download path
def browse_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, selected_path)

# Create main application window
app = tk.Tk()
app.title("YouTube Audio Downloader")

# YouTube URL input field
tk.Label(app, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Download path selection
tk.Label(app, text="Download Path:").grid(row=1, column=0, padx=10, pady=10)
path_entry = tk.Entry(app, width=50)
path_entry.grid(row=1, column=1, padx=10, pady=10)
browse_button = tk.Button(app, text="Browse", command=browse_path)
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Download button
download_button = tk.Button(app, text="Download", command=download_audio, bg="green", fg="white")
download_button.grid(row=2, column=1, padx=10, pady=20)

# Run the application
app.mainloop()
