<!-- image -->

# Invoking a synchronous subprocess in another EAR file fails

```
com.ibm.ws.sca.internal.ejb.util.EJBStubAdapter com.ibm.ws.sca.internal.ejb.util.EJBStubAdapter#003 
Exception: 
java.rmi.AccessException: CORBA NO\_PERMISSION 0x49424307 No; nested exception is: 
org.omg.CORBA.NO\_PERMISSION: The WSCredential does not contain a forwardable token. 
Enable Identity Assertion for this scenario. 
vmcid: 0x49424000 minor code: 307 completed: No
at com.ibm.CORBA.iiop.UtilDelegateImpl.mapSystemException(UtilDelegateImpl.java:202)
at javax.rmi.CORBA.Util.mapSystemException(Util.java:84)
```

## Reason

## Resolution

- For CSIv2 inbound authentication, see Configuring Common Secure Interoperability Version
2 inbound communications
- For CSIv2 outbound authentication, see Configuring Common Secure Interoperability Version
2 outbound communications