class ExpresionHoraria:
    def __init__(self, horas, minutos, segundos):
        self.horas = int(horas)
        self.minutos = int(minutos)
        self.segundos = int(segundos)

    def seg_medianoche(self):
        total_segs = int((self.horas*3600)) + int((self.minutos*60)) + int(self.segundos)
        if int(total_segs) <= 43200:
            total_segs = 43200 - total_segs
        else:
            total_segs = 86400 - total_segs
        return total_segs

    def __str__(self):
        horas_str = f"{self.horas:02}"
        minutos_str = f"{self.minutos:02}"
        segundos_str = f"{self.segundos:02}"
        return f"{horas_str}:{minutos_str}:{segundos_str}"

