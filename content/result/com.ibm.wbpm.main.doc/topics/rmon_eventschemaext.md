# Event schema extensions

## Monitoring events schema (MonitorEvents.xsd)

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema
        targetNamespace="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
        xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
        xmlns:xs="http://www.w3.org/2001/XMLSchema" 
        elementFormDefault="qualified" attributeFormDefault="qualified" version="2010-12-16">

    <xs:element name="monitorEvent">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="mon:eventPointData"/>
                <xs:element ref="mon:applicationData" minOccurs="0"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:string" use="optional"/>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="eventPointData">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="mon:kind"/>
                <xs:element ref="mon:time" minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref="mon:eventPointDataExtension" minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref="mon:model" minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref="mon:correlation" minOccurs="0"/>
                <xs:element ref="mon:source" minOccurs="0"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="eventPointDataExtension" type="mon:Any" abstract="true" />
    
    <xs:element name="time">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:dateTime">
                    <xs:attribute name="of" type="xs:string" use="optional"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="kind">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:QName">
                    <xs:attribute name="version" type="xs:string" use="optional"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    
    <xs:complexType name="ElementWithId" abstract="true">
        <xs:sequence>
            <xs:element name="name" type="xs:string" minOccurs="0"/>
            <xs:element ref="mon:documentation" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>     
        <xs:attribute name="id" type="xs:string" use="required"/>
    </xs:complexType>
    
    <xs:element name="documentation">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:string">
                    <xs:attribute name="textFormat" type="xs:string" use="optional"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="model">    
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="mon:ElementWithId">
                    <xs:sequence>
                        <xs:element ref="mon:modelExtension" minOccurs="0" maxOccurs="unbounded"/>
                        <xs:element ref="mon:instance" minOccurs="0" />
                    </xs:sequence>
                    <xs:attribute name="type" type="xs:QName" use="required"/>
			        <xs:attribute name="version" type="xs:string" use="optional"/>   
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
     </xs:element>
    <xs:element name="modelExtension" type="mon:Any" abstract="true" />
    
    <xs:element name="instance">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="mon:ElementWithId">
                    <xs:sequence>
                        <xs:element name="state" type="xs:string" minOccurs="0"/>
                        <xs:element name="started" type="xs:nonNegativeInteger" minOccurs="0"/>
                        <xs:element name="startedId" minOccurs="0">
                            <xs:simpleType>
                                <xs:list itemType="xs:string"/>
                            </xs:simpleType>
                        </xs:element>
                        <xs:element ref="mon:fault" minOccurs="0"/>
                        <xs:element ref="mon:role" minOccurs="0" maxOccurs="unbounded"/>
                        <xs:element ref="mon:instanceExtension" minOccurs="0" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="instanceExtension" type="mon:Any" abstract="true" />
    
    <xs:element name="fault">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:string">
                    <xs:attribute name="name" type="xs:QName" use="optional"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="role">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="mon:ElementWithId">
                    <xs:sequence>
                        <xs:element ref="mon:resource" minOccurs="1" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="resource">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="mon:ElementWithId">
                    <xs:sequence>
                        <xs:element ref="mon:resourceExtension" minOccurs="0" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="resourceExtension" type="mon:Any" abstract="true" />
    
    <xs:element name="correlation">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="mon:ancestor" minOccurs="0"/>
                <xs:element ref="mon:correlationExtension" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>    
    <xs:element name="correlationExtension" type="mon:Any" abstract="true" />
    
    <xs:element name="ancestor">
        <xs:complexType>
            <xs:complexContent>
                <xs:extension base="mon:ElementWithId">
                    <xs:sequence>
                        <xs:element ref="mon:ancestor" minOccurs="0" maxOccurs="unbounded"/>
                    </xs:sequence>
                </xs:extension>
            </xs:complexContent>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="source">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="mon:server" minOccurs="0" maxOccurs="unbounded"/>
                <xs:element ref="mon:sourceExtension" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="sourceExtension" type="mon:Any" abstract="true" />
    
    <xs:element name="server">
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:string">
                    <xs:attribute name="type" type="xs:QName" use="required"/>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    
    <xs:element name="applicationData">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="mon:applicationDataExtension" minOccurs="0" maxOccurs="unbounded" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="applicationDataExtension" type="mon:Any" abstract="true" />
    
    <xs:complexType name="Any" mixed="true">
        <xs:sequence>
            <xs:any minOccurs="0" maxOccurs="unbounded" processContents="skip"/>
        </xs:sequence>
        <xs:anyAttribute/>
    </xs:complexType>

