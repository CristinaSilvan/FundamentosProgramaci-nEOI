# Conceptos básicos
* _Algoritmo_ (Conjunto de instruccione programadas para resolver una tarea específica)
* _Datos_ (una colección de datos que se proporcionan a los algoritmos que se han de ejectar para encontar una solución: los datos se organizarán en estructuras de datos)
* _Objetos_ (el conjunto de datos y algoritmos que los manipulan, encapsulados en un tipo de dato nuevo conocido como objeto)
* _Clases_ (tipos de objetos con igual estado y comportamiento, o dicho de otro modo, los mismos atributos y operaciones)
* _Estructuras de datos_ (conjunto de organizaciones de datos para tratar y manipular eficazmente datos homogéneos y heterogéneos)

# Configuración de una computadora

Una computadora es un dispositivo electrónico utilizado para procesar información y obtener resultados. Los componentes físicos que constituyen la computadora, junto con los dispositivos que realizan las tareas de entrada y salida, se conocen con el término _hardware_. En su configuración física más básica una computadora está constituida por una **Unidad Central de Procesamiento (CPU)**, una **Memoria principal** y unas **Unidades de Entrada/Salida** o **periféricos**. Las funciones desempeñadas por cada una de estas partes son las siguientes: 
* Las **Unidades de Entrada/Salida** (Input/Output o I/O) se encargan de los intercambios de información con el esterior.
* La **Memoria principal** almacena tanto las instrucciones que constituyen los programas como los datos y resultados obtenidos; para que un programa se ejecute, tanto él como sus datos, se deben situar en memoria central. Sin embargo, la información almacenada en la memoria principal se pierde cuando se desconecta la computadora de la red eléctrica y, además, dicha memoria es limitada en capacidad. Por estas razones, los programas y datos necesitan ser transferidos a **dispositivos de almacenamiento secundario**, que son dispositivos periéfirocs que actúan como medio de soporte permanente (**Ej: disco duro**). 
La **memoria caché** es una memoria intermedia, de acceso aleatorio muy rápido entre la CPU y la memoria principal, que almacena los datos extraídos más frecuentemente de la memoria principal.
* La **CPU** es la encargada de la ejecución de los programas almacenados en memoria. La CPU consta de **Unidad de Control (CU)**, que se encarga de ejecutar las instrucciones, y la **Unidad aritmético lógica (ALU)**, que efectúa las operaciones.

El **bus del sistema** es una ruta eléctrica de múltiples líneas (clasificables como líneas de direcciones, datos y control) que conecta con la CPU, la memoria y los dispositivos I/O. Los dispositivos I/O son heterogéneos y de características muy variadas; por esta razón cada dispositivo o grupo de ellos cuenta con **controladores** específicos que admiten órdenes e instrucciones muy abstractas que les puede enviar a la CPU y se encargan de llevarlas a cabo generando microórdenes para gobernar los periféricos y liberando la CPU de estas tareas: en síntesis, un **controlador** es un programa que enlaza un dispositivo de la computadora y el sistema operativo que controla la misma. Los dispositivos I/O pueden producir **interrupciones**, que son sucesos que se producen inesperadamente pero a los que generalmente se debe atender inmediatamente, por lo que la CPU abandona momentáneamente las tareas que estaba ejecutando para atender a la interrupción.

En cuanto a las operaciones que debe realizar el **hardware**, éstas son especificadas por una lista de instrucciones, llamadas programas o **software**. El software se divide en dos grandes grupos: **software del sistema** y **software de aplicaciones**.
    
* El **software del sistema** es el conjunto de programas indispensables para que la máquina funcione
* El **sofware de aplicaciones** realizaría tareas concretas así como nóminas, contabilidad, análisis estadístico, etc

# Lenguajes de programación
Un programa se escribe en un lenguaje de programación y estos se pueden clasificar en:
* Lenguaje máquina: proporcionan instrucciones específicas para un determinado tipo de hardware y son directamente inteligibles por la máquina

* Lenguaje de bajo nivel: se caracteriza porque sus instruccciones son mucho más sencillas de recordar, aunque dependen del tipo de computadora y necesitan ser traducidas a lenguaje máquina por un programa al que se le denomina **ensamblador**

* Lenguaje de alto nivel: proporcionan sentencias muy fáciles de recordar, que no dependen del tipo de computadora y han de traducirse a lenguaje máquina por programas denominados como **compiladores** o **intérpretes**. Los programas escritos en un lenguaje de alto nivel se llaman **código fuente** y el programa traducido, **programa objeto** o **código objeto**

# Datos

Dato es la expresión general que describe objetos con los cuales opera el algoritmo. El tipo de un dato determina su forma de almacenamiento en memoria y las operaciones que van a poder ser efectuadas con él. En principio hay que tener en cuenta que, prácticamente cualquier lenguaje y por tanto cualquier algoritmo, se podrán usar datos de los siguientes tipos:

* Entero: Subconjunto finito de los números enteros, cuyo rango o tamaño dependerá del lenguaje en el que posteriormente codifiquemos el algoritmo y de la computadora utilizada.

* Real: Subconjunto de los números reales limitado no sólo en cuanto a tamaño, sino también en cuanto a la precisión

* Lógico: Conjunto formado por los valores verdad y falso

* Carácter: Conjunto finito y ordenado de los caracteres que la computadora reconoce

* Cadena: Los datos (objetos) de este tipo contendrán una serie finita de caracteres, que podrán ser directamente traídos o enviados a/desde la consola

Es decir, los tipos entero, real, carácter, cadena y lógico son **_tipos predefinidos_** en la mayoría de lenguajes de programación. En los algoritmos para indicar que un dato es de uno de estos tipos se declarará utilizando directamente el identificador o nombre del tipo (**palabra reservada**)

Además los lenguajes permiten al programador definir sus propios tipos de datos, los cuales pueden venir expresados con constantes, variables, expresiones o funciones.

# Constantes

Son datos cuyo valor no cambia durante todo el desarrollo del algoritmo. Las constantes