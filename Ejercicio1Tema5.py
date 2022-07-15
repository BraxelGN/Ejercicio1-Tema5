def areaTriangulo(altura=0.0, base = 0.0):
    area = (altura*base)/2
    print("El area del triangulo es: ", area,"cm")
    
def areaCirculo (radio=0.0):
    area = (3.14 * radio**2)
    print("El area del circulo es: ", area,"cm")
    

areaTriangulo(5.0 , 10.0)
areaCirculo (3.0)
