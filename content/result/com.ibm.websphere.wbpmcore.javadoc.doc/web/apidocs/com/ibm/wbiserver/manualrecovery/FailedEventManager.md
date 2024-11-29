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

## Interface FailedEventManager

- public interface FailedEventManager
The  FailedEventManager  interface defines the operations to manage failed events.
 The interface is implemented as a MBean with partial ObjectName:
 
 WebSphere:*,type=FailedEventManager
 

 To manage failed events with programming, obtain the FailedEventManager MBean
 from admin server or admin client and invoke the operations. In Network Deployment
 environment, there're more than one FailedEventManager MBeans running. Just get
 one of the MBeans, and all the failed events can be managed.

 
 Sample code to get FailedEventManager MBean from remote client.
 
 Properties connectProps = new Properties();
 connectProps.setProperty(AdminClient.CONNECTOR\_TYPE, AdminClient.CONNECTOR\_TYPE\_SOAP);
 connectProps.setProperty(AdminClient.CONNECTOR\_HOST, "localhost");
 connectProps.setProperty(AdminClient.CONNECTOR\_PORT, "8880");
 AdminClient adminClient = null;
 try {
     adminClient = AdminClientFactory.createAdminClient(connectProps);
 }
 catch (ConnectorException e) {
     System.out.println("Exception creating admin client: " + e);
 }
 ObjectName queryName = new ObjectName("WebSphere:*,type=FailedEventManager");
 ObjectName nodeAgent = null;
 Set s = adminClient.queryNames(queryName, null);
 if(!s.isEmpty())
     nodeAgent = (ObjectName) s.iterator().next();
 else
     System.out.println("Failed Event Manager MBean was not found");
 

 If security is enabled on the server, then the following properties have to set.
 
 connectProps.setProperty(AdminClient.CONNECTOR\_SECURITY\_ENABLED, "true");
 connectProps.setProperty(AdminClient.USERNAME, "test2");
 connectProps.setProperty(AdminClient.PASSWORD, "user24test");
 connectProps.setProperty(AdminClient.CACHE\_DISABLED, "false");
 connectProps.setProperty("javax.net.ssl.trustStore", "C:/WebSphere/AppServer/etc/DummyClientTrustFile.jks");
 connectProps.setProperty("javax.net.ssl.keyStore", "C:/WebSphere/AppServer/etc/DummyClientKeyFile.jks");
 connectProps.setProperty("javax.net.ssl.trustStorePassword", "WebAS");
 connectProps.setProperty("javax.net.ssl.keyStorePassword", "WebAS");
 

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
discardAll()
Delete all failed events.

void
discardFailedEvents(java.util.List<FailedEvent> failedEvents)
Delete failed events for a set of specified message IDs.

void
discardFailedEvents(java.lang.String[] msgIds)
Deprecated. 
since 6.2 Use discardFailedEvents(List failedEvents) instead.

java.util.List
getAllFailedEvents(int pagesize)
Get all the events that have failed so far.

BFMHoldQueueEvent
getEventDetailForBFMHold(FailedEvent fe)
Get the detailed information for a BFMHLD failed event.

BPCEvent
getEventDetailForBPC(FailedEvent failedEvent)
Get the detailed information for a BPC failed event.

JMSEvent
getEventDetailForJMS(FailedEvent failedEvent) 

MQEvent
getEventDetailForMQ(FailedEvent failedEvent) 

SCAEvent
getEventDetailForSCA(FailedEvent failedEvent)
Get the detailed information for a failed event.

java.lang.String[]
getFailedEventBOTypeNames(int pagesize)
Get business object type names from failed events.

long
getFailedEventCount()
Get the count of all failed events.

long
getFailedEventCount(com.ibm.wbiserver.manualrecovery.QueryFilters queryfilters)
Get the count of all failed events according query filters.

long
getFailedEventCountBySessionId(java.lang.String sessionId)
Get failed event count according to specified session id.

java.util.List
getFailedEventsByES(java.lang.Boolean esQualified,
                   int pagesize)
Search failed events according to event sequencing qualifier.

java.util.List
getFailedEventsByException(java.lang.String exceptionStr,
                          int pagesize)
