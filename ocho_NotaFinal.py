print("binvenido a el programa para encontrar la nota final de un estudiante")
n1=float(input("digite la primera nota (15%): "))
n2=float(input("digite la segunda nota (20%): "))
n3=float(input("digite la tercera nota (15%): "))
n4=float(input("digite la cuarta nota (30%): "))
n5=float(input("digite la quinta nota (20%): "))
n1p=n1*0.15
n2p=n2*0.2
n3p=n3*0.15
n4p=n4*0.3
n5p=n5*0.2
nf=n1p+n2p+n3p+n4p+n5p
print("la nota final es: ", nf)


