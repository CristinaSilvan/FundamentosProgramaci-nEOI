# Módulos

* Al tener que resolver una tarea mediante un algoritmo, es necesario organizar la tarea en diferentes partes
separando la información que vamos a tomar y estructurando las intrucciones de manera coherentes para resolver el problema

* Modular el programa, significa separar el programa en las diferentes partes en las que resolverá el trabajo
    
    * _Una parte se dedica a tomar los datos de entrada, otra parte se dedica a registratlos en una base de datos, otra parte se dedica
    a calcular o comprobar dicha información, otra parte se comunica con los periféricos, etc_

* Ese algoritmo, llama a otros subalgortismos a su vez (funciones, procesos, módulos, librerías, ...) para repartir esas tareas

# Usando Recursividad

* Es una técnica de programación que se dedica a resolver un problema sustituyéndolo por otros problemas de la misma categoría, pero de forma más simple

* Un algoritmo es recursivo si dentro del cuerpo del algoritmo y de forma directa o indirecta se realiza una llamada a él mismo

* Se llama caso base o condición de salida al caso trivial de un algortimo recursivo, del cual conocemos su solución

(**Nota: Todo algoritmo recursivo debe incluir al menos un caso base y garantizar que se ejecute en algún momento para evitar la recursividad infinita**)

* Muchas personas consideran que la recursividad puede ser sustituida por la iteratividad

* En general, tendremos que elegir en qué caso nos combiene aplicar una u otra

* Cuando en una llamada recursiva nos encontramos un **"devolver"**, no es necesario especificar el fin del subalgoritmo ya que en esta misma instrucción termina. Por esto, es importante un caso base que se asegure de devolver cierta información al algoritmo principal, para que no continúe llamándose infinitamente.