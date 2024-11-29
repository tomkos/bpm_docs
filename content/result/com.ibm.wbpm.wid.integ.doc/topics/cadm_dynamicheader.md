<!-- image -->

# JCA Interaction Spec and Connection Spec dynamic properties

The javax.cci.InteractionSpec carries information
on how the interaction request with the resource adapter should be
handled. It can also carry information on how the interaction was
achieved after the request. These two-way communications through the
interactions are sometimes referred to as conversations.

- Names must begin with the prefix IS, followed
by the property name. For example, an interaction spec with a JavaBeans property called InteractionId would
specify the property name as ISInteractionId.
- The name/value pair represents the name and the value of the simple
type of the Interaction Spec property.

In this example, an interface specifies that the input
of an operation is an Account data object. This interface
invokes an EIS import binding application with the intention to send
and receive a dynamic InteractionSpec property
called workingSet with the value xyz.

```
BOFactory dataFactory = (BOFactory) \
 serviceManager.locateService("com/ibm/websphere/bo/BOFactory");
  //Wrapper for doc-lit wrapped style interfaces,
  //skip to payload for non doc-lit
  DataObject docLitWrapper = dataFactory.createByElement /
  ("http://mytest/eis/Account", "AccountWrapper");
```

```
DataObject account = docLitWrapper.createDataObject(0);
  DataObject accountInfo = account.createDataObject("AccountInfo");
  //Perform your setting up of payload

  //Construct properties data for dynamic interaction
  
  DataObject properties = account.createDataObject("properties");
```

```
properties.setString("ISworkingSet", "xyz");

  //Invoke the service with argument

  Service accountImport = (Service) \
  serviceManager.locateService("AccountOutbound");
  DataObject result = accountImport.invoke("createAccount", docLitWrapper);               

  //Get returned property
  DataObject retProperties = result.getDataObject("properties");

  String workingset = retProperties.getString("ISworkingSet");
```

To use ConnectionSpec properties,
set the resAuth specified on the import binding to Application.
Also, make sure the resource adapter supports component authorization.
See chapter 8 of the J2EE Connector
Architecture Specification for more details.