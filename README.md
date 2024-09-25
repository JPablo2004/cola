Cola FIFO (First In, First Out)
Este proyecto implementa una estructura de datos cola (FIFO - First In, First Out) utilizando una lista en Python. La cola sigue el principio de que el primer elemento en ingresar es el primero en ser atendido.

Descripción
Este programa simula la atención de personas en una cola. Los elementos son agregados al final de la cola, y son atendidos en el mismo orden en que ingresaron (primero en entrar, primero en salir). Cada vez que se atiende a una persona, se elimina de la cola y se guarda en una lista separada llamada atendidos.

Funcionalidades
Agregar elementos a la cola.
Atender a los elementos en orden.
Guardar los elementos atendidos en una lista separada.
Imprimir el estado de la cola antes y después de ser procesada.
Estructura del Código
Se inicializa una cola con algunos elementos.
Se agregan nuevos elementos al final de la cola usando el método append().
A través de un bucle while, los elementos son eliminados de la cola con el método pop(0), simulando la atención en orden de llegada.
Los nombres atendidos son almacenados en una lista llamada atendidos.
Al finalizar el ciclo, la cola queda vacía y se imprimen los nombres de las personas atendidas.
Cómo usar
Copia el código fuente en tu entorno Python.
Ejecuta el código y observa cómo la cola es procesada en orden.
Puedes modificar la lista cola inicial o agregar más elementos según sea necesario.
Requisitos
Python 3.x
Autor
Juan Pablo Restrepo Alzate

https://youtu.be/L6CXx_nVNf0?feature=shared
