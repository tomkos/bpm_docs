<!-- image -->

# Typing fault variables

## About this task

## Procedure

1 Create the new type as follows:
    1. If there is no existing library, create a new library
called FaultType by clicking File > New > Other > Library.
    2. Right-click your process module and select Open Dependency Editor. Click Add and select the library from step 1a in the list.
    3. Create an XSD file called bpcfault.xsd by clicking File > New > Other > Simple > File.
    4. Paste the following text into the editor and save it.
<?xml version="1.0"?>

<!--
(C) Copyright IBM Corporation 2005, 2019.

This file specifies a complex data type that may be used
in BPEL processes in fault handlers that catch a standard or
runtime fault to specify the variable type.
-->
<xs:schema targetNamespace="http://www.ibm.com/xmlns/prod/websphere/business-process/6.0.0/"
           xmlns:xs="http://www.w3.org/2001/XMLSchema"
           elementFormDefault="qualified">

        <!--
        Standard fault type
        -->
        <xs:complexType name="StandardFaultType">
                <xs:sequence>
                        <xs:element name="faultName" type="xs:string"/>
                        <xs:element name="faultNameUri" type="xs:string"/>
                        <xs:element name="messageText" type="xs:string"/>
                        <xs:element name="rootException" type="xs:string"/>
                </xs:sequence>
        </xs:complexType>

</xs:schema>
2 Create a variable and point to the XSD file.

1. In the tray, create a new variable by clicking the plus
symbol () beside the Variables area.
2. In the properties area, click the Details tab.
3. Select Data Type, and click Browse.
4. In the Data Type Selection window, click Show all XSD types, browse to StandardFaultType, and click OK..
3. Determine the catch element (that exists within a Fault
Handler) that you would like to associate with the new fault type.
In the Details tab, browse to the newly create
fault variable.

## Results

## Related concepts

- Fault activities
- Raising faults
- BPEL process compensation
- Fault handling and compensation handling in BPEL processes

## Related tasks

- Using fault handlers
- Continue processing upon unhandled faults