<!-- image -->

# Invoking SCA components from JavaServer Pages

## Before you begin

## About this task

The JSP file has to be deployed in the same EAR file as
the module assembly. Do not copy the sca.references file to another
EAR file. The file will not work outside the module that it belongs
to. If the web project is in another EAR file, then the JSP file is
in another module, and imports and exports are required for it to
work with services in another module.

Here are the steps for
adding the JSP file to the module:

## Procedure

1. Create a web project.
2. Build the JSP file in the web project. If you are importing
the code, import it into this web project. See the example of code
below.
3. Open the module (which has the stand-alone references)
with the dependency editor. Add a dependency on the web project as
a Java 2 Platform Enterprise Edition project. Make sure that the Deploy
with Module check box option is selected so that the web
project will be added to the EAR file.

## Example

Here is an example of some JSP code that uses the stand-alone
references in the module assembly:

```
com.ibm.websphere.sca.Service bankService = 
(com.ibm.websphere.sca.Service)com.ibm.websphere.sca.ServiceManager.INSTANCE.locateService("BankServicePartner");
=> The "BankServicePartner" reference name comes from the sca.references file in the module 
=> (For example, <reference name="BankServicePartner">...). This file will exist after creating a stand-alone references node in the wiring editor.

com.ibm.websphere.sca.scdl.OperationType operationType = bankService.getReference().getOperationType("openAccount");
=> Use the operation type to get the DataObject types that need to be passed into the invoke operation.

com.ibm.websphere.bo.BOFactory factory = 
(com.ibm.websphere.bo.BOFactory) new com.ibm.websphere.sca.ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");
=> Standard way to obtain the factory for creating business objects.

commonj.sdo.DataObject input = factory.createByType(operationType.getInputType());
=> Create the proper kind of data object that the operation expects as input.

=> Assume that we do not have a multipart input, for now.
commonj.sdo.DataObject customer = input;

if(operationType.isWrapperType(type))
{
=> In order to call the reference in this case, the multipart must be passed in. 
=> So create the customer data object and set it on the multipart object.
customer = factory.createByType(operationType.getInputType().getProperty("input1").getType());
input.set("input1", customer);
}

customer.setString("firstName", "Bob"); 
customer.setString("lastName", "Smith");
customer.setString("address", "7 Holly Drive");
customer.setBoolean("isGold", true);
customer.setInt("birthYear", 1976);
=> The previous 5 lines set the attributes on Customer.

commonj.sdo.DataObject output = (commonj.sdo.DataObject)bankService.invoke("openAccount",input);
commonj.sdo.DataObject account = null;
if(operationType.isWrapperType(type))
{
=> Just like the input, the output may also be a wrapper type.
account = output.getDataObject("output1");
System.out.println(account.get("id"));
}
```