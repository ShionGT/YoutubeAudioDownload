import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
import os


# Function to download YouTube audio
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
        # Create YouTube object
        yt = YouTube(url)

        # Select the highest quality audio stream using an alternative method
        audio_stream = yt.streams.get_audio_only()

        # Download audio stream
        downloaded_file = audio_stream.download(output_path=download_path)

        # Rename file to .mp3
        base, ext = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)

        messagebox.showinfo("Success", f"Audio has been downloaded and saved as {new_file}")
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
