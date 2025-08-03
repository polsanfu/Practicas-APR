class Pixel:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.pixel_promedio_ = []
    def pixel_promedio(self, otro_pixel):
        pix_2 = otro_pixel
        pix_1 = [self.r,self.g,self.b,self.a]
        pixel_promedio_ = []
        for x in range(0,len(pix_1),1):
            promedio = round((int(pix_1[x]) + int(pix_2[x])) / 2)
            pixel_promedio_.append(promedio)
        return pixel_promedio_
    def __str__(self):
        return "Pixel promedio: " + str(self.pixel_promedio_)