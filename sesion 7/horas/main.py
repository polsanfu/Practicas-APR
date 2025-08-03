from expresionHoraria import ExpresionHoraria

hora_1 = input("Introduzca primera hora [hh:mm:ss]: ")
hora_2 = input("Introduzca segunda hora [hh:mm:ss]: ")

hora_1 = hora_1.split(":")
save = hora_1
hora_1 = ExpresionHoraria(int(hora_1[0]), int(hora_1[1]), int(hora_1[2]))
hora_1_ = hora_1.seg_medianoche()

hora_2 = hora_2.split(":")
save_2 = hora_2
hora_2 = ExpresionHoraria(int(hora_2[0]),int(hora_2[1]), int(hora_2[2]))
hora_2_ = hora_2.seg_medianoche()

if hora_1_ > hora_2_:
    print(f"La hora más cercana a medianoche es: {hora_2}")
else:
    print(f"La hora mas cercana a medianoche es {hora_1}")