</xs:schema>
```

The following extensions to the monitoring event schema
define additional supplied fields in the event point data section
of the monitoring events, and how tracking fields and KPI data values
are reported in the application data section.

## IBM extensions to the monitoring event schema

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema 
        targetNamespace="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions"
        xmlns:ibm="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5/extensions"
        xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" 
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        elementFormDefault="qualified" attributeFormDefault="qualified" version="2010-12-16">

    <xs:import namespace="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" schemaLocation="MonitorEvents.xsd"/>
    
    <xs:element name="sequenceId" type="ibm:ColonSeparatedNumbers" substitutionGroup="mon:eventPointDataExtension"/>
    <xs:element name="label" type="ibm:String" substitutionGroup="mon:eventPointDataExtension"/>
    
    <xs:element name="principal" type="ibm:String" substitutionGroup="mon:instanceExtension"/>
    
    <xs:element name="WBISESSION\_ID" type="ibm:String" substitutionGroup="mon:correlationExtension"/>
    
    <xs:element name="application" type="ibm:TypedString" substitutionGroup="mon:sourceExtension" />
    <xs:element name="server" type="ibm:TypedString" substitutionGroup="mon:sourceExtension" />
    <xs:element name="osProcessAndThreadId" type="ibm:ColonSeparatedNumbers" substitutionGroup="mon:sourceExtension"/>
    
    <xs:complexType name="ColonSeparatedNumbers">
        <xs:simpleContent>
            <xs:restriction base="mon:Any">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:pattern value="[0-9]+(:[0-9]+)*"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:restriction>
        </xs:simpleContent>
    </xs:complexType>
    
    <xs:complexType name="String">
        <xs:simpleContent>
            <xs:restriction base="mon:Any">
                <xs:simpleType>
                    <xs:restriction base="xs:string" />
                </xs:simpleType>
            </xs:restriction>
        </xs:simpleContent>
    </xs:complexType>    
    
    <xs:complexType name="TypedString">
        <xs:simpleContent>
            <xs:restriction base="mon:Any">
                <xs:simpleType>
                    <xs:restriction base="xs:string" />
                </xs:simpleType>
                <xs:attribute name="type" type="xs:string" use="required"/>
            </xs:restriction>
        </xs:simpleContent>
    </xs:complexType>

</xs:schema>
```

## Tracking point extensions to the monitoring event
schema

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5"
	xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5"
	xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5"
	xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"
	attributeFormDefault="qualified" version="2010-12-16">

	<xs:import namespace="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" schemaLocation="MonitorEvents.xsd" />

	<xs:element name="snapshot-name" type="wle:String" substitutionGroup="mon:modelExtension" />
	<xs:element name="starting-process-instance" type="wle:String" substitutionGroup="mon:correlationExtension" />
	<xs:element name="tracking-point" type="wle:TrackingPoint" substitutionGroup="mon:applicationDataExtension" />
	
    <xs:complexType name="String">
        <xs:simpleContent>
            <xs:restriction base="mon:Any">
                <xs:simpleType>
                    <xs:restriction base="xs:string" />
                </xs:simpleType>
            </xs:restriction>
        </xs:simpleContent>
    </xs:complexType>    

	<xs:complexType name="TrackingPoint">
		<xs:complexContent>
			<xs:restriction base="mon:Any">
				<xs:sequence>
					<xs:element name="tracked-field" type="wle:TrackedField" minOccurs="0" maxOccurs="unbounded" />
					<xs:element name="kpi-data" type="wle:TrackedField" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
				<xs:attribute name="time" type="xs:dateTime" use="optional" />
				<xs:attribute name="name" type="xs:string" use="optional" />
				<xs:attribute name="id" type="xs:string" use="required" />
				<xs:attribute name="version" type="xs:string" use="optional" />
				<xs:attribute name="description" type="xs:string" use="optional" />
				<xs:attribute name="groupName" type="xs:string" use="optional" />
				<xs:attribute name="groupId" type="xs:string" use="required" />
				<xs:attribute name="groupVersion" type="xs:string" use="optional" />
				<xs:attribute name="groupDescription" type="xs:string" use="optional" />
			</xs:restriction>
		</xs:complexContent>
	</xs:complexType>
	
	<xs:complexType name="TrackedField">
		<xs:simpleContent>
			<xs:extension base="xs:string">
				<xs:attribute name="name" type="xs:string" use="required" />
				<xs:attribute name="id" type="xs:string" use="required" />
				<xs:attribute name="version" type="xs:string" use="optional" />
				<xs:attribute name="description" type="xs:string" use="optional" />
				<xs:attribute name="type" type="xs:QName" use="required" />
			</xs:extension>
		</xs:simpleContent>
	</xs:complexType>

	<xs:simpleType name="trackedFieldType">
		<xs:restriction base="xs:string">
			<xs:enumeration value="number" />
			<xs:enumeration value="string" />
		</xs:restriction>
	</xs:simpleType>

</xs:schema>
```

## User task extensions to the monitoring event schema

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema targetNamespace="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5"
    xmlns:wle="http://www.ibm.com/xmlns/prod/websphere/lombardi/7.5"
    xmlns:mon="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified"
    attributeFormDefault="qualified" version="2010-12-16">
    <xs:import namespace="http://www.ibm.com/xmlns/prod/websphere/monitoring/7.5" schemaLocation="MonitorEvents.xsd" />
    <xs:element name="taskInstanceId" type="wle:String" substitutionGroup="mon:instanceExtension" />
    <xs:element name="taskRecord" type="wle:TaskRecord" substitutionGroup="mon:instanceExtension" />
    
    <xs:complexType name="TaskRecord">
        <xs:complexContent>
            <xs:restriction base="mon:Any">
                <xs:attribute name="taskDisplayName" type="xs:string" use="optional" />
                <xs:attribute name="taskStatus" type="xs:string" use="optional" />
                <xs:attribute name="taskDueDate" type="xs:dateTime" use="required" />
                <xs:attribute name="taskAtRiskTime" type="xs:dateTime" use="optional" />
                <xs:attribute name="taskCompletionTime" type="xs:dateTime" use="optional" />
                <xs:attribute name="taskDescription" type="xs:string" use="optional" />
                <xs:attribute name="taskPriority" type="xs:string" use="required" />
            </xs:restriction>
        </xs:complexContent>
    </xs:complexType>    
</xs:schema>
```