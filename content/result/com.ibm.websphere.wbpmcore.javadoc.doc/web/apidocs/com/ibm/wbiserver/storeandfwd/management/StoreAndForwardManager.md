- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface StoreAndForwardManager

- public interface StoreAndForwardManager
The  StoreAndForwardManager  interface defines the operations to
 manage stored events. The interface is implemented as a MBean with partial
 ObjectName:

 
 WebSphere:*,type=StoreAndForwardManager
 

 To manage the state of the control points, obtain the StoreAndForwardManager
 MBean from the admin server or admin client and invoke the operations. In a network
 deployment environment, there are multiple StoreAndForwardManager MBeans
 running. Each MBean manages the state of the control points on that
 deployment target.

 
 Sample code to get StoreAndForwardManager MBean from remote client.

 
 Properties connectProps = new Properties();
 connectProps.setProperty(AdminClient.CONNECTOR\_TYPE, AdminClient.CONNECTOR\_TYPE\_SOAP);
 connectProps.setProperty(AdminClient.CONNECTOR\_HOST, "localhost");
 connectProps.setProperty(AdminClient.CONNECTOR\_PORT, "8880");
 AdminClient adminClient = null;
 try {
     adminClient = AdminClientFactory.createAdminClient(connectProps);
 } catch (ConnectorException e) {
     System.out.println("Exception creating admin client: " + e);
 }
 ObjectName queryName = new ObjectName("WebSphere:*,type=StoreAndForwardManager");
 ObjectName nodeAgent = null;
 Set s = adminClient.queryNames(queryName, null);
 if (!s.isEmpty())
     nodeAgent = (ObjectName) s.iterator().next();
 else
     System.out.println("Store and Forward Manager MBean was not found");
 

 If security is enabled on the server, set the appropriate properties.
 
 If multiple deployment environments are used, the method
 systemAvailable(String, String, String) and
 systemUnavailable(String, String, String) are preferred.

 Sample code is provided for each operation with admin client. The invocation
 syntax for admin server is the same as admin client.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

void
systemAvailable(java.lang.String moduleName,
               java.lang.String storeConfigurationName)
Change the state of the control point to forward the stored events.

void
systemAvailable(java.lang.String moduleName,
               java.lang.String storeConfigurationName,
               java.lang.String deploymentEnvironmentName)
Change the state of the control point to forward the stored events.

void
systemUnavailable(java.lang.String moduleName,
                 java.lang.String storeConfigurationName)
Change the state of the control point to store the events.

void
systemUnavailable(java.lang.String moduleName,
                 java.lang.String storeConfigurationName,
                 java.lang.String deploymentEnvironmentName)
Change the state of the control point to store the events.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - systemAvailable
void systemAvailable(java.lang.String moduleName,
                   java.lang.String storeConfigurationName)
                     throws StoreAndForwardException
Change the state of the control point to forward the stored events.
 
 
 Sample code: 

 
 String opName = "systemAvailable"; 
 Object[] params = new Object[]{moduleName, configurationName}; 
 String[] signature = new String[]{"java.lang.String", "java.lang.String"};
 adminClient.invoke(storeAndForwardMBean, opName, params, signature);
 
Parameters:moduleName - The destination SCA module name to change the state of the control pointstoreConfigurationName - The configuration name defined in your Store and Forward qualifier
Throws:
StoreAndForwardException
    - systemAvailable
void systemAvailable(java.lang.String moduleName,
                   java.lang.String storeConfigurationName,
                   java.lang.String deploymentEnvironmentName)
                     throws StoreAndForwardException
Change the state of the control point to forward the stored events.
 
 
 Sample code: 

 
 String opName = "systemAvailable"; 
 Object[] params = new Object[]{moduleName, configurationName, deploymentEnvironmentName}; 
 String[] signature = new String[]{"java.lang.String", "java.lang.String", "java.lang.String"};
 adminClient.invoke(storeAndForwardMBean, opName, params, signature);
 
Parameters:moduleName - The destination SCA module name to change the state of the control pointstoreConfigurationName - The configuration name defined in your Store and Forward qualifierdeploymentEnvironmentName - The name of the destination deployment environment where the destination SCA module is running. If null, the behavior is the same as the systemAvailable(String, String) method
Throws:
StoreAndForwardException
    - systemUnavailable
void systemUnavailable(java.lang.String moduleName,
                     java.lang.String storeConfigurationName)
                       throws StoreAndForwardException
Change the state of the control point to store the events.
 
 
 Sample code: 

 
 String opName = "systemUnavailable"; 
 Object[] params = new Object[]{moduleName, configurationName}; 
 String[] signature = new String[]{"java.lang.String", "java.lang.String"};
 adminClient.invoke(storeAndForwardMBean, opName, params, signature);
 
Parameters:moduleName - The destination SCA module name to change the state of the control pointstoreConfigurationName - The configuration name defined in your Store and Forward qualifier
Throws:
StoreAndForwardException
    - systemUnavailable
void systemUnavailable(java.lang.String moduleName,
                     java.lang.String storeConfigurationName,
                     java.lang.String deploymentEnvironmentName)
                       throws StoreAndForwardException
Change the state of the control point to store the events.
 
 
 Sample code: 

 
 String opName = "systemUnavailable"; 
 Object[] params = new Object[]{moduleName, configurationName, deploymentEnvironmentName}; 
 String[] signature = new String[]{"java.lang.String", "java.lang.String", "java.lang.String"};
 adminClient.invoke(storeAndForwardMBean, opName, params, signature);
 
Parameters:moduleName - The destination SCA module name to change the state of the control pointstoreConfigurationName - The configuration name defined in your Store and Forward qualifierdeploymentEnvironmentName - The name of the destination deployment environment where the destination SCA module is running. If null, the behavior is the same as the systemUnavailable(String, String) method
Throws:
StoreAndForwardException