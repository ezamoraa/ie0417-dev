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

Diagrma de clases de los componentes de eieManager:

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

Diagrma de clases de los componentes de eieDevice:

.. uml::

	@startuml

	title Relationships - Class Diagram (eieManager)


	class EieDevice 

	class TransportServer{
	  +void SendReply()

	}
	class CommandManager{
	  +void RunCommand()

	}
	class Command{
	  +void ImplementFunctionality()

	}

	EieDevice "1" *-down- "1" CommandManager: Composition
	EieDevice "1" *-down- "1" TransportServer: Composition
	CommandManager <|-down- Command: Inheritance
	@endumlDevic

Diagrama de secuencia (El cliente envía un comando a un dispositivo específico):

.. uml ::
	@startuml
	Client -> APIServer: Send Command

	alt successful case

	   APIServer -> TransportClient: Protocol Request
	   
	   alt successful case

	   TransportClient -> APIServer: Protocol Specification 
	   
	   else some kind of failure

	   TransportClient -> APIServer: Protocol Specification Failure
	    end
	   
	   CommandInfo -> APIServer: Command Information Request

	   alt successful case

	   APIServer -> CommandInfo: Command Information
	   
	   else some kind of failure

	   APIServer -> CommandInfo: Command Information Failure
	   end
	 
	   CommandInfo -> CommandRegistry: Command Verification Request

	   alt successful case

	   CommandRegistry -> CommandInvoker: Valid Command
	   
	   else some kind of failure

	   CommandRegistry -> CommandInfo: Invalid Command
	   end
	   
	   CommandInvoker -> DeviceManager: specifies command and device

	   DeviceManager -> Device: Run Command

	    



	else some kind of failure

	    APIServer -> Client: Please repeat

	end
	@enduml

Diagrama de secuencia (El cliente envía un comando a un grupo de broadcast):

.. uml ::
	@startuml
	Client -> APIServer: Send Command

	alt successful case

	   APIServer -> TransportClient: Protocol Request
	   
	   alt successful case

	   TransportClient -> APIServer: Protocol Specification 
	   
	   else some kind of failure

	   TransportClient -> APIServer: Protocol Specification Failure
	    end
	   
	   CommandInfo -> APIServer: Command Information Request

	   alt successful case

	   APIServer -> CommandInfo: Command Information
	   
	   else some kind of failure

	   APIServer -> CommandInfo: Command Information Failure
	   end
	 
	   CommandInfo -> CommandRegistry: Command Verification Request

	   alt successful case

	   CommandRegistry -> CommandInvoker: Valid Command
	   
	   else some kind of failure

	   CommandRegistry -> CommandInfo: Invalid Command
	   end
	   
	   CommandInvoker -> DeviceGroup: specifies command and device

	   DeviceGroup -> Group: Run Command

	    



	else some kind of failure

	    APIServer -> Client: Please repeat

	end
	@enduml




