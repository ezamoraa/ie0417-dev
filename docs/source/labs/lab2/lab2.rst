*************
Laboratorio 2
*************

**Explicación general del diseño y del Endpoint**
================
En este laboratorio se implementara una parte del eiemanager en el cual existe un archivo llamado devices.json que guarda la
información de los dispositivos, tanto de su nombre, como el tipo que son. también existe un archivo init que hacer que la 
carpeta se comporte como un módulo, y este almacena el módulo de punto de entrada, con la información del autor, email, y
versión, luego un archivo llamado Command.py que abarca el comando ABC, el command runner, y los hilos para alivianar la carga del servidor API cuando se procesan los comandos. 
En la carpeta
config se encuentra un archivo llamado devices.json que da como ejemplos algunos dispositivos con su respectivo identificador,
nombre, tipo, comando e ip. En la carpeta device se encuentra un archivo llamado device.py que es donde se declaran los 
parámetros que caracterizan a los dispositivos, por medio de funciones que contienen el nombre, el tipo, entre otros.
Dentro de la carpeta eie_commands, device, se encuentra el archivo DeviceManager.py, el cual administra el control de los 
dispositivos y contiene un init general, que inicializa los dispositivos dependiendo de su tipo haciendo un mapa del diccionario
Un init config que invoca la lista de dispositivos del archivo .json, hay otro que invoca su tipo y nombre para organizarlos 
en una lista, también dentro de la carpeta Device existe un archivo llamado computers.py el cual se conecta con el device y
tiene una clase que tiene el nombre y lista de los dispositivos. 
En el branch de API, se encuentran tres archivos: basic_rest_server.py, el cual usa FAST API y se conecta con el archivo de devices.json para cargar la información de los dispositivos, y provee varias funciones, las cuales una crea y registra un nuevo dispositivo y retorna el mismo, un identificador que permite eliminar los objetos, y poder obtener la información de un dispositivo en específico. El archivo basic_rest_client.py contiene una funcion main que asigna los URL para los dispositivos, también contiene una función que imprime todos los dispositivos, o algunos dependiendo de sus características, y otra que crea un nuevo dispositivo e imprime la lista, obtiene un dispositivos específico, o elimina un dispositivo e imprime la lista, todo esto conectándose con el archivo de lista de dispositivos invocandola. Por último se encuentra el archivo devices.json que contiene los dispositivos registrados separados por un nombre clave que es el que los conecta con las otras clases y módulos.

REST en API
""""""""""""

Dado la sencillez y confiabilidad de la arquitectura de tipo REST, se utilizó la misma para restringir el HTTP API y esta es una serie de reglas para definir cómo las aplicaciones o dispositivos se conectan y comunican entre sí, y para esto, el código debe cumplir con las restricciones cómo: una interfaz uniforme, el admin y el cliente deben de ser independientes entre sí, el sistema está compuesto por capas para mayor legibilidad del código y modularidad. 

DocStrings
"""""""""""

Es importante mencionar que en el código se utilizó docStrings para la documentación de las clases, funciones, módulos y métodos, para esto, se sabe que en docStrings en una línea se debe comenzar con una letra mayúscula y terminar con un punto. La primera línea cumple que debe tener una breve descripción. Si hay más líneas en el docString, la segunda línea debe estar en blanco, separando visualmente el resumen del resto de la descripción. Las siguientes líneas deben ser uno o más párrafos que describan las convenciones de llamada del objeto, sus efectos secundarios, entre otros.


Device
"""""""
Para los dispositivos, cómo mencionado en la explicación general, almacena el identificador del dispositivo único, su nombre, comandos de nombres soportados y la información IP, estos dispositivos el sistema será capaz de actualizar la información de los dispositivos a pesar de ya estar registrado, obtener la información de los demás dispositivos registrados o de uno especifico, eliminar un dispositivo y enviar comandos específicos a dispositivos por medio de los request de las demás funciones y clases del API.

.JSON
""""""
En estos archivos, se encuentran listas predefinidas de dispositivos, los cuales se organizan cómo una lista de diccionarios tienen la información necesaria para crear las instancias iniciales, el API tendrá acceso a crear y destruir los dispositivos de una manera dinámica.
