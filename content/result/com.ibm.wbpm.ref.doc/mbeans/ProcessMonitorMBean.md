ProcessMonitor MBean
IBM Business Process Manager provides a programming interface for accessing process monitor data.

ObjectName: 
com.lombardisoftware:Scope=ENVIRONMENT\_SERVER,Name=ProcessMonitor,cell=[cell],Type=ProcessMonitor,node=[node],process=[server]

 
 MBean ProcessMonitor
Information on the management interface of the MBean
Data retrieved complies to the following schema:

<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema attributeFormDefault="unqualified"
	elementFormDefault="qualified" targetNamespace="http://www.ibm.com/bpm/v1/process\_monitor" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://www.ibm.com/bpm/v1/process\_monitor">
	<xsd:element name="processMonitor" type="tns:processMonitorType" />

	<xsd:complexType name="processMonitorType">
		<xsd:sequence>
			<xsd:element name="process" type="tns:processType" minOccurs="0" maxOccurs="unbounded"/>
			<xsd:element name="service" type="tns:serviceType"  minOccurs="0" maxOccurs="unbounded"/>
		</xsd:sequence>
		<xsd:attribute type="xsd:string" name="server" />
		<xsd:attribute type="xsd:string" name="id" />
		<xsd:attribute type="xsd:boolean" name="showDetails" />
		<xsd:attribute type="xsd:long" name="durationExceededInSeconds" />
		<xsd:attribute type="xsd:long" name="stepExceeded" />
	</xsd:complexType>

	<xsd:complexType name="stepType">
		<xsd:attribute type="xsd:string" name="name"/>
		<xsd:attribute type="xsd:string" name="type"/>
		<xsd:attribute type="xsd:dateTime" name="lastEnterTime" />
		<xsd:attribute type="xsd:string" name="lastDuration"/>
		<xsd:attribute type="xsd:string" name="totalDuration"/>
		<xsd:attribute type="xsd:long" name="steps"/>
	</xsd:complexType>

	<xsd:complexType name="serviceType">
		<xsd:sequence>
			<xsd:element name="step" type="tns:stepType" minOccurs="0" maxOccurs="unbounded"/>
		</xsd:sequence>
		<xsd:attribute type="xsd:string" name="processApplication"/>
		<xsd:attribute type="xsd:string" name="name" />
		<xsd:attribute type="xsd:string" name="state"  />
		<xsd:attribute type="xsd:string" name="contextID"  />
		<xsd:attribute type="xsd:dateTime" name="lastEnterTime"/>
		<xsd:attribute type="xsd:string" name="duration"/>
		<xsd:attribute type="xsd:string" name="lastDuration"/>
		<xsd:attribute type="xsd:string" name="totalDuration"/>
		<xsd:attribute type="xsd:long" name="steps"/>
	</xsd:complexType>

	<xsd:complexType name="processType">
		<xsd:sequence>
			<xsd:element name="step" type="tns:stepType" minOccurs="0" maxOccurs="unbounded"/>
			<xsd:element name="service" type="tns:serviceType" minOccurs="0" maxOccurs="unbounded"/>
		</xsd:sequence>
		<xsd:attribute type="xsd:string" name="processApplication"/>
		<xsd:attribute type="xsd:string" name="name"/>
		<xsd:attribute type="xsd:long" name="instanceID"/>
		<xsd:attribute type="xsd:string" name="state"/>
		<xsd:attribute type="xsd:dateTime" name="lastEnterTime"/>
		<xsd:attribute type="xsd:string" name="totalDuration"/>
		<xsd:attribute type="xsd:long" name="steps"/>
	</xsd:complexType>
</xsd:schema>

Attribute Summary

 java.lang.String
DisplayName

           

 boolean
Monitoring

           

 javax.management.ObjectName
ParentObjectName

           

 

Operation Summary

 void
haltProcess(java.lang.String processInstanceID)

          Attempt to halt running of a process instance.

 void
haltProcessAndAssociatedServices(java.lang.String processInstanceID)

          Attempt to halt running of a process instance.

 void
haltService(java.lang.String serviceContextID)

          Attempt to halt running of a service execution.

 java.lang.String
retrieveMonitorAll()

          Return all process monitor data

 java.lang.String
retrieveMonitorAllAsJSON()

          Return all process monitor data

 java.lang.String
retrieveMonitorByFilter(boolean showDetails,
                        long durationExceededInSeconds,
                        long stepExceeded)

          Return a selected set process monitor data

 java.lang.String
retrieveMonitorByFilterAsJSON(boolean showDetails,
                              long durationExceededInSeconds,
                              long stepExceeded)

          Return a selected set process monitor data

 void
startMonitoring()

           

 void
stopMonitoring()

           

 

Operations inherited from class java.lang.Object

clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait

 

Attribute Detail

Monitoring

public boolean Monitoring

DisplayName

public java.lang.String DisplayName

ParentObjectName

public javax.management.ObjectName ParentObjectName

Operation Detail

startMonitoring

public void startMonitoring()

stopMonitoring

public void stopMonitoring()

retrieveMonitorAll

public java.lang.String retrieveMonitorAll()
                                    throws AdminException

Return all process monitor data

Returns:all process monitor data as XML
Throws:
AdminException

retrieveMonitorByFilter

public java.lang.String retrieveMonitorByFilter(boolean showDetails,
                                                long durationExceededInSeconds,
                                                long stepExceeded)
                                         throws AdminException

Return a selected set process monitor data

Parameters:showDetails - show information about individual steps in process instance/servicedurationExceededInSeconds - only show process instance/service that exceeded a certain time in secondsstepExceeded - only show process instance/service that exceeded a certain steps
Returns:all process monitor data as XML
Throws:
AdminException

retrieveMonitorAllAsJSON

public java.lang.String retrieveMonitorAllAsJSON()
                                          throws AdminException

Return all process monitor data

Returns:all process monitor data as JSON
Throws:
AdminException

retrieveMonitorByFilterAsJSON

public java.lang.String retrieveMonitorByFilterAsJSON(boolean showDetails,
                                                      long durationExceededInSeconds,
                                                      long stepExceeded)
                                               throws AdminException

Return a selected set process monitor data

Parameters:showDetails - show information about individual steps in process instance/servicedurationExceededInSeconds - only show process instance/service that exceeded a certain time in secondsstepExceeded - only show process instance/service that exceeded a certain steps
Returns:all process monitor data as JSON
Throws:
AdminException

haltProcess

public void haltProcess(java.lang.String processInstanceID)
                 throws AdminException

Attempt to halt running of a process instance.  This will fail if the process is not active, or is in the middle of executing a task.

Throws:
AdminException

haltProcessAndAssociatedServices

public void haltProcessAndAssociatedServices(java.lang.String processInstanceID)
                                      throws AdminException

Attempt to halt running of a process instance.  This will fail if the process is not active, or is in the middle of executing a task.

Throws:
AdminException

haltService

public void haltService(java.lang.String serviceContextID)
                 throws AdminException

Attempt to halt running of a service execution.  This will fail if the service is not active, or is in the middle of executing a step.

Throws:
AdminException

Copyright IBM Corp. 2018, 2019.