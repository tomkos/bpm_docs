<!-- image -->

# SCA data object containment and wrapper usages

Some interfaces require no wrapper when a single argument is accepted while other interfaces
require a wrapper for any operation. For example, a Java method which accepts a single parameter
does not require the parameter be wrapped. All Document Literal Wrapped style WSDL operations
require a wrapper regardless of the number of parameters.

```
Service service = (Service) locateService\_servicePartner();
Type inputType = service.getReference().getOperationType("echoMulti").getInputType();
ServiceManager serviceManager = new ServiceManager();
BOFactory boFactory = (BOFactory) serviceManager.locateService("com/ibm/websphere/bo/BOFactory");
DataObject wrapper = boFactory.createByType(inputType);
wrapper.set(0, new Integer(5));
wrapper.set(1, new Integer(10));
service.invoke("echoMulti", wrapper);
```

## Containment

```
<parent>
<child>
...
</child>
</parent>
```

In this example, "child" is always contained within the enclosing elements of its parent. It can
be moved to another parent container, but cannot exist as a sub-element of two parents without
copying the XML text <child>…</child>.

In order to avoid damaging the existing containment relationship, a DataObject
must first be cloned before being set into another property. To prevent unnecessary cloning of
DataObject parameters and facilitate a simplified programming model, the SCA
container provides input and output types with non-containment properties when the interface is
either a Java interface or a WSDL interface using the document literal wrapped style. No clone is
necessary when the wrapper is created by using the Type returned by the
OperationType.getInputType() or OperationType.getOuputType()
methods for these interface types. To instantiate the wrapper for these types, use the
BOFactory.createByType(...) method.

```
Type type = operationType.getInputType();
List properties = type.getProperties();
for(int i=0;i<properties.size();i++){
    Property property = (Property)properties.get(i);
    if(property.getType().getInstanceClass() == null || property.getType().getInstanceClass().equals(DataObject.class)){
        //Property is a complex type
        if(!property.isContainment()){
          //The property is a non-containment complex property. If a DataObject is set to this property, its parent will not be changed
        } else{
          //The property is a containment (ordinary) property. If a DataObject is set to this property, its previous parent will be discarded
        }

   } else{
        //The property is a simple type. All simple type properties are non-containment
   }
}
```

When serialized, a non-containment property does not include the XML representation of the
business object, but instead includes only a reference to the business object, which is expressed as
a URI. Since this URI is likely not meaningful to the application, direct serialization of container
provided non-containment business objects is not advised.

## Object Reference Visibility

Data Object and Java Object parameters which are passed either directly or as a non-containment
property of a wrapper are provided directly to component implementations when the invocation occurs
on the same thread and within the same module. This means that the caller and the target both view
the same business object or Java object, and therefore modifications made to the object in the
target component be visible to the caller after the completion of the processing. The object
reference is never passed between multiple threads or outside of a single module, so anytime the
invocation is transferred to another thread or module, a copy of the original object is provided to
the caller.

To promote component implementations which can be used in multiple wiring configurations, it is
best to avoid expecting that any object modifications be visible upstream. Instead, if any
modifications must be made visible to the caller, return the modified values. Doing so assures that
the component can be used consistently regardless of how it is wired and invoked.