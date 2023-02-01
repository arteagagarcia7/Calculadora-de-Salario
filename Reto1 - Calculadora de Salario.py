print ("Por favor digite el Salario Base, las horas extras y las bonificaciones; sin puntos y con un espacio entre cada uno.")

Salariobase, Totalhoraextra, Totalbonos = input().split()
Salariobase = float(Salariobase)
Totalhoraextra = int(Totalhoraextra)
Totalbonos = int(Totalbonos)

Horatrabajo = Salariobase / 192
Totalhoraextra = ((Horatrabajo * 1.25) * Totalhoraextra)
Totalbonos = Salariobase * 0.05 * Totalbonos
Salariosindescuentos = Salariobase + Totalhoraextra + Totalbonos
Valorobligaciones = ((Salariosindescuentos * 8.5) /100)
SalarioTotal = Salariosindescuentos - Valorobligaciones

print("Su sueldo correspondiente a este mes es de:")
print (round (SalarioTotal,1))