Search failed events according to exception message.

java.util.List
getFailedEventsBySessionId(java.lang.String sessionId,
                          int pagesize)
Search failed events according to a particular session id.

java.util.List
getFailedEventsByType(java.lang.String BusinessObjectType,
                     int pagesize)
Search failed events according to a particular business object type.

java.util.List
getFailedEventsForDestination(java.lang.String destModuleName,
                             java.lang.String destComponentName,
                             java.lang.String destMethodName,
                             int pagesize)
Deprecated. 
since 6.2 use queryFailedEvents(QueryFilters queryFilters, int offset, int maxRows) instead.

java.util.List
getFailedEventsForSource(java.lang.String sourceModuleName,
                        java.lang.String sourceComponentName,
                        int pagesize)
Search failed events according to a particular source combination.

java.util.List
getFailedEventsForTimePeriod(java.util.Date begin,
                            java.util.Date end,
                            int pagesize)
Deprecated. 
since 6.2 use queryFailedEvents(QueryFilters queryFilters, int offset, int maxRows) instead.

FailedEventWithParameters
getFailedEventWithParameters(java.lang.String msgId)
Deprecated. 
since 6.2 use getEventDetailForSCA(FailedEvent failedEvent) instead.

java.util.List
queryFailedEvents(com.ibm.wbiserver.manualrecovery.QueryFilters queryFilters,
                 int offset,
                 int maxRows)
Search failed events according to queryfilers.

void
resubmitFailedEvents(java.util.List failedEvents)
Resubmit a list of failed events.

void
resubmitFailedEvents(java.lang.String[] msgIds)
Deprecated. 
since 6.2 use resubmitFailedEvents(List failedEvents) instead

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getFailedEventCount
long getFailedEventCount()
                         throws FailedEventReadException
Get the count of all failed events.

 
 Sample code:
 
 String opName = "getFailedEventCount";
 Long failedEventCount = (Long) adminClient.invoke(nodeAgent, opName, null, null);
 
Returns:the count of all failed events
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventCount
long getFailedEventCount(com.ibm.wbiserver.manualrecovery.QueryFilters queryfilters)
                         throws FailedEventReadException
Get the count of all failed events according query filters.

 
 Sample code:
 
 String opName = "getFailedEventCount";
 QueryFilters queryFilters = new QueryFilters();
 queryFilters.setFilter(queryFilters.MODULE\_NAME, "testAsync");
 Object [] event\_type = {FailedEvent.TYPE\_SCA,FailedEvent.TYPE\_JMS};
 queryFilters.setFilterArray(queryFilters.EVENT\_TYPE, event\_type);
 Object[] parameters = new Object[] {queryFilters};
 String[] signature = new String[] {"com.ibm.wbiserver.manualrecovery.QueryFilters"}
 Long failedEventCount = (Long)adminClient.invoke(nodeAgent, opName, parameters, signature);
 

 QueryFilters can be used is listed as below:
 
  "MODULE\_NAME", "COMPONENT\_NAME", "OPERATION\_NAME", "BEGIN\_TIME", "END\_TIME", "DEPLOYMENT\_TARGET","EVENT\_TYPE" and "EVENT\_STATUS"
  For "EVENT\_TYPE" and "EVENT\_STATUS" can be set as array:
  Event\_Type with: "BPC", "SCA", "JMS", "BFMHold", "MQ"
  Event\_status with: 1 for failed, 4 for terminated, 5 for stopped
 
Returns:the count of all failed events
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getAllFailedEvents
java.util.List getAllFailedEvents(int pagesize)
                                  throws FailedEventReadException
