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

- Si escribo copy con <NombreArchivo.Extensión> en la consola, esta me creará un archivo exactamente igual en el que se guardará lo que escriba a continuación (finaliza con Ctrl + Z)

#### **(Escribir el nombre de un fichero o programa en consola, abre el fichero o programa)**
#### **(Se puede pegar en la línea de comandos con clic derecho)**
### **(Algunos comandos requieren permisos de administrador)**



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