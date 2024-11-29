InstrumentationManager MBean
IBM Business Process Manager provides a programming interface for accessing instrumentation data. To view the instrumentation data, follow the procedure for accessing the Instrumentation monitor and displaying the most recent data, as described in the topic Capturing process instrumentation data.

ObjectName (for Performance Data Warehouse): 
com.lombardisoftware:Scope=ENVIRONMENT\_PERFORMANCE\_SERVER,Name=InstrumentationManager,cell=[cell],Type=InstrumentationManager,node=[node],process=[server]
 
ObjectName (for Process Server): 
com.lombardisoftware:Scope=ENVIRONMENT\_SERVER,Name=InstrumentationManager,cell=[cell],Type=InstrumentationManager,node=[node],process=[server]

 
 MBean InstrumentationManager
The MBean interface to the instrumentation manager.
Data retrieved complies to the following schema:

<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://www.ibm.com/bpm/v1/instrumentations" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://www.ibm.com/bpm/v1/instrumentations">
	<xsd:element name="instrumentations" type="tns:instrumentationType">
	</xsd:element>

	<xsd:complexType name="instrumentationType">
		<xsd:sequence>		
			<xsd:element name="logFilePath" type="xsd:string" maxOccurs="1" minOccurs="0" />
			<xsd:element name="inst" maxOccurs="unbounded" minOccurs="0" type="tns:instType"/>
		</xsd:sequence>
		<xsd:attribute type="xsd:boolean" name="isLogging" />
		<xsd:attribute type="xsd:string" name="server" />
		<xsd:attribute type="xsd:string" name="id" />

	</xsd:complexType>

	<xsd:complexType name="instType" mixed="true">
		<xsd:sequence>
			<xsd:element type="xsd:string" name="description" minOccurs="0"/>
			<xsd:element type="xsd:string" name="description-key" minOccurs="0" />
			<xsd:element type="xsd:long" name="value" minOccurs="0" />
			<xsd:element type="xsd:long" name="count" minOccurs="0" />
			<xsd:element type="xsd:int" name="inProcess" minOccurs="0" />
			<xsd:element type="xsd:decimal" name="averageDuration" minOccurs="0" />
			<xsd:element type="xsd:decimal" name="movingAverageDuration" minOccurs="0" />
			<xsd:element type="xsd:decimal" name="total" minOccurs="0" />
		</xsd:sequence>
		<xsd:attribute type="xsd:string" name="name" />
		<xsd:attribute type="xsd:string" name="id" />
		<xsd:attribute type="xsd:string" name="type" />
		<xsd:attribute type="xsd:int" name="depth" />
	</xsd:complexType>

</xsd:schema>

Attribute Summary

 java.lang.String
DisplayName

           

 java.lang.String
LogFilePath

          Return the path to the current log file

 boolean
Logging

          Returns true if the manager is currently logging.

 javax.management.ObjectName
ParentObjectName

          Provides support for a parent/child structure over the beans

 

Operation Summary

 java.lang.String
retrieveInstrumentationAll()

          Return the set of instrumentation data as XML

 java.lang.String
retrieveInstrumentationAllAsJSON()

          Return the set of instrumentation data as JSON

 java.lang.String
retrieveInstrumentationByFilter(boolean showVisibleOnly)

          Return a selected set set of instrumentation data as XML

 java.lang.String
retrieveInstrumentationByFilterAsJSON(boolean showVisibleOnly)

          Return a selected set set of instrumentation data as JSON

 void
startLogging()

          Start logging to a new log file.

 void
stopLogging()

          If currently logging stop, otherwise do nothing.

 

Attribute Detail

Logging

public boolean Logging

Returns true if the manager is currently logging.

LogFilePath

public java.lang.String LogFilePath

Return the path to the current log file

DisplayName

public java.lang.String DisplayName

ParentObjectName

public javax.management.ObjectName ParentObjectName

Provides support for a parent/child structure over the beans

Operation Detail

startLogging

public void startLogging()

Start logging to a new log file. If currently logging close the exisitng file and open a new one.

stopLogging

public void stopLogging()

If currently logging stop, otherwise do nothing.

retrieveInstrumentationByFilter

public java.lang.String retrieveInstrumentationByFilter(boolean showVisibleOnly)
                                                 throws AdminException

Return a selected set set of instrumentation data as XML

Parameters:showVisibleOnly - show user visible instrumentations only (only instrumentations seen in Process Admin)
Returns:the set of instrumentation data as XML
Throws:
AdminException

retrieveInstrumentationAll

public java.lang.String retrieveInstrumentationAll()
                                            throws AdminException

Return the set of instrumentation data as XML

Returns:the set of instrumentation data as XML
Throws:
AdminException

retrieveInstrumentationByFilterAsJSON

public java.lang.String retrieveInstrumentationByFilterAsJSON(boolean showVisibleOnly)
                                                       throws AdminException

Return a selected set set of instrumentation data as JSON

Parameters:showVisibleOnly - show user visible instrumentations only (only instrumentations seen in Process Admin)
Returns:the set of instrumentation data as JSON
Throws:
AdminException

retrieveInstrumentationAllAsJSON

public java.lang.String retrieveInstrumentationAllAsJSON()
                                                  throws AdminException

Return the set of instrumentation data as JSON

Returns:the set of instrumentation data as JSON
Throws:
AdminException

Copyright IBM Corp. 2018, 2019.