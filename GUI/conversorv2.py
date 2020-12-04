import tkinter as tk

root = tk.Tk()
root.title("Conversor Gb-Mb")
root.geometry("543x300")

### Labels

title = tk.Label(root, text = "GigaBytes to MegaBytes", width = 25, height = 4, font = "Helvetica 15", bg = "lightgreen")
result = tk.Label(root, width = 25, height = 8, font = "Helvetica 15")

title.pack(fill=tk.X, pady=(0, 20))

### Entries

mbEntry = tk.Entry(root, font = "Helvetica 15")

mbEntry.pack()

### Functions

def convert():
    mbs = int(mbEntry.get())
    result["text"] = str(mbs * 1024) + " Megabytes"

### Buttons

send = tk.Button(root, text = "Convertir", font = "Helvetica 15", command = convert)
send.pack()
result.pack()

root.mainloop()