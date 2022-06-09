# Mis notas de la materia de Python I

__Nombre:__ Natalia Gutiérrez Ponce

*Fecha:* 03/02/2022

## Tema: Markdown



### ¿Qué es Markdown?

- Lenguaje de marcado
- Basado en texto plano
- Fácil de exportar a otros formatos



Ejemplo de marcado de código:

``int nombre() ;``

```
///esto es un bloque de código
var x=1;
```



Links:

Aquí puedes consultar el sitio de la [LCG](https://www.lcg.unam.mx/)

<https://www.lcg.unam.mx/>



Imágenes:

![]()

Haciendo uso de HTML podemos manipular el tamaño de la imagen:

<img src="./img/logo_lcg.png" width="120" height="50" />



Tabla:

|  Formato  | Etiqueta |
| :-------: | -------- |
|  Título   | `#`      |
| Subtítulo | `##`     |



## Git

*10, 17 y 24 de febrero de 2022*

### Introducción

#### ¿Qué queremos lograr con el desarrollo de un software?

Es importante saber cuál es el problema a resolver. Debemos codificar de tal manera que si se lo pasamos a a alguien más, esa persona pueda continuar trabajando con nuestro código sin ningún problema.

#### ¿Cómo lograrlo?

Hay estándares que son básicos para escribir código, lo cual permite codificar de una manera adecuada.

- Usar estándares de codificación.
  - Para Python se usa PEP8 para Python.
- Usar notaciones o estándares de nombrado.
  - Camel case.
  - Upper case.
- Buenas prácticas.
- Control de versiones de código.

Al desarrollar software buscamos:

- Resolver problemas.
- Que el código pueda ser utilizado por más personas
- Que el código pueda entenderse y modificarse fácilmente.

La solución debe tener prácticas y características que permitan recordar o que otras personas lo entiendan

### Buenas prácticas

Se basa en lineamientos que usan muchos programadores alrededor del mundo.

- Encabezado de programas.
- Documentación interna. Pocas líneas que nos ayuden a recordar con palabras claves lo que hace una línea de código.
- Nombres adecuados de variables y métodos/funciones.
- Nombre adecuado de programas.
- Organización del código.
- Retroalimentación.

Debemos tener un control (automatizado o manual) de las versiones, lo cual sirve para identificar lo que fue cambiando en un documento de código.

#### Control de versiones

##### Forma manual

El versionamiento está constituido por dos dígitos, versiones primarias y secundarias (X.Y). Cada quien decide cómo versionar sus documentos.

v1.8 major y minor

minor es para cambios menores

###### Reglas

- Major
- Minor
- Ejemplo: myScript_v0.1.py

##### Forma automática

Se hace por medio de un sistema de control de versiones.

Ejemplos:

- Git

#### ¿Qué es un sistema de control de versiones?

- Herramienta encargada de controlar todos los cambios realizados en los programas, creando deferentes versiones de nuestros archivos.
- Commit: es un registro de un cambio de interés.
- Los controladores existen desde inicios de 1980.

#### ¿Para qué?

- Se conserva toda la historia de los cambios en nuestro código.
- Permite que varias personas trabajen en paralelo.

### ¿Qué es Git?

Git es un sistema de control de versiones que permite el trabajo colaborativo.

#### Git de manera local

- Acceso sólo desde el dispositivo (privado)
- Control desde computadora
- Uso personal

#### Git + GitHub

- Trabajar conjuntamente
- Comunidad por un fin común
- Contribución para mejoras
- Acceso de otras personas al código sin afectarlo

#### Trabajar con Git

1. Instalar y configurar
2. Esquema de trabajo
3. Crear un repositorio
4. Inicializar el repositorio
5. Crear un programa y agregarlo a Git
6. Commit
7. Explorar el historial
8. Comparar archivos
9. Ignorar archivos por elección propia

### Comandos importantes

`git --version` Devuelve la versión de Git instalada

`git config --global user.name "[TuNombre]"` Sirve para configurar el nombre de usuario en Git

### Esquema de trabajo

Git no controla todo lo que se almacene en el repositorio Git, por lo que hay que indicarle que lo haga usando `git add`, con lo que empezará a preparar almacenando temporalmente los cambios, y cuando le indiquemos que confirme esos cambios usamos `git commit`

**Repositorio:** Carpeta que contiene el seguimiento de los cambios que se realicen en el código.

### Crear un repositorio

1. Definir la ruta de trabajo
2. Crear una carpeta
3. Entrar a la carpeta
4. Crear la estructura interna

#### Buenas prácticas

Seguir una estructura de organización de carpetas y archivos para proyectos.

- docs
- lib
- src
- test

**Importante:** ¡No meterse con .git! Es importante para que el repositorio esté controlado por Git, el controlador de versiones.

`git init` Sirve para inicializar el repositorio

`git add` Sirve para que agregar cambios hechos al código

`git commit -m "Mensaje"` Sirve para confirmar los cambios realizados

### Mensaje para el commit

Escribir un mensaje que describa con precisión los cambios que se han realizado. Alrededor de 50 caracteres.

### Ramas de Git

La rama **master** es la empleada por defecto en Git.

Git permite hacer referencia a los commits a través de cabeceras. Si se quiere hacer referencia a un commit se puede hacer por medio del identificador o de la cabecera. El commit más reciente se encuentra hasta arriba, por lo que es el HEAD. El segundo más reciente será el HEAD~1, el tercero el HEAD~2, y así sucesivamente.

### Restaurar una versión

Para restaurar una versión usamos `git checkout [HEAD|IdCommit] [file]`

```
git log
git log -N
git log --oneline
git diff HEAD~#
```

### Ignorar archivos

El archivo **.gitignore** le indica a Git cuáles son los archivos que debe ignorar.



## GitHub

*24 de febrero y 3 de marzo de 2022*

GitHub es una plataforma web que permite alojar proyectos basados en Git, haciendo

### GitHub Desktop

GitHub Desktop es la interfaz gráfica de GitHub, que permite la interacción con la plataforma desde nuestra plataforma.

### Comandos importantes para GitHub

`pull` baja información y `push` la sube

`git credential-oskeychain erase` borra las credenciales previas.

Se usan casos de uso para describir los problemas.

### Consejos para documentación de código

- Usar estándar PEP8
- No escribir "código spaghetti o repetir"
  - Refactorizar
- Comentar el código, iniciando con un encabezado
  - TITLE
  - VERSION
  - AUTHOR
  - DESCRIPTION
  - CATHEGORY
  - USAGE
  - ARGUMENTS
- La primera versión que se sube a GitHub debe tener el algoritmo de lo que se desea hacer sin codificar.



## Introducción a Python

*10 de marzo de 2022*

Python es un lenguaje interpretado, por lo que lee las instrucciones y las ejecuta en tiempo real.

### Filosofía de Python

Se espera que podamos entender el código de cualquier persona, y que cualquier persona pueda entender nuestro código, es decir, se busca que sea legible para los humanos. Python fue creado por Guido van Rossum buscando desarrollar un lenguaje más sencillo para los programadores. Los principales objetivos al crear Python eran un lenguaje amigable.

### Versiones de Python

No son recomendables las versiones beta.

Es preferible usar Python 3 porque tiene soporte por parte del equipo de desarrollo, sólo usamos Python 2 cuando el programa ya estaba hecho en Python 2 y es complicado pasarlo a Python 3

#### Números y sus operadores

Python sirve como una calculadora

#### Strings

Son cadenas de caracteres y pueden estar encerradas entre comillas simples ('...') o comillas dobles ("...")

En Python, cada dato en un programa es un objeto.

- Dato es un valor

  - Enteros
  - Flotantes
  - Cadenas

- Objeto tiene

  - Identificador
  - Tipo
  - Valor

- Funcionalidades por tipo de objeto definidas por Python: métodos

- Funciones no están vinculadas a objetos

- Input: Dar una variable

  - input(): Ingresar un valor
  - open(): Lee archivos
  - Argumentos: Pasar argumentos por medio de la línea de comandos

  ```
  dna = input('Dame una secuencia de DNA:\n')
  print(dna)
  ```



## Condicionales

*7 de abril de 2022*

### Tipos de datos lógicos o booleanos

Una variable o dato booleano sólo puede tomar como valores `True` o `False`.

En Python cualquier variable puede considerarse como booleana.

### Operadores lógicos

Son operaciones que trabajan con valores booleanos.

- and
- or
- not

### True y False

No son *strings* y no requieren comillas.

```
print(True)
print(False)
```

### Operadores para True y False

Estos operadores evalúan una condición y regresan True o False:

- Igualdad ==
- Menor o mayor que < o >
- No igual a !=
- Prueba si un valor está en una lista `in`

### Sentencia `if`

La forma más simple de una sentencia condicional es usando `if`. Requiere evaluar una condición.

La sintaxis es:

```
if <expr>:
    <statement>
```

#### `if` dentro de loops

Se puede evaluar toda una lista usando `for` e `if`.

### Diferencias entre `is` e `==`

Para comparar valores se usa `==`

### Sentencia `elif`

```
file1 = open()
file2
file3
for accession in accs:
    if accession.startswitc
```

## Desarrollo de software y errores

Hay diferentes tipos de errores:

- Sintaxis
- Lógicos
- De tiempo de ejecución



## Interfaz de línea de comandos (CLI)

Software o herramientas cuya interfaz deinteracción con el usuario es la línea de comandos.

### Herramientas de interfaz de línea de comandos (CLI)

La ventaja de la línea de comandos contra interfaz gráfica es la **productividad**.

```
reverse complement dna.seq | cut -c1-50
```

Dado que Python es muy popular, se ha vuelto muy utilizado para crear herramientas de línea de comandos.

### Argumentos de la línea de comandos en Python

Los **argumentos** son valores que se pueden utilizar dentro del programa y que son especificados en la terminal desde la línea de comando, y van después del nombre del programa.

### Ayuda (--help)

Podemos decirle al usuario lo que hace falta usando `if`. Ejemplo: imprimir los archivos de un `dir os.listdir("data/")`.

```
import os
import sys

if len(sys.argv) < 2:
    print("You need to specify the path to be listed")
```



### Utilizando `argparse`

*5 de mayo de 2022*

Se debe checar que se cuente con la paquetería necesaria.

#### NameSpace

Un NameSpace es una colección aislada de nombres o identificadores que hacen referencia a objetos. Todas las variables que de



## Programación modular

*19 de mayo de 2022*

### ¿Qué es la programación modular?

La programación modular es un paradigma de programación que consiste en dividir un programa en módulos o subprogramas con el fin de hacerlo más legible y manejable.

Algunas de sus ventajas son:

- Simplicidad
- Facilidad de mantenimiento
- Reusabilidad

### Módulos

Los módulos son bloques de código con funciones y clases. Tienen extensión `.py` y sirven para realizar tareas comunes.

Los módulos pueden escribirse en Python o en C, y se cargan utilizando `import`.



## Expresiones regulares

*26 de mayo de 2022*

### Patrones

Un patrón es una regularidad, una sucesión de elementos que se construye siguiendo una **regla** (repetición o recurrencia) al observar las regularidades.

### ¿Qué es una expresión regular?

Una expresión regular, *regex* o *regexp*, es una secuencia de caracteres que conforma un patrón de búsqueda, y se usan para encontrar una combinación determinada de caracteres en una cadena de texto.

### Uso de expresiones regulares en Python

Para usar expresiones regulares en Python, se utiliza el módulo `re`.

Para buscar un patrón en un *string*, se utiliza `search` de la siguiente manera:

```
re.search(pattern, string, flags)
```





