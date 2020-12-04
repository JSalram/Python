import tkinter as tk

root = tk.Tk()
root.geometry("543x300")

### Labels

gb = tk.Label(root, text = "Gigabytes", width = 25, height = 2)
to = tk.Label(root, text = "to", width = 25, height = 2)
mb = tk.Label(root, text = "MegaBytes", width = 25, height = 2)
result = tk.Label(root, text = "RESULTADO", width = 25, height = 8)

gb.grid(row = 0, column = 0)
to.grid(row = 0, column = 1)
mb.grid(row = 0, column = 2)
result.grid(row = 3, column = 1)

### Entries

mbEntry = tk.Entry(root)
gbEntry = tk.Entry(root)

mbEntry.grid(row = 1, column = 0)
gbEntry.grid(row = 1, column = 2)

### Functions

def convert():
    mbs = int(mbEntry.get())
    result["text"] = str(mbs * 1024) + " Megabytes"

### Buttons

send = tk.Button(root, text = "Convertir", command = convert)
send.grid(row = 2, column = 1)

root.mainloop()