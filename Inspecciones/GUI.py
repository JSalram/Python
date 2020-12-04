from tkinter import *
from Avion import Avion


def printAvion():
    t = int(tipo.get())
    anyo = str(anno.get())
    a = Avion(t)
    y = a.annos[anyo]

    year = Tk()
    year.title(f"{a.tipo} {anyo}")
    year.geometry("500x400+600+150")

    Label(year, text=f"Año {anyo}", height=2,
          font="Helvetica 25", bg="lightblue").pack(fill=X)

    dia = Label(year, font="Helvetica 20", anchor=W)
    dia.pack(fill=X, padx=50, pady=10)
    hActividad = Label(year, font="Helvetica 16", anchor=W)
    hActividad.pack(fill=X, padx=75)
    grupo = Label(year, font="Helvetica 16", anchor=W)
    grupo.pack(fill=X, padx=75)
    hIns = Label(year, font="Helvetica 16", anchor=W)
    hIns.pack(fill=X, padx=75)
    tIns = Label(year, font="Helvetica 16", anchor=W)
    tIns.pack(fill=X, padx=75)

    prev = Button(year, text="Anterior", font="Helvetica 15")
    next = Button(year, text="Siguiente", font="Helvetica 15")
    prev.pack()
    next.pack(pady=5)

    def printDay(i=0):
        if i < len(y["dia"]):
            dia["text"] = f"Día {y['dia'][i]}:"
            hActividad["text"] = f" - Horas de actividad: {y['hAct'][i]}"
            grupo["text"] = f" - Grupo: {y['gActivo'][i]}."
            hIns["text"] = f" - Horas motor grupo: {y['hIns'][i]}."
            tIns["text"] = f" - Tipo inspección: {y['tipoIns'][i]}.\n"
        else:
            ins = a.annoIns(anyo)
            label = [hActividad, grupo, hIns, tIns]

            dia["text"] = "TOTAL INSPECCIONES"
            for j in range(len(label)):
                if j < len(ins["tiposIns"]):
                    label[j]["text"] = f" - Inspecciones {ins['tiposIns'][j]}h: {ins['cant'][j]}"
                else:
                    label[j]["text"] = ""

            next["command"] = ""

        if i > 0:
            prev["command"] = lambda: printDay(i - 1)
        if i < len(y["dia"]):
            next["command"] = lambda: printDay(i + 1)

    printDay()
    year.mainloop()


#########################################################################################


root = Tk()
root.title("Inspecciones")
root.geometry("400x325+150+150")

Label(root, text="Modelo de avión", height=2, font="Helvetica 15").pack()

tipo = IntVar()

Radiobutton(root, text="Diamonds", variable=tipo, value=0,
            font="Helvetica 10").pack()
Radiobutton(root, text="Pipers", variable=tipo, value=1,
            font="Helvetica 10").pack()
Radiobutton(root, text="Acrobáticas", variable=tipo, value=2,
            font="Helvetica 10").pack()

Label(root, text="Año", height=2, font="Helvetica 15").pack(pady=(30, 0))
anno = Entry(root, font="Helvetica 10")
anno.pack()

Button(root, text="Mostrar", command=printAvion, font="Helvetica 15").pack(pady=(30, 0))

root.mainloop()
