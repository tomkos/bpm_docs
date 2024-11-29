# SMO: HTTP schema

## Introduction

The HTTP schema specifies the
overall structure of the HTTP header.

## HTTP header schema

```
<schema xmlns="http://www.w3.org/2001/XMLSchema"
        xmlns:httpsca="http://www.ibm.com/xmlns/prod/websphere/http/sca/6.1.0"
        xmlns:ecore="http://www.eclipse.org/emf/2002/Ecore"
        ecore:package="com.ibm.websphere.http.headers"
        ecore:nsPrefix="httpsca"
        elementFormDefault="qualified"
        targetNamespace="http://www.ibm.com/xmlns/prod/websphere/http/sca/6.1.0">

  <element name="HTTPMessageHeader" type="httpsca:HTTPMessageParameters"/>
  
  <complexType name="HTTPMessageParameters">
    <sequence>
      <element minOccurs="0" nillable="true" name="HTTPControl" type="httpsca:HTTPControl"/>
      <element minOccurs="0" nillable="true" name="HTTPHeaders" type="httpsca:HTTPHeaders"/>
    </sequence>
  </complexType>

  <complexType name="HTTPControl">
    <sequence>
      <element minOccurs="0" nillable="true" name="URL" type="anyURI"/>
      <element minOccurs="0" nillable="true" name="Version" type="httpsca:HTTPVersion"/>
      <element minOccurs="0" nillable="true" name="Method" type="string"/>
      <element minOccurs="0" nillable="true" name="DynamicOverrideURL" type="anyURI"/>
      <element minOccurs="0" nillable="true" name="DynamicOverrideVersion" type="httpsca:HTTPVersion"/>
      <element minOccurs="0" nillable="true" name="DynamicOverrideMethod" type="string"/>
      <element minOccurs="0" nillable="true" name="MediaType" type="string"/>
      <element minOccurs="0" nillable="true" name="Charset" type="string"/>
      <element minOccurs="0" nillable="true" name="TransferEncoding" type="string"/>
      <element minOccurs="0" nillable="true" name="ContentEncoding" type="string"/>
      <element minOccurs="0" name="StatusCode" type="int"/>
      <element minOccurs="0" nillable="true" name="ReasonPhrase" type="string"/>
      <element minOccurs="0" nillable="true" name="Authentication" type="httpsca:HTTPAuthentication"/>
      <element minOccurs="0" nillable="true" name="SSLSettings" type="httpsca:HTTPSSLSettings"/>
      <element minOccurs="0" maxOccurs="2" nillable="true" name="ProxySettings" type="httpsca:HTTPProxySettings"/>
    </sequence>
  </complexType>

  <complexType name="HTTPHeader">
    <sequence>
      <element name="name" type="string"/>
      <element name="value" type="string"/>
    </sequence>
  </complexType>

  <complexType name="HTTPHeaders">
    <sequence>
      <element name="header" minOccurs="0" maxOccurs="unbounded" type="httpsca:HTTPHeader"/>
    </sequence>
  </complexType>
  
  <!--SSL Settings -->
  <complexType name="HTTPSSLSettings">
    <sequence>
      <element default="SSL" nillable="true" name="SSLVersion" type="string"/>
      <element default="false" nillable="true" name="SSLDebug" type="boolean"/>
      <element default="JKS" nillable="true" name="KeyStoreType" type="string"/>
      <element default="JKS" nillable="true" name="TrustStoreType" type="string"/>
      <element nillable="true" name="KeyStore" type="string"/>
      <element nillable="true" name="KeyStoreAlias" type="string"/>
      <element nillable="true" name="KeyStorePassword" type="string"/>
      <element nillable="true" name="TrustStore" type="string"/>
      <element nillable="true" name="TrustStorePassword" type="string"/>
      <element default="false" nillable="true" name="UseClientAuth" type="boolean"/>
    </sequence>
  </complexType>
	
  <!--Proxy Settings -->
  <complexType name="HTTPProxySettings">
    <sequence>
      <element nillable="true" name="proxyHost" type="string"/>
      <element nillable="true" name="proxyPort" type="int"/>
      <element nillable="true" name="proxyType" type="httpsca:HTTPProxyType"/>
      <element nillable="true" minOccurs="0" name="proxyCredentials" type="httpsca:HTTPCredentials"/>
      <element nillable="true" minOccurs="0" maxOccurs="unbounded" name="nonProxyHost" type="string"/>
    </sequence>
  </complexType>
	
  <!--HTTP Authentication -->
  <complexType name="HTTPAuthentication">
    <sequence>
      <element nillable="true" name="credentials" type="httpsca:HTTPCredentials"/>
      <element nillable="true" name="authenticationType" type="httpsca:HTTPAuthenticationType"/>
    </sequence>
  </complexType>
	
  <!--HTTP Credentials -->
  <complexType name="HTTPCredentials">
    <sequence>
      <element nillable="true" name="userId" type="string"/>
      <element nillable="true" name="password" type="string"/>
    </sequence>
  </complexType>
	
  <!-- Authentication Type. Supports: Basic Auth -->
  <simpleType name="HTTPAuthenticationType">
    <restriction base="string">
      <enumeration value="Basic"/>
    </restriction>
  </simpleType>
	
  <!-- Proxy protocol type. Supports: http and https -->
  <simpleType name="HTTPProxyType">
    <restriction base="string">
      <enumeration value="http"/>
      <enumeration value="https"/>
    </restriction>
  </simpleType>	
	
  <!-- HTTP Version type.-->
  <simpleType name="HTTPVersion">
    <restriction base="string">
      <enumeration value="1.0"/>
      <enumeration value="1.1"/>
    </restriction>
  </simpleType>	
</schema>
```

## Schema field descriptions