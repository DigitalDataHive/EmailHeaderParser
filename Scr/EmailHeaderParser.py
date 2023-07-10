import tkinter as tk
from tkinter import filedialog
import email
from email.header import decode_header
from PIL import Image, ImageTk

def browse_file():
    """Open a file dialog to select an email file."""
    filename = filedialog.askopenfilename(filetypes=[("Email Files", "*.eml")])
    if filename:
        extract_header_info(filename)

def extract_header_info(filename):
    """Extract and display the header information from the email file."""
    with open(filename, "r", encoding="utf-8") as file:
        msg = email.message_from_file(file)

    header_info = {}
    for header in msg._headers:
        name = header[0]
        value = header[1]

        try:
            # Decode the header value if it's encoded
            decoded_value = decode_header(value)[0][0]
            if isinstance(decoded_value, bytes):
                decoded_value = decoded_value.decode("utf-8")
            header_info[name] = decoded_value
        except Exception as e:
            header_info[name] = value

    display_header_info(header_info)

def display_header_info(header_info):
    """Display the header information in a GUI window."""
    window = tk.Tk()
    window.title("Email Header Information")
    window.geometry("800x900")

    canvas = tk.Canvas(window, height=500)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    for i, (name, value) in enumerate(header_info.items()):
        label = tk.Label(frame, text=f"{name}:", font=("Arial", 14, "bold"))
        label.grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)

        value_text = tk.Text(frame, height=2, width=60, font=("Arial", 12))
        value_text.insert(tk.END, value)
        value_text.config(state=tk.DISABLED)
        value_text.grid(row=i, column=1, padx=10, pady=5)

    window.mainloop()

# Create the GUI window
window = tk.Tk()
window.title("Email Header Extractor")

# Set window title
title_label = tk.Label(window, text="Email Header Extractor", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

# Load and display the logo
logo_image = Image.open("/Users/milliemancilla/Desktop/ddh.png")  # Replace "logo.png" with the path to your logo image file
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(window, image=logo_photo)
logo_label.pack(side=tk.RIGHT, padx=10)

# Create a button to browse and select an email file
browse_button = tk.Button(window, text="Browse", command=browse_file, font=("Arial", 12))
browse_button.pack(pady=20)

window.mainloop()
