# Considerations for the IBM Integration
Designer migration
process

- It validates if a business object of the specified namespace and name exists. If it is invalid,
you see the following error message in the Problems
view:A BO with namespace <namespace> and name <BO name> cannot be found.
- It validates if the correct getter and setter methods are used based on the attribute type. If
not, you see the following error message in the Problems
view:Incompatible method argument type.  
The <BO attribute name> field is of type <actual attribute type>.
- It validates if the attribute referenced in the getter and setter methods exists. If not, you
see the following error message in the Problems
view:The field <BO attribute name> does not exist in the Business Object <BO name with namespace>.

- Java components
- Custom mediation primitive in mediation flows
- Java snippet activities in business processes
- Custom mappings in business object maps

```
com.ibm.websphere.bo.BOXMLSerializer serializer = new 
com.ibm.websphere.bo.impl.BOXMLSerializerImpl();
```

```
com.ibm.websphere.sca.ServiceManager srvMgr = 
com.ibm.websphere.sca.ServiceManager.INSTANCE;
com.ibm.websphere.bo.BOXMLSerializer serializer = (BOXMLSerializer) 
srvMgr.locateService("com/ibm/websphere/bo/BOXMLSerializer");
```

For example, a namespace must
be an absolute Uniform Resource Identifier, for example, starting
with http://.  Refactor the target namespace by pressing Alt+Shift+R on
the target namespace field of the Properties page.

```
The <attribute\_name> schema element was not found in the <xpath\_expression> XPATH.
```

```
/MyBO/myAttribute
Then change it to:
/MyBO/@myAttribute
```

```
CWLAT0064W: The 4 transform includes an inherited type, 
which might produce unwanted side effects when the map runs.
```

The MQ binding now uses an activation specification in its
configuration rather than listener ports. If you are migrating an
application that uses an MQ binding for an import or export from V6
to V7, you must update your binding configuration. For instructions
about the required migration steps for the MQ binding, see the related
task.

## Related information

- Migrating WebSphere MQ Bindings from version 6 to later versions