<!-- image -->

# Connection timeout when running a wsadmin script

## Reason

- For the call from the wsadmin environment to the deployment manager.
The default for is 180 seconds.
- For the connection from the deployment manager to the node agent.
The default is 600 seconds.
- For the connection from the node agent to the runtime deployment
target. The default is 600 seconds.

## Resolution

- Modify the invocation parameters so that less work is performed,
so that the operation completes before the timeout. For example, many
scripts have parameters that can be used to select fewer objects.
- Modify the properties for the connector that is used. Remote JMX connector This connector is used between server processes that reside ondifferent physical machines, for example, between the deployment managerand the node agent. The default is the SOAP connector. Local JMX connector This connector is used between server processes that reside onthe same physical machine, for example, between the node agent andits application servers. The default is the IPC connector. You must modify the properties in the soap.client.propsfile, ipc.client.props, or sas.client.prop files, and the custom propertiesfor the deployment manager and the node agents where members of yourruntime deployment target are running. The following example showshow to change the SOAP connector properties.
    1. Modify the com.ibm.SOAP.requestTimeout property by editing
the soap.client.props file that is located in
the properties subdirectory of the profile\_root directory.
    2 Change the requestTimeout custom propertyusing the administrative console:
        1. For servers or cluster members, click Servers > Application servers > server\_name > Server
Infrastructure > Administration > Administration Services > Additional
properties > JMX Connectors > SOAPConnector > Additional Properties > Custom properties, locate the requestTimeout custom
property, and modify its value.
        2. For the deployment manager, click System
administration > Deployment manager > Additional Properties > Administration
Services > Additional properties > JMX Connectors > SOAPConnector > Additional Properties > Custom properties, locate the requestTimeout custom
property, and modify its value.
        3. For the node agents, click System administration > Node agents > node\_agent\_name > Additional Properties > Administration
Services > Additional properties > JMX Connectors > SOAPConnector > Additional Properties > Custom properties, locate the requestTimeout custom
property, and modify its value.

## Related information

- Java Management Extensions connector properties