# Lenguaje SWIFT


## Historia

* El desarrollo de este sistema comenzó en julio de 2010 por Chris Lattener junto con la colaboración de otros programadores de Apple.
Swift se benefició de la experiencia de muchos lenguajes tomando ideas de Objective-C, Haskell, Rust, Ruby, Python, C#, CLU entre otros. 

* En 2014, en el mes de junio la aplicación Apple Worldwide Developers Conference (WWDC) se convirtió en la primera aplicación publicada escrita con este sistema. En septiembre de 2014 swift alcanzó el hito 1.0 con el Gold Master de Xcode 6.0 para iOS.  El Swift 1.1 fue lanzado en octubre de ese mismo año, junto con el lanzamiento de Xcode 6.1. 

* En 2015, swift 1.2 fue lanzado el 8 de abril de 2015, junto con Xcode 6.3. Swift 2.0 se anunció en WWDC 2015 y estuvo disponible para la publicación de aplicaciones en la App Store el 21 de septiembre de 2015. Swift ganó el primer lugar como Lenguaje de programación más querido en la Encuesta para desarrolladores de Stack Overflow este mismo año. 

* En 2016, swift 3.0 se lanzó en septiembre. Durante la WWDC 2016 , Apple anunció una aplicación exclusiva para iPad , llamada Swift Playgrounds , destinada a enseñar a las personas cómo codificar en Swift. La aplicación se presenta en una interfaz similar a un videojuego en 3D que proporciona información cuando las líneas de código se colocan en un orden determinado y se ejecutan.

* En enero de 2017 Chris Lattner anunció su salida de Apple para ocupar un nuevo puesto en Tesla Motors y el papel principal del proyecto Swift recayó en el veterano del equipo Ted Kremenek. Ese mismo año salió la versión swift 4, al año siguiente swift 4.1 y swift 5 fue lanzado en marzo de 2019. 

* Durante la WWDC 2019, Apple anunció SwiftUI, que proporciona un marco para el diseño de la estructura declarativa de la interfaz de usuario en todas las plataformas de Apple. Swift 5.1 se lanzó oficialmente en septiembre de 2019. Swift 5.1 se basa en la versión anterior de Swift 5 al extender las características estables del lenguaje al tiempo de compilación con la introducción de la estabilidad del módulo. La introducción de la estabilidad del módulo permite crear y compartir marcos binarios que funcionarán con futuras versiones de Swift.


## Compilado/interpretado/Hybrido

* Swift es un lenguaje de programación compilado de uso general. 


## Palabras clave

* Al ser un lenguaje mayormente inspirado en C#, su sintaxis es muy similar, al igual que el tratamiento de datos.
Acorde con [Swift’s official docs](https://docs.swift.org/swift-book/ReferenceManual/LexicalStructure.html#:~:text=the%20following%20keywords%20are%20reserved%20and%20can%E2%80%99t%20be%20used%20as%20identifiers), existen seis tipos de palabras reservadas en el lenguaje:
    
    * **Palabras reservadas para declaraciones:** associatedtype, class, deinit, enum, extension, fileprivate, func, import, init, inout, internal, let, open, operator, private, precedencegroup, protocol, public, rethrows, static, struct, subscript, typealias y var

    * **Palabras reservadas para instrucciones:** break, case, catch, continue, default, defer, do, else, fallthrough, for, guard, if, in, repeat, return, throw, switch, where y while

    * **Palabras reservadas para espresiones y tipos:** Any, as, catch, false, is, nil, rethrows, self, Self, super, throw, throws, true y try

    * **Palabras reservadas para patrones:** _

    * **Palabras reservadas que comienzan con un signo numérico:** #available, #colorLiteral, #column, #dsohandle, #elseif, #else, #endif, #error, #fileID, #fileLiteral, #filePath, #file, #function, #if, #imageLiteral, #keyPath, #line, #selector, #sourceLocation y #warning

    * **Palabras reservadas en contextos particulares:** associativity, convenience, didSet, dynamic, final, get, indirect, infix, lazy, left, mutating, none, nonmutating, optional, override, postfix, precedence, prefix, Protocol, required, right, set, some, Type, unowned, weak y willSet 

**Nota: Los siguientes caracteres están reservados como puntuación y no pueden ser utilizados para customizar identificadores: (, ), {, }, [, ], ., ,, :, ;, =, @, #, &, ->, `, ?, and ! (como prefijos)**

**Sin embargo, las palabras reservadas pueden usarse como identificadores poniendo acentos graves (`) antes y después del identificador**


## Sensible a la mayuscula y minuscula

* Es un lenguaje sensible a las mayúsculas y a las minúsculas, al igual que le sucede a otros lenguajes como, por ejemplo, el lenguaje C. 


## Tipado

* Swift es un lenguaje fuertemente tipado, aunque su declaración no siempre es necesaria gracias a su capacidad de inferir tipos. Los tipos de datos se dividen principalmente en dos grupos. Los Tipos de valor y los Tipos por referencia, se diferencian principalmente en como son asignados.


## Cuánto gana un programador de media:

* Programar Swift está asociado con un salario global medio de 57.520€, aunque este aumenta en Estados Unidos donde puede llegar a los $82.472. El salario asociado a este lenguaje es un 19,6% más alto que la media global, ya que busca ser más asequible que las opciones existentes. Por otra parte, un desarrollador de iOS independiente con mucha experiencia puede cobrar hasta $75 por hora (eso es $150.000 al año). En la actualidad, todo profesional que se precie, debe dominarlo para poder trabajar en el desarrollo de cualquier app compatible con iOS.


## Cantidad de personas en la comunidad:

* Al ser Swift un lenguaje joven (nacido en 2014 y convertido por Apple en código abierto al año siguiente), uno diría que su comunidad debería ser pequeña en comparación con otros lenguajes, pero curiosamente no. Solo en el primer año, alrededor de 60.000 personas empezaron a usarlo creciendo exponencialmente hasta competir con otros lenguajes (considerado en el TOP 10 de los lenguajes actuales). Todas sus características hacen de este lenguaje imprescindible para cualquier programador que se precie o aspire a trabajar con iOs, por esto mismo en la actualidad, su comunidad la conforman casi todos los programadores de Apple (por no decir todos) más la de los programadores especializados en otras plataformas para trabajar con la portabilidad de sus programas. 
Para resaltar, Swift tiene una comunidad de código abierto tremendamente activa. Esto propicia que Swift tenga abundantes recursos para ayudar a todos los desarrolladores a aprender y dominar la programación con este sistema.
También tiene un gran conjunto de podcasts, cursos, e incluso juegos Swift con para mejorar y facilitar la experiencia de aprendizaje.


## Influencia de otro lenguaje:

* Swift combina el rendimiento y la eficiencia de los lenguajes compilados con la simplicidad y la interactividad de los lenguajes de scripts populares. Hay que entender que su existencia deriva de la necesidad de mejorar o incluso sustituir lenguajes como Objetive-C. De hecho, no solo lo supera, sino que también se le considera mejor que usar C o C++, en los que también se basa. Por esto, puede usar cualquier biblioteca programada en Objective-C y llamar a funciones de C.


## Plataformas:

* Lo primero que tenemos que entender es que Swift está basado en C, con algunas capas en código binario de las plataformas donde funciona.
Swift es un lenguaje abierto y multiplataforma, eso supone que su compilador y todos sus componentes son capaces de generar código binario ejecutable que cada sistema operativo donde tenga soporte sea capaz de entender. Esto solo sucedía hasta ahora en Linux y los sistemas de Apple, pero ahora ya sucede también en Windows.