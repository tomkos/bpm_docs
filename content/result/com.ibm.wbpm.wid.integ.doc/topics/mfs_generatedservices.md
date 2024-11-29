<!-- image -->

# Generated services

The business graph generated for each data type (or business object)
has a suffix of BG. For example, the business graph for a data type
called IVTCMBI1\_Page1 would be IVTCMBI1\_Page1BG. Both the business
objects and business graphs are listed under the Data Types section.

The generated interface file is a WSDL interface file and is listed
under the Interfaces section. You can see the content of the interface
file by right-clicking the file and selecting Open
With > Text Editor.
The following sample shows the input type and output type for a generated
interface called MFSEMDOutboundinterface.

```
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions name="MFSEMDOutboundinterface" targetNamespace="http://ConvPB/MFSEMDOutboundinterface" 
 xmlns:bons1="http://www.ibm.com/xmlns/prod/ims/mfs/sca/IVTCBMI1\_Page1BG" 
 xmlns:bons2="http://www.ibm.com/xmlns/prod/ims/mfs/sca/IVTCBMO2BG" 
 xmlns:bons3="http://www.ibm.com/xmlns/prod/ims/mfs/sca/IVTCBMI2\_Page1BG" 
 xmlns:tns="http://ConvPB/MFSEMDOutboundinterface" 
 xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
 xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <wsdl:types>
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://ConvPB/MFSEMDOutboundinterface">
      <xsd:import namespace="http://www.ibm.com/xmlns/prod/ims/mfs/sca/IVTCBMI2\_Page1BG" schemaLocation="IVTCBMI2BG.xsd"/>
      <xsd:import namespace="http://www.ibm.com/xmlns/prod/ims/mfs/sca/IVTCBMI1\_Page1BG" schemaLocation="IVTCBMI1BG.xsd"/>
      <xsd:import namespace="http://www.ibm.com/xmlns/prod/ims/mfs/sca/IVTCBMO2BG" schemaLocation="IVTCBMO2BG.xsd"/>
      <xsd:element name="IVTCBMI1">
        <xsd:complexType>
          <xsd:sequence>
 1             <xsd:element name="IVTCBMI1Input" type="bons1:IVTCBMI1\_Page1BG"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="IVTCBMI1Response">
        <xsd:complexType>
          <xsd:sequence>
 2             <xsd:element name="IVTCBMI1Output" type="bons2:IVTCBMO2BG"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="IVTCBMI2">
        <xsd:complexType>
          <xsd:sequence>
 3             <xsd:element name="IVTCBMI2Input" type="bons3:IVTCBMI2\_Page1BG"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="IVTCBMI2Response">
        <xsd:complexType>
          <xsd:sequence>
 4             <xsd:element name="IVTCBMI2Output" type="bons2:IVTCBMO2BG"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:schema>
  </wsdl:types>
  <wsdl:message name="IVTCBMI1RequestMsg">
    <wsdl:part element="tns:IVTCBMI1" name="IVTCBMI1Parameters"/>
  </wsdl:message>
  <wsdl:message name="IVTCBMI1ResponseMsg">
    <wsdl:part element="tns:IVTCBMI1Response" name="IVTCBMI1Result"/>
  </wsdl:message>
  <wsdl:message name="IVTCBMI2RequestMsg">
    <wsdl:part element="tns:IVTCBMI2" name="IVTCBMI2Parameters"/>
  </wsdl:message>
  <wsdl:message name="IVTCBMI2ResponseMsg">
    <wsdl:part element="tns:IVTCBMI2Response" name="IVTCBMI2Result"/>
  </wsdl:message>
  <wsdl:portType name="MFSEMDOutboundinterface">
    <wsdl:operation name="IVTCBMI1">
      <wsdl:input message="tns:IVTCBMI1RequestMsg" name="IVTCBMI1Request"/>
      <wsdl:output message="tns:IVTCBMI1ResponseMsg" name="IVTCBMI1Response"/>
    </wsdl:operation>
    <wsdl:operation name="IVTCBMI2">
      <wsdl:input message="tns:IVTCBMI2RequestMsg" name="IVTCBMI2Request"/>
      <wsdl:output message="tns:IVTCBMI2ResponseMsg" name="IVTCBMI2Response"/>
    </wsdl:operation>
  </wsdl:portType>
</wsdl:definitions>
```