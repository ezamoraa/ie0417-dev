*************
Laboratorio 1
*************

Endpoints
==================

Para lograr que el prototipo cumpla con las operaciones que se desean, se deben de tener los siguientes endpoints.

+-------------+--------------------------+---------------------------+
| HTTP method |   API endpoint           |  Descripción              |
+=============+==========================+===========================+
| |   POST    |     /devices             | Permite crear y registrar |
| |           |                          | dispositivos nuevos.      |
+-------------+--------------------------+---------------------------+
| |    PUT    | /devices/<device_id>     | Permite actualizar un     |       
| |           |                          | dispositivo.              |
+-------------+--------------------------+---------------------------+
| |   GET     |     /devices             | Se obtiene la lista de    |
| |           |                          | dispositivos registrados. |
+-------------+--------------------------+---------------------------+
| | DELETE    | /devices/<device_id>     | Permite eliminar un       |
| |           |                          | dispositivo.              |
+-------------+--------------------------+---------------------------+
| |   GET     | /devices/<device_id>     | Permite obtener la        |
| |           |                          | respuesta de un           |
| |           |                          | disopositivo especifico   |
+-------------+--------------------------+---------------------------+
| |   GET     | /devices/<device_command | Permite obtener commands  |
| |           |                          | y dar una respuesta       |
| |           |                          | mediantea archivo Json    |
+-------------+--------------------------+---------------------------+

Donde se tiene:

* device_id: que va a indicar el id del device con el cual se esta trabajando
* device_command: que es un parámentro que va a recibir el endpoint para lograr obtener la informacion necesaria del servicio de deviceManager y trasladar la informacion por medio de un archivo Json.
