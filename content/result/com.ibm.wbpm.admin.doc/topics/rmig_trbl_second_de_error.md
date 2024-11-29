# Error message when creating a second deployment environment

```
SystemErr     R Caused by: javax.management.MBeanException: Exception thrown in RequiredModelMBean while trying to invoke operation getApplicationInfo
SystemErr     R     at com.ibm.ws.management.connector.soap.SOAPConnectorClient.handleAdminFault(SOAPConnectorClient.java:959)
SystemErr     R     at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invokeTemplateOnce(SOAPConnectorClient.java:924)
SystemErr     R     at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invokeTemplate(SOAPConnectorClient.java:689)
SystemErr     R     at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invokeTemplate(SOAPConnectorClient.java:679)
SystemErr     R     at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invoke(SOAPConnectorClient.java:665)
SystemErr     R     at com.ibm.ws.management.connector.soap.SOAPConnectorClient.invoke(SOAPConnectorClient.java:487)
SystemErr     R     at com.sun.proxy.$Proxy161.invoke(Unknown Source)
SystemErr     R     at com.ibm.ws.management.AdminClientImpl.invoke(AdminClientImpl.java:224)
SystemErr     R     at com.ibm.websphere.management.application.AppManagementProxy.proxyInvoke(AppManagementProxy.java:186)
SystemErr     R     ... 20 more
SystemErr     R Caused by: com.ibm.websphere.management.exception.AdminException: ADMA0017E: The context for SchedulerCalendars cannot be obtained. The application does not appear to be installed.
SystemErr     R     at com.ibm.ws.management.application.EditApplication.getApplicationInfo(EditApplication.java:354)
SystemErr     R     at com.ibm.ws.management.application.AppManagementImpl.\_getApplicationInfo(AppManagementImpl.java:647)
SystemErr     R     at com.ibm.ws.management.application.AppManagementImpl.getApplicationInfo(AppManagementImpl.java:623)
```