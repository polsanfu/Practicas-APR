from pixel import Pixel

pix__1 = (input("Introduzca el primer pixel (R,G,B,A): "))
pix__2 = (input("Introduzca el segundo pixel (R,G,B,A): "))

pix__1 = pix__1.split(",")
pixel = Pixel(pix__1[0], pix__1[1], pix__1[2], pix__1[3])
pix__2 = pix__2.split(",")
pix__2 =(pix__2[0],pix__2[1], pix__2[2], pix__2[3])
promedio = Pixel.pixel_promedio(pixel, pix__2)
print(promedio)