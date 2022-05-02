*************
Laboratorio 1
*************

Patrones de Diseño
==================

El patrón de diseño proxy funcionaria perfectamente para solucionar el problema de interacción y comunicación debido a que lo que hace es que se convierte en la interfaz de algo que puede ser costoso de almacenar o algo que no se quiere que se pueda duplicar. De forma que utilizando este patrón se puede dar acceso al protocolo de comunicación que se necesita para que se realice de forma adecuada el intercambio de comunicación, así como también se podría instanciar el mensaje de forma local para que pueda ser utilizado por los distintos componentes. Este patrón se puede relacionar a los siguientes componentes:

* Device.
* Group.
* DeviceManager.
* GroupManager.
* TransportClient.



Diagramas UML
=============

Diagrma de clases de los componentes de eieManager
.. uml::

  	@startuml
	title Relationships - Class Diagram (eieManager)


	class EieManager 

	class APIServer{
	  +void ClientRequest()
	}
	class CommandRegistry{
	  +void CheckCommand()
	}
	class CommandInvoker{
	  +void RunCommand()
	}
	class GroupManager{
	  +void ManageGroup()
	}
	class ConfigHandler{
	  +void Configuration()
	}
	class DeviceManager{
	  +viod DeviceLifeCycle()
	}
	class TransportClient{
	  +void CommunicationProtocol()
	}
	class DatabaseHandler{
	  +void StoreData()
	}
	class Device
	class Group
	class CommandInfo{
	  +void ExtractCommandInformation()
	}




	EieManager "1" *-down- "1" ConfigHandler: Composition
	ConfigHandler  <.down-  DeviceManager: Use
	ConfigHandler  <.down-  GroupManager: Use
	APIServer "1" *-down- "1" CommandInfo: Composition
	CommandInfo "1" *-down- "1" CommandRegistry: Composition
	APIServer <|-right- TransportClient: Inheritance
	CommandRegistry "1" *-down- "1" CommandInvoker: Composition
	ConfigHandler <.down- DatabaseHandler: Use
	DeviceManager <|-down- Device: Inheritance
	GroupManager <|-down- Group: Inheritance
	TransportClient "1" *-down- "1" EieManager: Composition
	@enduml


