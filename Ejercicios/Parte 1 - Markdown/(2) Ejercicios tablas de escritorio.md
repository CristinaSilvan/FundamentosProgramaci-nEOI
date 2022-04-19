# Ejercicios de Algoritmos

## 1. Hola Mundo

* 1.1   Imprimir: _Hola Mundo_

```
print("Hola Mundo")
```

## 2. A partir de un número ingresado diga si es mayor, menor o igual a 9

* 1.1   N: 0
* 1.2   Imprimir: _Escribir el numero_
* 1.3   N: 10
* 1.4   N == 9: _False_
* 1.5   N  > 9: _True_
* 1.6   Imprimir: _El numero es mayor a 9_
---
* 2.1   N: 0
* 2.2   Imprimir: _Escribir el numero_
* 2.3   N: 7
* 2.4   N == 9: _False_
* 2.5   N  > 9: _False_
* 2.6   N  < 9: _True_
* 2.7   Imprimir: _El numero es menor a 9_
---
* 3.1   N: 0
* 3.2   Imprimir: _Escribir el numero_
* 3.3   N: 9
* 3.4   N == 9: _True_
* 3.5   Imprimir: _El numero es igual a 9_

```
N = 0
N = int(input("Escribir el numero "))
if N == 9:
    print("El numero es igual a 9)
else:
    if N > 9:
        print("El numero es mayor a 9)

    else:
        print("El numero es menor a 9)
```

## 3. A partir de un número ingresado diga si el mismo es par o impar

* 1.1   nro: 2
* 1.2   nro % 2 == 0: _True_
* 1.3   Imprimir: _Es par_

---

* 2.1   nro: 3
* 2.2   nro % 2 == 0: _False_
* 2.3   Imprimir: _Es impar_

```
nro = int(input())

if nro % 2 == 0:
    print("Es par")
else:
    print("Es impar")
```

## 4. Ingrese dos números y devuelva el resultado de la suma entre ambos

* 1.1   Num1: 0
* 1.2   Num2: 0
* 1.3   Imprimir: _Escribir el numero 1_
* 1.4   Num1: 2
* 1.5   Imprimir: _Escribir el numero 2_
* 1.6   Num2: 3
* 1.7   Rta: 5
* 1.8   Imprimir: _El resultado es 5_

```
Num1 = 0
Num2 = 0

print("Escribir el numero 1 ")
Num1 = int(input())

print("Escribir el numero 2 ")
Num2 = int(input())

Rta = Num1 + Num2

print("El resultado es ", Rta)
```

## 5. Sumar todos los números pares entre 2 y 100

* 1.1   suma: 0
* 1.2   nro: 2
* 1.3   nro <= 100: _True_
* 1.4   nro % 2 == 0: _True_
* 1.5   suma: 0 + 2
* 1.6   nro: 3

(Salta a **1.3**)
* 1.3   nro <= 100: _True_
* 1.4   nro % 2 == 0: _False_
* 1.6   nro: 4

(Salta a **1.3**)
* 1.3   nro <= 100: _True_
* 1.4   nro % 2 == 0: _True_
* 1.5   suma: 2 + 4
* 1.6   nro: 5

(Salta a **1.3**)
* 1.3   nro <= 100: _True_
* 1.4   nro % 2 == 0: _False_
* 1.6   nro: 6

... (etc etc)

(Continúa el bucle hasta llegar a **nro: 101**)
* 1.6    nro: 101

(Salta a **1.3**)
* 1.3    nro <= 100: _False_

(Salta a **1.7**)
* 1.7   suma: 2550
* 1.8   Imprimir: _La suma de los pares entre 1 y 100 es 2550_

```
suma = 0
nro = 2

while (nro <= 100):
    if nro % 2 == 0:
        suma = suma + nro
    nro = nro + 1

print("La suma de los pares entre 2 y 100 es ",suma)

```

## 6. Ingrese un número y muestre todos los divisores del mismo

* 1.1    Imprimir: _Ingrese Numero_
* 1.2   Num: 4
* 1.3   div: 1
* 1.4   div <= Num: _True_
* 1.5   Num % div == 0: _True_
* 1.6   Imprimir: _1_
* 1.7   div = 2

(Salta a **1.4**)
* 1.4   div <= Num: _True_
* 1.5   Num % div == 0: _True_
* 1.6   Imprimir: _2_
* 1.7   div = 3

