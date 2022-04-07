# **Conceptos**
- **_Repositorio local_** (archivos en mi hardware)
- **_Repositorio remoto_** (archivos en la nube (_GitHub_))
- **_Ruta absluta_** (dirección exacta del archivo en mi _hardware_ desde el disco en el que se encuentra)
- **_Ruta relativa_** ()
- **_Stage_** (estado de espera en el que entran los archivos del repositorio local una vez ejecuto _git add_ hasta que guardo con _git commit_ para posteriormente conectar con el repositorio remoto)



# **Comandos básicos de Windows (Win + R / cmd)**
## **(El tabulador se utiliza para autocompletar)**
### **(Las flechas del teclado para navegar)**
- cd

- md

- rm

- dir

- /a

- cls

- (Tocar la tecla Q para matar un proceso)

# **Comandos básicos de Git**

- git init (_convertir carpeta actual en repositorio local_)

- git config (_información sobre comandos_)

- git branch (_ver las ramas del repositorio_)

- git status (_ver información del repositorio actual_)

- git checkout -- . (_los archivos se reestablecen a la última actualización del "stage", por si necesito recuperarlos, inclusive archivos borrados_)

- git log (_listado de todos los comits_)

- git commit --amend (_modificar último commit_)

- git checkout -b (_crear nueva rama agregando su nombre al lado del comando_)

- git checkout master (_cambiar a la rama master_ (_o a la que escriba_))

- git merge (_junto al nombre de la rama, para unir sus archivos a la actual rama_)

- git branch -d (_junto al nombre de la rama para borrarla_)

- git push (_subir el estado del "stage" a la nube_)

- git commit -am (_git add y git commit simultaneamente, se puede agregar un mensaje_)

# **Modo de conectar el Git con GitHub**
## **(Una vez instalado propiamente el Git)**

- git config --global user.name " ...  " (_el nick entre comillas_)

- git config --global user.email " ... " (_el email de GitHub entre comillas_)

- git config --global -l (_comprobar usuario_)



# **Conectar repositorio remoto con repositorio local**
## **(Copiar el link del repositorio de la nube)**

- git remote add main ... (_link del repositorio_)

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