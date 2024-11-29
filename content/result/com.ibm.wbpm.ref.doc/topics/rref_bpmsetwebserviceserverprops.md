# BPMSetWebServiceServerProperties command

The BPMSetWebServiceServerProperties command
is run using the AdminTask object of the wsadmin scripting client.
The variables that are updated by this command must already exist.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, an application cluster member
runs the Workflow Server and Workflow Center applications.
Therefore, you must run this command on the node that contains that
application cluster member. Do not run the command from the deployment
manager profile.

## Location

Start the wsadmin scripting client from the install\_root/bin directory.

## Syntax

```
BPMSetWebServiceServerProperties
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
-serverName server\_name
[-wsdlUrl webserviceurl]
[-protectedWsdl {true | false}]
[-wsdlUsername wsdlusername]
[-wsdlPassword wsdlpassword]
[-overrideEndpoint {true | false}]
[-endpointAddress endpointaddress]
[-endpointPort endpointport\_number]
[-securityMode {USE\_BASIC\_SECURITY | USE\_POLICY\_SET}]
[-policySet policyset]
[-policyBinding policybinding]
[-authentication {NONE | HTTP\_AUTHENTICATION | USERNAME\_TOKEN\_PASSWORD\_PLAINTEXT | USERNAME\_TOKEN\_PASSWORD\_DIGEST}]
[-username username]
[-password password]
[-clientCertificateAlias clientcertificatealias]
[-signRequest {true | false}]
[-expectEncryptedResponse {true | false}]
[-serverCertificateAlias servercertificatealias]
[-encryptRequest {true | false}]
[-expectSignedResponse {true | false}]
```

## Parameters

## Example

The following examples first show
how to set the web service server connection variables on the web
service server for the http://mycorp.com/usafinance?wsdl URL.
These variables are in a snapshot of the AmericanFinance process application.
Basic security is used with no authentication. When a property value
is set to null, the command does not update the property value. In
the next example, the URL is changed to http://mycorp.com/newyorkfinance?wsdl.
The next example shows the short form of the same example. The last
example removes the wsdlUrl value. To remove a value, use "" or do
not pass a value to the property.

In the example, the user
establishes a SOAP connection to the Workflow Center server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSetWebServiceServerProperties('[-containerAcronym AMERICANFINANCE -containerSnapshotAcronym V001 -serverName WEBSERVICE\_SERVER
 -wsdlUrl http://mycorp.com/usafinance?wsdl -protectedWsdl true -wsdlUsername admin -wsdlpassword admin -overrideEndpoint false 
-endpointAddress null -endpointPort null -securityMode USE\_BASIC\_SECURITY -policySet null -policyBinding null -authentication NONE 
-username null -password null -clientCertificateAlias null -signRequest null -expectEncryptedResponse null 
-serverCertificateAlias null -encryptRequest null -expectSignedResponse null]')

wsadmin>AdminTask.BPMSetWebServiceServerProperties('[-containerAcronym AMERICANFINANCE -containerSnapshotAcronym V001 -serverName WEBSERVICE\_SERVER
 -wsdlUrl http://mycorp.com/newyorkfinance?wsdl -protectedWsdl null -wsdlUsername null -wsdlpassword null -overrideEndpoint null 
-endpointAddress null -endpointPort null -securityMode null -policySet null -policyBinding null -authentication null 
-username null -password null -clientCertificateAlias null -signRequest null -expectEncryptedResponse null 
-serverCertificateAlias null -encryptRequest null -expectSignedResponse null]')

wsadmin>AdminTask.BPMSetWebServiceServerProperties('[-containerAcronym AMERICANFINANCE -containerSnapshotAcronym V001 -serverName WEBSERVICE\_SERVER
 -wsdlUrl http://mycorp.com/newyorkfinance?wsdl]')

wsadmin>AdminTask.BPMSetWebServiceServerProperties('[-containerAcronym AMERICANFINANCE -containerSnapshotAcronym V001 -serverName WEBSERVICE\_SERVER
 -wsdlUrl ""]')
```