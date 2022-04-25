# **Conceptos**
- **_Repositorio local_** (archivos en mi hardware)
- **_Repositorio remoto_** (archivos en la nube (_GitHub_))
- **_Ruta absluta_** (dirección exacta del archivo en mi _hardware_ desde el disco en el que se encuentra) **Ej. "C:\00-EOI\Apuntes\Semana_1\Documento.pdf"**
- **_Ruta relativa_** (dirección desde la _carpeta_ en la que me encuentro) **Ej. "\Semana_1\Documento.pdf"**
- **_Stage_** (estado de espera en el que entran los archivos del repositorio local una vez ejecuto _git add_ hasta que guardo con _git commit_ para posteriormente conectar con el repositorio remoto)



# **Comandos básicos de Windows (Win + R / cmd)**
## **(El tabulador se utiliza para autocompletar)**
### **(Las flechas del teclado para navegar)**
- cd (_cargar ruta especificada_)

- cd . (_ruta actual_)

- cd .. (_retroceder en la ruta actual_)

- cd /.. (_ir hasta la raíz, el disco duro_) **Ej. "C:"**

- md (_crear archivo_)

- mkdir (_crear una carpeta_)

- rm (_borrar archivo_)

- rmdir (_borrar carpeta_ (_no funciona si la carpeta contiene archivos_))

- dir (_lista de las carpetas y archivos dentro de mi ruta actual con su información respectiva_)

- /a (_mostrar archivos ocultos_)

- cls (_limpiar la consola_)

- C: D: E: ... (_para cambiar ruta a otro disco_)

- exit (_para cerrar_) 

- (_Tocar la tecla Q para matar un proceso_)

- **C:\Users\Cristina>**  (_Prompt del sistema por defecto_)

- type <_archivo.extension_> muestra el contenido

- echo " " >> <_archivo.extension_> escribe la cadena en el archivo (si no existe el fichero, lo crea)

- Si escribo copy con <NombreArchivo.Extensión> en la consola, esta me creará un archivo exactamente igual en el que se guardará lo que escriba a continuación (finaliza con Ctrl + Z) (Si vuelvo a escribir **copy con** con ese mismo archivo, lo sobreescribe)

#### **(Escribir el nombre de un fichero o programa en consola, abre el fichero o programa)**
#### **(Se puede pegar en la línea de comandos con clic derecho)**
### **(Algunos comandos requieren permisos de administrador)**

# **Trucos consola Windows**
- F1: Vuelve a escribir el último comando utilizado, carácter por carácter por pulsación.
- F2: Pregunta por un carácter, luego vuelve a escribir el último comando utilizado hasta la primera aparición de ese caracter.
- F3: Vuelve a escribir completamente el último comando utilizado.
- F4: Solicita un carácter, luego borra todos los caracteres en el comando actual, comenzando desde la posición del cursor hasta la primera aparición del carácter solicitado.
- F5: Vuelve a escribir completamente los comandos utilizados anteriormente, pero no se activa.
- F6: Tipos ^ Z en el comando actual.
- F7: Presenta un menú de comandos utilizados anteriormente.
- F8: Reescribe completamente los comandos usados ??anteriormente.
- F9: Vuelve a escribir completamente un comando utilizado previamente, que corresponde al número en el menú presentado por F7.


# **Comandos básicos de Git**

- git init (_convertir carpeta actual en repositorio local_)

- git config (_información sobre comandos_)

- git branch (_ver las ramas del repositorio_)

- git switch (_cambiar de rama agregando el nombre_)

- git status (_ver información del repositorio actual_)

- git checkout -- . (_los archivos se reestablecen a la última actualización del "stage", por si necesito recuperarlos, inclusive archivos borrados_)

- git log (_listado de todos los comits_)

- git commit --amend (_modificar último commit_)

- git checkout -b (_crear nueva rama agregando su nombre al lado del comando_)

- git checkout master (_cambiar a la rama master_ (_o a la que escriba_))

- git merge (_junto al nombre de la rama, para unir sus archivos a la actual rama_)

- git branch -d (_junto al nombre de la rama para borrarla_)

- git push (_subir el estado del "stage" a la nube_)

- git pull (_cargar el estado del remoto al local_)

- git commit -am (_git add y git commit simultaneamente, se puede agregar un mensaje_)

- git restore (_deshacer cambios en el stage_)

- (**NOTA: Establecer la conexión desde origin ahorra problemas**)
    - git remote add origin **_enlace repositorio_**

## Fetch significa importar desde remoto
## Push significa exportar a remoto


# **Modo de conectar el Git con GitHub**
## **(Una vez instalado propiamente el Git)**

- git config --global user.name " ...  " (_el nick entre comillas_)

- git config --global user.email " ... " (_el email de GitHub entre comillas_)

- git config --global -l (_comprobar usuario_)



# **Conectar repositorio remoto con repositorio local**
## **(Copiar el link del repositorio de la nube)**

- git remote add main ... (_link del repositorio_)
(_alternativa origin en vez de main_)

- git remote -v (_comprobar conexión con repositorio_)

(**NOTA IMPORTANTE: Si al crear el repositorio, creamos el README.md, habrá un error de sincronización al no estar ese archivo en nuestro repositorio local y habrá que hacer un git pull antes del push**)

(**Otra alternativa en caso de que de error por esto mismo, es escribir git clone <_link repositorio_>**)

- git push main (_conectar_)


# **Actualizar archivos en repositorio remoto**
## **(Una vez el repositorio local haya sido modificado)**

- git add . (_añadir los cambios de la carpeta actual_ (_"git reset ." revierte los cambios del "stage"_))

- git status (_opcional para comprobar cambios_)

- git commit -m " ... " (_nombre de la actualización o descripción_) (**_git commit se puede usar sin agregar título y sirve para guardar el "stage"_**)

- git push main (_completar actualización_)

- git status (_comprobar que se ha realizado_)


# **Borrar conexión con repositorio remoto**

- git remote rm main

# **Sincronicar si el remoto no está coordenado**

- git branch --set-upstream-to=origin/main main

# **Solución al error sobre unrelated histories**

- git pull --allow-unrelated-histories