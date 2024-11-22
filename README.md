# Global_Python
INTEGRANTES:
- Rivas Tobias
- Morgui Mateo
- Diaz Manuel
- Diaz Moyano Sebastian


El repositorio cuenta con 3 archivos:

 - Ejecutable.py (es el que se debe ejecutar y este posee el programa que se le muestra al usuario)
 - Clases.py (este es el archivo que cuenta con todas las clases instanciadas en Ejecutable.py)
 - funciones.py (este archivo posee con funciones utiles que permiten realizar ciertas cosas dentro de Ejecutable.py y Clases.py)



COMO UTILIZAR EN PROGRAMA:

  Se le mostrará por pantalla al usuario, el menú con las opciones a seleccionar 

OPCIONES:

1)- En esta opcion se ingresará el ADN 

  1,1)- Se le explicará al usuario como es el formato de un ADN y como debe ingresar el ADN en el programa

      Formato en el que deberá ingresarlo --->  ["Fila 1","Fila 2","Fila 3","Fila 4","Fila 5","Fila 6"]
 
  1,2)- Se verificará que el ADN cumpla con los parametros establecidos

    Que esté compuesto por bases nitrogenadas --->  "A" (Adenina) , "T" (Tinina) , "C" (Citosina) , "G" (Guanina)    

    Que cumpla con el largo adecuado --->  6 Filas X 6 Columnas
 
  1,3)- Si el ADN cumple con los parametros, se guardará en una variables, de lo contrario, se le pedirá nuevamente que lo ingrese y asi sucesivamente, hasta que cumpla los parametros

2)- En esta opcion se detectaran mutantes en el ADN que el usuario ingreso y retornara true o false segun tenga o no mutante. Los mutantes son celulas nitrogenadas repetidas por lo menos 4 veces de manera continua (una despues de la otra) en cualquier direccion (Vertical, Horizontal y Diagonal)

3)- En esta opcion, se mutará el ADN
 
  3,1)- Se le muestra un menú al usuario, donde se le pregunta si quiere realizar Radiación o un Virus
 
  3,2)- Dependiendo de la opcion ingresada por el usuario, se iniciará la clase Radiacion o Virus

  CLASE RADIACION:

   1)- Se le preguntará al usuario si quiere insertar un mutante de manera horizontal('H') o vertical('V')

   2)- Se le solicitará que ingrese las posicion horizontal y vertical donde desea empezar el mutante a insertar
 
   3)- Finalmente, se mostrará el ADN con los mutantes insertados
 
  CLASE VIRUS:
 
   1)- Se le preguntará al usuario si quiere insertar un mutante en las diagonales de izquiera a derecha o al reves:

   Izquierda a derecha:  ---> D son las diagonales

   ![image](https://github.com/user-attachments/assets/50555926-0cf3-4eac-bea2-9043f099cd09)

   Derecha a Izquierda:  ---> D son las diagonales

   ![image](https://github.com/user-attachments/assets/31a6a3d5-4a57-4427-b4ac-e0f7f47643b4)


   2)- Se le solicitará al usuario que ingrese las posiciones donde desea insertar el mutante
   
   3)- Finalmente, se mostrará el ADN con los mutantes insertados diagonalemente

4)- En esta opcion el programa detectara si el ADN ingresado posee mutantes para poder sanarlo

   4,1)- Si el ADN no posee mutantes, le devolverá al usuario el mismo ADN ingresado

   4,2)- Si el ADN posee mutantes, se generará un ADN completamente nuevo y aleatorio, el cual no tendrá mutantes

5)-En esta opcion el programa muesta el adn con su respectivo formato por ejemplo: 

    ADN = ["AAAAAA","CCCCCC","TTTTTT","GGGGGG","AAAAAA","CCCCCC"]  ---->    A A A A A A
                                                                            C C C C C C 
                                                                            T T T T T T 
                                                                            G G G G G G 
                                                                            A A A A A A 
                                                                            C C C C C C

6)-En esta opcion el programa finaliza.
