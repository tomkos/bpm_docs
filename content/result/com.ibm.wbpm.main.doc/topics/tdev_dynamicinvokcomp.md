<!-- image -->

# Dynamically invoking a component

## Before you begin

## About this task

## Procedure

1. Determine the module that contains the component required.
2 Determine the array required by the component. The input array can be one of three types:
    - Primitive uppercase Java types or arrays of this type
    - Ordinary Java classes or arrays of the classes
    - Service Data Objects (SDOs)
3. Define an array to contain the response from the component.

The response array can be of the same types as the input array.
4. Use the invoke() method to invoke the required component and pass the array object to the
component.
5. Process the result.

## Examples of dynamically invoking a component

```
Service service = (Service)serviceManager.locateService("multiParamInf");
		
		Reference reference = service.getReference();

		OperationType methodMultiType = 
				reference.getOperationType("methodWithMultiParameter");

		Type t = methodMultiType.getInputType();

		BOFactory boFactory = (BOFactory)serviceManager.locateService
				("com/ibm/websphere/bo/BOFactory");

		DataObject paramObject = boFactory.createbyType(t);

		paramObject.set(0,"input1")
		paramObject.set(1,"input2")
		paramObject.set(2,"input3")

		service.invoke("methodMultiParamater",paramObject);
```

The following example uses the invoke method with a WSDL port type interface as the target.

```
Service serviceOne = (Service)serviceManager.locateService("multiParamInfWSDL");
	
	DataObject dob = factory.create("http://MultiCallWSServerOne/bos", "SameBO");
			dob.setString("attribute1", stringArg);

	DataObject wrapBo = factory.createByElement
		("http://MultiCallWSServerOne/wsdl/ServerOneInf", "methodOne");
			wrapBo.set("input1", dob); //wrapBo encapsulates all the parameters of methodOne
			wrapBo.set("input2", "XXXX");
			wrapBo.set("input3", "yyyy");

	DataObject resBo= (DataObject)serviceOne.invoke("methodOne", wrapBo);
```