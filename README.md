# Global_Python
INTEGRANTES:
- Rivas Tobias
- Morgui Mateo
- Diaz Manuel
- Diaz Moyano Sebastian

COMO UTILIZAR EN PROGRAMA:
1)- Se le mostrará por pantalla al usuario, el menú con las opciones a seleccionar 

OPCIONES:
1)- En esta opcion se ingresará el ADN 
 1,1)- Se le explicará al usuario como es el formato de un ADN y como debe ingresar el ADN en el programa
 1,2)- A continuación, se verificará que el ADN cumpla con los parametros establecidos
 1,3)- Si el ADN cumple con los parametros, se guardará en una variables, de lo contrario, se le pedirá 
    nuevamente que lo ingrese y asi sucesivamente, hasta que cumpla los parametros
2)- En esta opcion, se mutará el ADN
 2,1)- Se le muestra un menú al usuario, donde se le pregunta si quiere realizar Radiación o un Virus
 2,2)- Dependiendo de la opcion ingresada por el usuario, se iniciará la clase Radiacion o Virus
 CLASE RADIACION:
 1)- Se le solicita al usuario que ingrese si quiere insertar un mutante de manera horizontal('H') o vertical('V')
 2)- A continuación, se le solicitará que ingrese las posicion horizontal y vertical donde desea empezar el mutante a insertar
 3)- Finalmente, se mostrará el ADN con los mutantes insertados
 CLASE VIRUS:
 1)- Se le solicitará al usuario si quiere insertar un mutante en las diagonales de izquiera a derecha o al reves:

 Izquiera a derecha:                            Derecha a izquierda:
   D D D A A A                                    A A A D D D
   D D D D A A                                    A A D D D D 
   D D D D D A                                    A D D D D D
   A D D D D D  --> D son las diagonales          D D D D D A   ---> D son las diagonales
   A A D D D D                                    D D D D A A
   A A A D D D                                    D D D A A A

   2)- A continuacion, se le solicitará al usuario que ingrese las posiciones donde desea insertar el mutante
   3)- Finalmente, se mostrará el ADN con los mutantes insertados diagonalemente