(Salta a **1.4**)
* 1.4   div <= Num: _True_
* 1.5   Num % div == 0: _False_
* 1.7   div = 4

(Salta a **1.4**)
* 1.4   div <= Num: _True_
* 1.5   Num % div == 0: _True_
* 1.6   Imprimir: _4_
* 1.7   div = 5

(Salta a **1.4**)
* 1.4   div <= Num: _False_

```
print("Ingrese Numero")
Num = int(input())
div = 1

while div <= Num:
    if Num % div == 0:
        print(div)

    div = div + 1
```

## 7. Determinar si un alumno aprueba o suspende un curso, sabiendo que aprobará si su promedio de tres calificaciones es mayor o igual a 4.0; supsende en caso contrario. Deberá permitir ingresar las tres calificaciones y luego calcular su promedio

* 1.1   Imprimir: _Ingrese calificacion 1_
* 1.2   Cal1: 5
* 1.3   Imprimir: _Ingrese calificacion 2_
* 1.4   Cal2: 7
* 1.5   Imprimir: _Ingrese calificacion 3_
* 1.6   Cal3: 10
* 1.7   Prom: 21/3 (7)
* 1.8   Prom >= 4: _True_
* 1.9   Imprimir: _Aprueba_
* 1.10  Imprimir: _7_

---

* 2.1   Imprimir: _Ingrese calificacion 1_
* 2.2   Cal1: 1
* 2.3   Imprimir: _Ingrese calificacion 2_
* 2.4   Cal2: 4
* 2.5   Imprimir: _Ingrese calificacion 3_
* 2.6   Cal3: 3
* 2.7   Prom: 8/3 (2.6)
* 2.8   Prom >= 4: _False_
* 2.9   Imprimir: _Reprueba_
* 2.10  Imprimir: _2.6_

```
Cal1 = float(input("Ingrese calificacion 1"))
Cal2 = float(input("Ingrese calificacion 2"))
Cal3 = float(input("Ingrese calificacion 3"))

Prom = (Cal1 + Cal2 + Cal3)/3

if Prom >= 4:
    print("Aprueba")
else:
    print("Reprueba")

print(Prom)
```

## 8. Crear un algoritmo que permita ingresar un nombre y una cantidad numérica para escribir este nombre tantas veces como su cantidad ingresada

* 1.1   Imprimir: _Ingresar Nombre_
* 1.2   nombre: Cristina
* 1.3   Imprimir: _Ingresar Cantidad_
* 1.4   num: 3
* 1.5   num > 0: _True_
* 1.6   Imprimir: _Cristina_
* 1.7   Num: 2

(Salta a **1.5**)
* 1.5   num > 0: _True_
* 1.6   Imprimir: _Cristina_
* 1.7   Num: 1

(Salta a **1.5**)
* 1.5   num > 0: _True_
* 1.6   Imprimir: _Cristina_
* 1.7   Num: 0

(Salta a **1.5**)
* 1.5   num > 0: _False_

```
nombre = input("Ingresar Nombre")
num = int(input("Ingresar Cantidad"))

while num > 0:
    print(nombre)
    num = num - 1
```

## 9. Sumar todos los números naturales comprendidos entre 1 y 50

* 1.1   Num: 1
* 1.2   Resul: 0
* 1.3   Num > 50: _False_
* 1.4   Resul: 1
* 1.5   Num: 2

(Salta a **1.3**)
* 1.4   Resul: 3
* 1.5   Num: 3

(Salta a **1.3**)
* 1.4   Resul: 6
* 1.5   Num: 4

(Salta a **1.3**)
* 1.4   Resul: 10
* 1.5   Num: 5

(Salta a **1.3**)
* 1.4   Resul: 15
* 1.5   Num: 6

... (etc etc)

(Salta a **1.3**)
* 1.4   Resul: 1275
* 1.5   Num: 51

(Salta a **1.3**)
* 1.3   Num > 50: _True_
* 1.4   Imprimir: 1275


```
Num = 1
Resul = 0

while not(Num > 50):
    Resul = Resul + Num
    Num = Num + 1

print(Resul)
```

## 10. Leer tres números; si el primero es negativo, debe imprimir la multiplicación de los tres y si no lo es, imprimirá la suma