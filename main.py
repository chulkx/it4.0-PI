#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:42:44 2022

@author: chulke
"""
import sys


def carga():
    try:
        cant = int(input('¿Cuantos numeros desea ingresar? '))
        print(f'Ingrese {cant} numeros por favor: ')
        lista = []
        while len(lista)<cant:
            lista.append(float(input('->: ')))
        return lista
    except:
        print(sys.stderr)
        print('El valor ingresado no es correcto')
        sys.exit(1)

def seleccion():
    print()
    print('Opciones: ')
    print('a -> Sumar todos los elemntos')
    print('b -> Calcular el promedio de los numeros ingresados')
    print('c -> Mostrar el máximo valor ingresado')
    print('d -> Mostrar el menor valor ingresado')
    print('e -> Ingresar otra lista de numeros')
    print('q -> Terminar y salir')
    seleccion = input('Ingrese una opcion: ')
    return seleccion


def suma(lista):
    res = 0
    for i in lista:
        res += i
    return res


def promedio(lista):
    res = suma(lista)/len(lista)
    return res


def maximo(lista):
    res = max(lista)
    return res


def minimo(lista):
    res = min(lista)
    return res


def main():
    print()
    print()
    print('='*50)

    print('Actividad integradora Programacion Inicial IT4.0')
    print('-'*22+'Aula 4'+'-'*22)
    print()
    
    cargados = carga()
    try:
        while True:
            opcion = seleccion()

            if opcion == 'a':
                print('La suma de los elementos es:', suma(cargados))
            
            elif opcion == 'b':
                print('El promedio de los elementos es:', promedio(cargados))

            elif opcion == 'c':
                print('El máximo elemento es:', maximo(cargados))

            elif opcion == 'd':
                print('El mínimo elemento es:', minimo(cargados))

            elif opcion == 'e':
                main()

            elif opcion == 'q':
                sys.exit(1)
            
            else:
                print('Su selección no es correcta. Intente de nuevo.')
                print('Error, el valor ingresado no es válido')
                seguir = input('Si desea intentar de nuevo ingrese "1", si desea salir ingrese "q": ')
                if seguir == '1':
                    main()
                elif seguir == 'q':
                    sys.exit(1)
                else:                    
                    sys.exit(1)

    except:
        print('ERROR')
        print('El valor ingresado no es válido, mejor suerte para la próxima.')
        

if __name__ == '__main__':
    main()