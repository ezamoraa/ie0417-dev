*************
Laboratorio 1
*************
**Planeamiento**

De manera breve, explique cómo se pueden planear los releases de funcionalidad del proyecto para habilitar lo más rápido posible el desarrollo en el equipo del App (externo a eieLabs).

Utilice conceptos de planeamiento a largo plazo con metodologías Agile (Quiz 2).

Agile

Paso 1: 

Para iniciar con el proyecto se tiene la idea general de este ultimo: Se tiene un proyecto en el cual se tendrá 
dos secciones importantes el eieManager que se encarga de comunicarse con los dispositivos de la empresa,este eieManager debe
de servir como API es decir,sirve como un intermediario entre los dispositivos a controlar y el cliente,
los dispositivos a controlar como un grupo es el eieDevice el cual debe recibir 
comandos desde el eieManager actuar de acuerdo a estos comandos recibidos y de ser el caso se genera una respuesta al cliente.

Se crearan procesos para construir un eieManager bastante solido,una base comunicacion AP queI en la pueda ser 
fácilmente consumido por otro equipo de desarrollo
para implementar un cliente en un App móvil con GUI.
Paso 2:

Al ser un diseño de software los aspectos de mas valor caerán en la estabilidad y modificabilidad de diseño API aplicado.

Paso 3:

eieManager:
******************** comandos ***********************
*Definir los comandos predefinidos que se enviaran a los eieDevices
*Esquematizar el rango de dispositivos aplicado por cada uno de los comandos
********************* API *****************************
*Iniciar el API bajo un protocolo de comunicacion RPC
*Crear un puente de comunicacion tal que el eieManager pueda recopilar todas las respuestas y se las presente al cliente
*permitir que el funcionamiento del API sea independiente del sistema operativo utilizado y los comandos que transiten por el *cohesion*
*Configurar el API de manera que soporte concurrencia en cantidad de comandos aplicados como la cantidad de dispositivos a los cuales se les envia el comandos
Paso 4:

Estimacion en el tiempo del trabajo
Creacion algoritmo API=
Aumentar adaptabilidad y ancho de banda de API=
Aplicación protocolo comunicacion API=
Diseño de los algoritmos usados por el eieManager=
Manejo de comandos en transmision/recepcion eieManager=
Diseño eieDevices y respuestas=
Definicion de grupos de broadcast =
*Restablecimiento a un punto anterior
Paso 5:

release 1=API
release 2=eieManager
release 3=eieDevice
release 4=proyecto final

Paso 6:

Scope: Un proyecto que permita el manejo de una empresa desde clientes externos,capacidad de trabajar bajo concurrencia y una sumamente adaptable a cambios tanto en software 
como en metodos de conexion
tiempo=?
recursos=?

**Requerimientos**

Los requerimientos funcionales son las acciones esenciales en el software que reciben y procesan las entradas para generar salidas, usualmente los requerimientos funcionales son enunciados como "el sistema deberia..." y deben cumplir los siguientes principios:

a) Correcto;
b) No ambiguo;
c) Completa;
d) consistente;
e) Clasificados por importancia y/o estabilidad;
f) Verificable;
g) Modificable;
h) Rastreable.

Algunos ejemplos son:

A) Verificar la validez de las entradas
B) Llevar una secuencia exacta de las operaciones
C) Tener una respuesta a las situaciones anormales.

Es importante mencionar que estos requerimientos funcionales pueden ser divididos en subprocesos, pero no quiere decir que el software tambien lo hara.

Requerimientos funcionales: 

User class A.3:
Cuando el sistema requiere de usuarios con diferentes privilegios en el software, por ejemplo, un "admin" y un "client", en este caso queremos tener diferentes accesos como el de un cliente y un servidor.

Feature A.5
Se refiere cuando es un deseo exterior por el sistema que puede necesitar entradas (inputs) y afecta al resultado deseado. En el proyecto se usaria dado que el cliente puede dar entradas y modificar la respuesta del administrador. 

Response A.6 
Conjunto de funciones que permite un sistema generar una respuesta deseada, como cuando hay una cuenta de un sistema que tiene que poder acceder a diferentes caracteristicas como, lista de empleados, salarios, horarios y todos los relacionados. En el proyecto constara de un administrador que pueda tener de facil acceso los distintos dispositivos e interactuar con ellos.

No funcionales:
System mode A.1 & A.2
Algunos sistemas necesitan tener diferenes modos de funcioanlidad, por ejemplo, uno en caso de emergencia, o de simulacro, o de entrenamiento. En este caso no se utilizara ningun modo especial en especifico.

Objects A.4
Los objetos son caracteristicas que el sistema puede ofrecer, como por ejemplo, conexion con sensores, bases de datos, entre otros. En este caso no se tiene contacto con atributos de ese indole, entonces no se usara.
Stimulus A.6
Los Stimulus describen diferentes funciones dependiendo del tema, pero en este caso no se utilizaran temas complejos.
Functional Hierarchy A.7
La jerarquia se utiliza cuando ningun de los esquemas organizacionales anteriores no funcionan, entonces las funciones se organizan segun su tipo, o relacion de sus atributos entre si, y no se utilizara dado que algunos de los esquemas mencionados si se utilizaran.


**Patrones de diseño**

Explique cómo se puede aplicar el patrón de diseño Proxy para abstraer la interacción y comunicación con los dispositivos desde eieManager.

Lo primero es definir Proxy como una interfaz funcionando para algún otro software, en este caso de network conection entre los dispositivos y el servidor eieManager. Proxy se utiliza como una clase más de **eieManager** trabajando como un servidor remoto donde la información que viaja desde los computadores conocidos como **eieDevices** llegando a **eieManager**, ejecutando acciones de diseno y enviar ya sea devuelta al dispositivo o ya el **Client**.  

Explique cómo se puede aplicar el patrón de diseño Command para desacoplar los procesos de:

Encapsular la información requerida para ejecutar comandos en dispositivos específicos.
Ejecutar los comandos y esperar la respuesta correspondiente.

Command funciona como un patrón de encapsulamiento, es útil para ejecutar funcionamiento lógico entre clases sin necesidad de revelar información detallada entre ellas. Esto es muy importante dado que puede que el servidor contenga información muy confidencial de proveniente de un **eieDevice** o del **Client** que debe ser ejecutada por otro dispositivo sin la necesidad de revelar datos sensibles. 

**Diagramas UML**

.. uml::
   @startuml

   class eieManager
   class eieDevice
   class ConfigHandler{
      + name
      + broadcastgroup
   }
   class APIServer 
   class CommandRegistry
   class DeviceManager
   class GroupManager
   class CommandInvoker
   class TransportClient
   class TransportServer
   class CommandManager
   class Command

   eieManager --|> ConfigHandler
   eieManager --|> APIServer
   eieManager --|> TransportClient
   eieManager --|> GroupManager
   eieManager --|> DeviceManager
   eieManager --|> CommandRegistry
   CommandRegistry --o CommandInvoker
   DeviceManager -- eieDevice
   CommandInvoker -- CommandManager

   TransportClient --* TransportServer
   eieDevice --|> TransportServer
   eieDevice --|> CommandManager

   CommandManager --* Command

   @enduml
