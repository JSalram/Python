class Avion:
    def __init__(self, tipo):
        self.tipo = self.listaAvion(tipo)
        self.grupo = self.listaGrupo(tipo)
        self.horas = []
        self.annos = {}
        self.gActivo = []
        self.hCambio = []
        self.hDia()
        self.agrupaAnnos()

    @staticmethod
    def listaAvion(tipo):
        tipoAvion = [
            "diamonds",
            "pipers",
            "acrobaticas"
        ]

        return tipoAvion[tipo]

    @staticmethod
    def listaGrupo(tipo):
        tipoGrupo = {
            0: ["D1-D2", "D3-D4", "D5-D6"],
            1: ["P1-P5", "P6-P10", "P11-P15", "P16-P20"],
            2: ["S1", "R1"]
        }

        return tipoGrupo[tipo]

    @staticmethod
    def anno(dia):
        annos = [
            1,
            251,
            507,
            758,
            1014,
            1268,
            1522,
            1776,
            2029,
            2284
        ]

        if dia in annos:
            return annos.index(dia)
        else:
            return ""

    def compruebaIns(self, horas):

        if self.tipo != "diamonds":
            if (horas / 500) % 2 == 0 and horas % 1000 == 0:
                return 1000
            elif horas % 500 == 0:
                return 500
            elif horas % 100 == 0:
                return 100
            else:
                return 50

        else:
            tipoInspeccion = {
                1000: [1000, 3000, 5000],
                2000: [2000],
                4000: [4000],
                6000: [6000]
            }

            clave = -1
            for h in tipoInspeccion:
                if horas in tipoInspeccion[h]:
                    clave = h

            if clave > 0:
                return clave
            elif (horas / 100) % 2 == 0:
                return 200
            else:
                return 100

    def cambiaGrupo(self, horas, g):
        ult = len(self.grupo)
        self.hCambio.append(horas)

        g += 1
        if g == ult:
            g = 0

        return g

    def hDia(self):
        g = 0
        j = 1
        for i in range(2539):
            h = 5 * j

            self.horas.append(h)
            self.gActivo.append(self.grupo[g])

            if h % 100 == 0 and self.tipo == "diamonds":
                g = self.cambiaGrupo(h, g)

            elif h % 50 == 0 and self.tipo != "diamonds":
                g = self.cambiaGrupo(h, g)

            j += 1

    def agrupaAnnos(self):
        nHoras = 50
        if self.tipo == "diamonds":
            nTipos = 3
            nHoras = 100
        elif self.tipo == "pipers":
            nTipos = 4
        else:
            nTipos = 2

        dia = 1
        hGrupo = [0]
        cambio = 0
        anno = 2021

        for h in self.horas:
            if self.anno(dia) != "":
                anno = f"20{20 + (self.anno(dia) + 1)}"
                self.annos[anno] = {
                    "dia": [],
                    "hAct": [],
                    "gActivo": [],
                    "hIns": [],
                    "tipoIns": []
                }

            if h in self.hCambio:
                hIns = int(round(self.horas[dia - 1] - hGrupo[-1], 0))
                self.annos[anno]["dia"] += [dia]
                self.annos[anno]["hAct"] += [self.horas[dia - 1]]
                self.annos[anno]["gActivo"] += [self.gActivo[dia - 1]]
                self.annos[anno]["hIns"] += [hIns]
                self.annos[anno]["tipoIns"] += [self.compruebaIns(hIns)]

                hGrupo.append(h - cambio)

                if len(hGrupo) % nTipos == 0:
                    cambio += nHoras

            dia += 1

    def annoIns(self, anno):
        a = self.annos[str(anno)]
        ins = {
            "tiposIns": [],
            "cant": []
        }

        for i in range(len(a["tipoIns"])):
            if a["tipoIns"][i] not in ins["tiposIns"]:
                ins["tiposIns"].append(a["tipoIns"][i])
                ins["cant"].append(1)
            else:
                pos = ins["tiposIns"].index(a["tipoIns"][i])
                ins["cant"][pos] += 1

        return ins

    def printAnno(self, anno):
        a = self.annos[str(anno)]
        ins = self.annoIns(anno)

        print(f"\n\n[______________AÑO_{anno}______________]\n\n")
        for i in range(len(a["dia"])):
            print(f"Día {a['dia'][i]}:\n")
            print(f"   Horas de actividad: {a['hAct'][i]}")
            print(f"   Grupo: {a['gActivo'][i]}.")
            print(f"   Horas motor grupo: {a['hIns'][i]}.")
            print(f"   Tipo inspección: {a['tipoIns'][i]}.\n")

        print("\nTOTAL INSPECCIONES:")
        for i in range(len(ins["tiposIns"])):
            print(f" - Inspecciones {ins['tiposIns'][i]}h: {ins['cant'][i]}")
        print("\n")
