#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:42:44 2022

@author: chulke

@email: gustavogodoy85@gmail.com
"""
####hp probook##### proton mail

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
    '''
    Imprime en pantalla las opciones a elegir.
    Retorna un string con la opcion elegida (a,b,c,d,e o q)
    '''
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
    '''
    Recibe una lista con numeros int o float.
    Retorna el valor resultante de sumar los elementos de la lista.
    '''
    res = 0
    for i in lista:
        res += i
    return res


def promedio(lista):
    '''
    Recibe una lista con numeros int o float.
    Retorna el promedio de los valores de la lista.
    '''
    res = suma(lista)/len(lista)
    return res


def maximo(lista):
    '''
    Recibe una lista con numeros int o float.
    Retorna el mayor de los valores de la lista.
    '''
    res = max(lista)
    return res


def minimo(lista):
    '''
    Recibe una lista con numeros int o float.
    Retorna el menor de los valores de la lista.
    '''
    res = min(lista)
    return res


def main():
    '''
    Funcion principal.
    1-Llama a la funcion carga()
    2-Llama a la funcion seleccion()
    3-Segun lo que retorna la funcion seleccion llama a las fuciones:
        a-suma(param)
        b-promedio(param)
        c-maximo(param)
        d-minimo(param)
        e-main()
        q-sys.exit(1)
    '''
    
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