Get all the events that have failed so far.

 
 Sample code:
 
 String opName = "getAllFailedEvents";
 //pagesize of 0 means all failed events will be returned.
 Object[] params = new Object[] {new Integer(0)};
 String[] signature = new String[] {"int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 //Obtain failed event information in the list.
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:pagesize - the maximum rows returned.
                 pagesize<0, return an empty list;
                 pagesize>0, return at most the specified rows;
                 pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - queryFailedEvents
java.util.List queryFailedEvents(com.ibm.wbiserver.manualrecovery.QueryFilters queryFilters,
                               int offset,
                               int maxRows)
                                 throws FailedEventReadException
Search failed events according to queryfilers.
 
 Sample code:
 
 String opName = "queryFailedEvents";
 QueryFilters queryFilters = new QueryFilters();
 queryFilters.setFilter(queryFilters.MODULE\_NAME, "testAsync");
 Object [] event\_type = {FailedEvent.TYPE\_SCA,FailedEvent.TYPE\_JMS};
 queryFilters.setFilterArray(queryFilters.EVENT\_TYPE, event\_type);
 Object[] params = new Object[] {queryfilter,0,0};
 String[] signature = new String[] {"com.ibm.wbiserver.manualrecovery.QueryFilters","int","int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:queryFilters - Filters used to query failed eventsoffset - This is supported from 7.5 onwards. This indicates the
                          number of failed events that will be skipped in the returned result.
                          The result is ordered by decreasing failure timestamp.maxRows - the maximum rows returned.
                          maxRows<0, return an empty list;
                          maxRows>0, return at most the specified rows;
                          maxRows=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsForDestination
java.util.List getFailedEventsForDestination(java.lang.String destModuleName,
                                           java.lang.String destComponentName,
                                           java.lang.String destMethodName,
                                           int pagesize)
                                             throws FailedEventReadException
Deprecated. since 6.2 use queryFailedEvents(QueryFilters queryFilters, int offset, int maxRows) instead.
Search failed events according to a particular destination combination.

 
 Sample code:
 
 String opName = "getFailedEventsForDestination";
 Object[] params = new Object[] {"Destination\_module\_name", "Destination\_component\_name", "Destination\_method\_name", new Integer(0)};
 String[] signature = new String[] {"java.lang.String", "java.lang.String", "java.lang.String", "int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:destModuleName - destination module name.
                          wildcard search supported for asterisk (*).
                          searching criteria ignored if not assigned or empty String.destComponentName - destination component name.
                          wildcard search supported for asterisk (*).
                          searching criteria ignored if not assigned or empty String.destMethodName - destination method name.
                          wildcard search supported for asterisk (*).
                          searching criteria ignored if not assigned or empty String.pagesize - the maximum rows returned.
                          pagesize<0, return an empty list;
                          pagesize>0, return at most the specified rows;
                          pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsForSource
java.util.List getFailedEventsForSource(java.lang.String sourceModuleName,
                                      java.lang.String sourceComponentName,
                                      int pagesize)
                                        throws FailedEventReadException
Search failed events according to a particular source combination.
 This API is for SCA failed events only.

 
 Sample code:
 
 String opName = "getFailedEventsForSource";
 Object[] params = new Object[] {"Source\_module\_name", "Source\_component\_name", new Integer(0)};
 String[] signature = new String[] {"java.lang.String", "java.lang.String", "int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:sourceModuleName - source module name.
                            wildcard search supported for asterisk (*).
                            searching criteria ignored if not assigned or empty String.sourceComponentName - source component name.
                            wildcard search supported for asterisk (*).
                            searching criteria ignored if not assigned or empty String.pagesize - the maximum rows returned.
                            pagesize<0, return an empty list;
                            pagesize>0, return at most the specified rows;
                            pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsForTimePeriod
java.util.List getFailedEventsForTimePeriod(java.util.Date begin,
                                          java.util.Date end,
                                          int pagesize)
                                            throws FailedEventReadException
Deprecated. since 6.2 use queryFailedEvents(QueryFilters queryFilters, int offset, int maxRows) instead.
Search failed events according to a particular time period.

 
 Sample code:
 
 String opName = "getFailedEventsForTimePeriod";
 SimpleDateFormat dataFormat = new SimpleDateFormat("yyyy-MM-dd");
 Date begin = dataFormat.parse("2000-01-01");
 Date end = dataFormat.parse("2010-01-01");
 Object[] params = new Object[] {begin, end, new Integer(0)};
 String[] signature = new String[] {"java.util.Date", "java.util.Date", "int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:begin - the starting time. if not assigned, the starting criteria will not be appliedend - the ending time. if not assigned, current time will be applied.pagesize - the maximum rows returned.
                 pagesize<0, return an empty list;
                 pagesize>0, return at most the specified rows;
                 pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventBOTypeNames
java.lang.String[] getFailedEventBOTypeNames(int pagesize)
                                             throws FailedEventReadException
Get business object type names from failed events.
 This API is for SCA failed events only.

 
 Sample code:
 
 String opName = "getFailedEventBOTypeNames";
 Object[] params = new Object[] {new Integer(0)};
 String[] signature = new String[] {"int"};
 String[] boTypeNames = (String[]) adminClient.invoke(nodeAgent, opName, params, signature);
 
Parameters:pagesize - the maximum rows returned.
                 pagesize<0, return an empty list;
                 pagesize>0, return at most the specified rows;
                 pagesize=0, unlimited.
Returns:array of BO type names
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsByType
java.util.List getFailedEventsByType(java.lang.String BusinessObjectType,
                                   int pagesize)
                                     throws FailedEventReadException
Search failed events according to a particular business object type.
 This API is for SCA failed events only.

 
 Sample code:
 
 String opName = "getFailedEventsByType";
 //asterisk symbol indicates wildcard searching.
 Object[] params = new Object[] {"*BusinessObjectType*", new Integer(0)};
 String[] signature = new String[] {"java.lang.String", "int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:BusinessObjectType - business object type name.
                           wildcard search supported for asterisk (*).
                           searching criteria ignored if not assigned or empty String.pagesize - the maximum rows returned.
                 pagesize<0, return an empty list;
                 pagesize>0, return at most the specified rows;
                 pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsByException
java.util.List getFailedEventsByException(java.lang.String exceptionStr,
                                        int pagesize)
                                          throws FailedEventReadException
Search failed events according to exception message.
 This API is for SCA failed events only.

 
 Sample code:
 
 String opName = "getFailedEventsByException";
 //asterisk symbol indicates wildcard searching.
 Object[] params = new Object[] {"*RuntimeException*", new Integer(0)};
 String[] signature = new String[] {"java.lang.String", "int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:exceptionStr - exception message.
                     wildcard search supported for asterisk (*).
                     searching criteria ignored if not assigned or empty String.pagesize - the maximum rows returned.
                 pagesize<0, return an empty list;
                 pagesize>0, return at most the specified rows;
                 pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventCountBySessionId
long getFailedEventCountBySessionId(java.lang.String sessionId)
                                    throws FailedEventReadException
Get failed event count according to specified session id.
 This API is for SCA failed events only.

 
 Sample coce:
 
 String opName = "getFailedEventCountBySessionId";
 Object[] params = new Object[] {"Session\_ID"};
 String[] signature = new String[] {"java.lang.String"};
 Long feCount = (Long) adminClient.invoke(nodeAgent, opName, params, signature);
 
Parameters:sessionId - session id
Returns:count of failed events
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsBySessionId
java.util.List getFailedEventsBySessionId(java.lang.String sessionId,
                                        int pagesize)
                                          throws FailedEventReadException
Search failed events according to a particular session id.
 This API is for SCA failed events only.

 
 Sample code:
 
 String opName = "getFailedEventsBySessionId";
 Object[] params = new Object[] {"Session\_ID", new Integer(0)};
 String[] signature = new String[] {"java.lang.String", "int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);
 Iterator it = failedEventList.iterator();
 while(it.hasNext()) {
     FailedEvent failedEvent = (FailedEvent) it.next();
     String msgId = failedEvent.getMsgId();
     System.out.println(msgId);
 }
 
Parameters:sessionId - session idpagesize - the maximum rows returned.
                 pagesize<0, return an empty list;
                 pagesize>0, return at most the specified rows;
                 pagesize=0, unlimited.
Returns:failed event list
Throws:
FailedEventReadException - when error happens when retrieving failed event information
    - getFailedEventsByES
java.util.List getFailedEventsByES(java.lang.Boolean esQualified,
                                 int pagesize)
                                   throws FailedEventReadException
Search failed events according to event sequencing qualifier.
 This API is for SCA failed events only.
Parameters:esQualified - Boolean.TRUE if ES-qualified
                    Boolean.FALSE if not ES-qualified
                    null not applicablepagesize - 
Returns:failed event list
Throws:
FailedEventReadException
    - getFailedEventWithParameters
FailedEventWithParameters getFailedEventWithParameters(java.lang.String msgId)
                                                       throws FailedEventDataException
Deprecated. since 6.2 use getEventDetailForSCA(FailedEvent failedEvent) instead.
Get the detailed information for a failed event.

 
 Sample code:
 
 String opName = "getFailedEventWithParameters";
 Object[] params = new Object[] {"Message\_ID"};
 String[] signature = new String[] {"java.lang.String"};
 FailedEventWithParameters failedEventWithParameters = (FailedEventWithParameters) adminClient.invoke(nodeAgent, opName, params, signature);
 //CEI trace level and expiration time
 String ceiTrace = failedEventWithParameters.getCEITraceControl();
 Date expirationTime =  failedEventWithParameters.getExpirationTime();
 //Business Object parameters
 List paramList = failedEventWithParameters.getFailedEventParameters(adminClient.getConnectorProperties());
 Iterator it = paramList.iterator();
 while(it.hasNext()) {
     //Each parameter is of FailedEventParameter type.
     FailedEventParameter failedEventParameter = (FailedEventParameter) it.next();
     System.out.println("parameter name is: " + failedEventParameter.getName());
     System.out.println("parameter type is: " + failedEventParameter.getType());
     System.out.println("parameter value is: " + failedEventParameter.getValue());
 }
 
Parameters:msgId - message id
Returns:failed event details with parameter information
Throws:
FailedEventDataException - when error happens when obtaining failed event detailed information
    - getEventDetailForSCA
SCAEvent getEventDetailForSCA(FailedEvent failedEvent)
                              throws FailedEventDataException
Get the detailed information for a failed event.

 
 Sample code:
 
 String opName = "getEventDetailForSCA";
 Object[] params = new Object[] {failedevent};
 String[] signature = new String[] {"com.ibm.wbiserver.manualrecovery.FailedEvent"};
 SCAEvent failedEventWithParameters = (SCAEvent) adminClient.invoke(nodeAgent, opName, params, signature);
 //CEI trace level and expiration time
 String ceiTrace = failedEventWithParameters.getCEITraceControl();
 Date expirationTime =  failedEventWithParameters.getExpirationTime();
 //Business Object parameters
 List paramList = failedEventWithParameters.getFailedEventParameters(adminClient.getConnectorProperties());
 Iterator it = paramList.iterator();
 while(it.hasNext()) {
     //Each parameter is of FailedEventParameter type.
     FailedEventParameter failedEventParameter = (FailedEventParameter) it.next();
     System.out.println("parameter name is: " + failedEventParameter.getName());
     System.out.println("parameter type is: " + failedEventParameter.getType());
     System.out.println("parameter value is: " + failedEventParameter.getValue());
 }
 
Parameters:failedEvent - 
Returns:SCAEvent
Throws:
FailedEventDataException
    - getEventDetailForBPC
BPCEvent getEventDetailForBPC(FailedEvent failedEvent)
                              throws FailedEventDataException
Get the detailed information for a BPC failed event.

 
 Sample code:
 
 String opName = "getEventDetailForBPC";
 Object[] params = new Object[] {failedevent};
 String[] signature = new String[] {"com.ibm.wbiserver.manualrecovery.FailedEvent"};
 BPCEvent bpcEvent = (BPCEvent) adminClient.invoke(nodeAgent, opName, params, signature);
 //Business Object parameters
 List paramList = bpcEvent.getInputMessage(adminClient.getConnectorProperties());
 Iterator it = paramList.iterator();
 while(it.hasNext()) {
     //Each parameter is of FailedEventParameter type.
     FailedEventParameter failedEventParameter = (FailedEventParameter) it.next();
     System.out.println("parameter name is: " + failedEventParameter.getName());
     System.out.println("parameter type is: " + failedEventParameter.getType());
     System.out.println("parameter value is: " + failedEventParameter.getValue());
 }
 
Parameters:failedEvent - 
Returns:BPCEvent
Throws:
FailedEventDataException
    - getEventDetailForBFMHold
BFMHoldQueueEvent getEventDetailForBFMHold(FailedEvent fe)
                                           throws FailedEventDataException
Get the detailed information for a BFMHLD failed event.

 
 Sample code:
 
 String opName = "getEventDetailForBFMHold";
 Object[] params = new Object[] {failedevent};
 String[] signature = new String[] {"com.ibm.wbiserver.manualrecovery.FailedEvent"};
 BFMHoldQueueEvent hldEvent = (BFMHoldQueueEvent) adminClient.invoke(nodeAgent, opName, params, signature);
 //Business Object parameters
 String piid = hldEvent.getPIID();
 System.out.println("The related process instance id is: "+piid);
 
Parameters:fe - 
Returns:BFMHoldQueueEvent
Throws:
FailedEventDataException
    - getEventDetailForJMS
JMSEvent getEventDetailForJMS(FailedEvent failedEvent)
                              throws FailedEventDataException
Parameters:failedEvent - 
Returns:
Throws:
FailedEventDataException
    - getEventDetailForMQ
MQEvent getEventDetailForMQ(FailedEvent failedEvent)
                            throws FailedEventDataException
Parameters:failedEvent - 
Returns:
Throws:
FailedEventDataException
    - discardAll
void discardAll()
                throws DiscardFailedException
Delete all failed events.
 If some of failed events are not deleted successfully, the exception information
 will be reported in DiscardFailedException. Other successful deletions are committed.

 
 Sample code:
 
 String opName = "discardAll";
 try {
     adminClient.invoke(nodeAgent, opName, null, null);
 }
 catch (MBeanException e) {
     e.printStackTrace();
     if(e.getTargetException() instanceof DiscardFailedException) {
         FailedEventExceptionReport[] exceptionReports = ((DiscardFailedException) e.getTargetException()).getFailedEventExceptionReports();
         for(int i=0; i<exceptionReports.length; i++)
             System.out.println("Message id: " + exceptionReports[i].getMsgId());
             System.out.println("Failure time: " + exceptionReports[i].getExceptionTime());
             System.out.println("Failure detail: " + exceptionReports[i].getExceptionDetail());
     }
 }
 
Throws:
DiscardFailedException - when error happens when deleting failed event information
    - discardFailedEvents
void discardFailedEvents(java.lang.String[] msgIds)
                         throws DiscardFailedException
Deprecated. since 6.2 Use discardFailedEvents(List failedEvents) instead.
Delete failed events for a set of specified message IDs.
 If some of failed events are not deleted successfully, the exception information
 will be reported in DiscardFailedException. Other successful deletions are committed.

 This API is for SCA failed events only.

 
 Sample code:
 
 String opName = "discardFailedEvents";
 Object[] params = new Object[] {new String[] {"Message\_ID\_1", "Message\_ID\_2"}};
 String[] signature = new String[] {"[Ljava.lang.String;"};
 try {
     adminClient.invoke(nodeAgent, opName, params, signature);
 }
 catch(MBeanException e) {
     e.printStackTrace();
     if(e.getTargetException() instanceof DiscardFailedException) {
         FailedEventExceptionReport[] exceptionReports = ((DiscardFailedException) e.getTargetException()).getFailedEventExceptionReports();
         for(int i=0; i<exceptionReports.length; i++)
             System.out.println("Message id: " + exceptionReports[i].getMsgId());
             System.out.println("Failure time: " + exceptionReports[i].getExceptionTime());
             System.out.println("Failure detail: " + exceptionReports[i].getExceptionDetail());
     }
 }
 
Parameters:msgIds - an array of failed event message IDs
Throws:
DiscardFailedException - when error happens when deleting failed event information
    - discardFailedEvents
void discardFailedEvents(java.util.List<FailedEvent> failedEvents)
                         throws DiscardFailedException
Delete failed events for a set of specified message IDs.
 If some of failed events are not deleted successfully, the exception information
 will be reported in DiscardFailedException. Other successful deletions are committed.

 
 Sample code:
 
 String opName = "getAllFailedEvents";
 Object[] params = new Object[] {new Integer(0)};
 String[] signature = new String[] {"int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);

 String opName = "discardFailedEvents";";
 Object[] params = new Object[] {failedEventList};
 String[] signature = new String[] {"java.util.List"};
 try {
     adminClient.invoke(nodeAgent, opName, params, signature);
 }
 catch(MBeanException e) {
     e.printStackTrace();
     if(e.getTargetException() instanceof DiscardFailedException) {
         FailedEventExceptionReport[] exceptionReports = ((DiscardFailedException) e.getTargetException()).getFailedEventExceptionReports();
         for(int i=0; i<exceptionReports.length; i++)
             System.out.println("Message id: " + exceptionReports[i].getMsgId());
             System.out.println("Failure time: " + exceptionReports[i].getExceptionTime());
             System.out.println("Failure detail: " + exceptionReports[i].getExceptionDetail());
     }
 }
 
Parameters:failedEvents - a list of failed events
Throws:
DiscardFailedException - when error happens when deleting failed event information
    - resubmitFailedEvents
void resubmitFailedEvents(java.util.List failedEvents)
                          throws ResubmissionFailedException
Resubmit a list of failed events.
 If some of failed events are not resubmitted successfully, the exception information
 will be reported in ResubmissionFailedException. Other successful resubmissions are
 committed.

 
 Sample code:
 
 String opName = "getAllFailedEvents";
 Object[] params = new Object[] {new Integer(0)};
 String[] signature = new String[] {"int"};
 List failedEventList = (List) adminClient.invoke(nodeAgent, opName, params, signature);

 String opName = "resubmitFailedEvents";
 Object[] params = new Object[] {failedEventList};
 String[] signature = new String[] {"java.util.List"};
 try {
     adminClient.invoke(nodeAgent, opName, params, signature);
 }
 catch(MBeanException e) {
     e.printStackTrace();
     if(e.getTargetException() instanceof ResubmissionFailedException) {
         FailedEventExceptionReport[] exceptionReports = ((ResubmissionFailedException) e.getTargetException()).getFailedEventExceptionReports();
         for(int i=0; i<exceptionReports.length; i++)
             System.out.println("Message id: " + exceptionReports[i].getMsgId());
             System.out.println("Failure time: " + exceptionReports[i].getExceptionTime());
             System.out.println("Failure detail: " + exceptionReports[i].getExceptionDetail());
     }
 }
 
Parameters:failedEvents - a list of failed events, each of which is
                     either a valid failed event, or a message id
Throws:
ResubmissionFailedException - when error happens when resubmitting failed event information
    - resubmitFailedEvents
void resubmitFailedEvents(java.lang.String[] msgIds)
                          throws ResubmissionFailedException
Deprecated. since 6.2 use resubmitFailedEvents(List failedEvents) instead
Resubmit failed events for a set of specified message IDs.
 If some of failed events are not resubmitted successfully, the exception information
 will be reported in ResubmissionFailedException. Other successful resubmissions are
 committed.

 
 Sample code:
 
 String opName = "resubmitFailedEvents";
 Object[] params = new Object[] {new String[] {"Message\_ID\_1", "Message\_ID\_2"}};
 String[] signature = new String[] {"[Ljava.lang.String;"};
 try {
     adminClient.invoke(nodeAgent, opName, params, signature);
 }
 catch(MBeanException e) {
     e.printStackTrace();
     if(e.getTargetException() instanceof ResubmissionFailedException) {
         FailedEventExceptionReport[] exceptionReports = ((ResubmissionFailedException) e.getTargetException()).getFailedEventExceptionReports();
         for(int i=0; i<exceptionReports.length; i++)
             System.out.println("Message id: " + exceptionReports[i].getMsgId());
             System.out.println("Failure time: " + exceptionReports[i].getExceptionTime());
             System.out.println("Failure detail: " + exceptionReports[i].getExceptionDetail());
     }
 }
 
Parameters:msgIds - an array of failed event message IDs
Throws:
ResubmissionFailedException - when error happens when resubmitting failed event information