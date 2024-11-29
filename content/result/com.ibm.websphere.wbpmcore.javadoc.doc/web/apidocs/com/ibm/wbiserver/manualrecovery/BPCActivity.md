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

## Interface BPCActivity

- public interface BPCActivity The BPCActivity is an interface to obtain detailed information of a stopped activity in a BPC failed event, and set new information for failed event resubmission. The detailed information includes

```
public interface BPCActivity
```

    - Activity Instance ID
    - Activity Name
    - Input Message
    - Last State Change Time For The Activity

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

java.lang.String
getActivityName()
Return the Activity Name

java.lang.String
getAiid()
Return the activity instance ID

java.util.Date
getFailureDateTime()
Return the last state change time for the activity

java.util.List<FailedEventParameter>
getInputMessage()
Return the input message  of the stopped activity.

java.util.List<FailedEventParameter>
getInputMessage(java.util.Properties adminClientProperties)
Return input message of a stopped activity in the BPC failed event with admin client
 connection properties.

void
setInputMessage(java.util.List<FailedEventParameter> inputMessage)
Set the input message for activity forceRetry

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getAiid
java.lang.String getAiid()
Return the activity instance ID
Returns:String
    - getActivityName
java.lang.String getActivityName()
Return the Activity Name
Returns:String
    - getInputMessage
java.util.List<FailedEventParameter> getInputMessage()
Return the input message  of the stopped activity.
 This API is used in the following two scenarios.
 
 1. The client is in the same cell as Workflow Server runtime.
 
 2. The client is in a different cell as Workflow Server runtime, and the admin client properties
 have been put into Java system environment.

 
 This API does not explicitly throw exception. However, if exception happens such as
 failed to load BO schema and BO deserialization fails,
  FailedEventRuntimeException  will be throw as runtime exception.
Returns:List
    - getInputMessage java.util.List<FailedEventParameter > getInputMessage(java.util.Properties adminClientProperties) Return input message of a stopped activity in the BPC failed event with admin client connection properties. This API is used when the client is in a different cell as Workflow Server runtime, and the admin client properties are not in Java system environment. The admin client properties should included the following information. When security is enabled, additional information are required. For SOAP based connection, some other properties may also be required in order to make a SSL connection. An easy way to use this API is to obtain the properties from the existing admin client. For example, List parameters = getFailedEventParameters(adminClient.getConnectorProperties()); This API does not explicitly throw exception. However, if exception happens such as failed to load BO schema and BO deserialization fails, FailedEventDataException will be throw as runtime exception. Parameters: adminClientProperties - Returns: List

#### getInputMessage

```
java.util.List<FailedEventParameter> getInputMessage(java.util.Properties adminClientProperties)
```

The admin client properties should included the following information.
 
 AdminClient.CONNECTOR\_TYPE 
 AdminClient.CONNECTOR\_HOST 
 AdminClient.CONNECTOR\_PORT 

 When security is enabled, additional information are required.
 
 AdminClient.CONNECTOR\_SECURITY\_ENABLED 
 AdminClient.USERNAME 
 AdminClient.PASSWORD 

 For SOAP based connection, some other properties may also be required in order to
 make a SSL connection.
 
 javax.net.ssl.trustStore 
 javax.net.ssl.keyStore 
 javax.net.ssl.trustStorePassword 
 javax.net.ssl.keyStorePassword 

 An easy way to use this API is to obtain the properties from the existing admin client.
 

 For example,
 
 List parameters = getFailedEventParameters(adminClient.getConnectorProperties());
 

 This API does not explicitly throw exception. However, if exception happens such as
 failed to load BO schema and BO deserialization fails, FailedEventDataException will
 be throw as runtime exception.

- setInputMessage
void setInputMessage(java.util.List<FailedEventParameter> inputMessage)
Set the input message for activity forceRetry
Parameters:inputMessage -

- getFailureDateTime
java.util.Date getFailureDateTime()
Return the last state change time for the activity
Returns:Date