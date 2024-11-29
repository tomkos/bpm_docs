# Existing Java integration implementations may throw exceptions when using the WebSphere
Javamail library

Business Automation Workflow V18.0.0.1 and later loads the
following two Javamail libraries at run time:

- The recommended newer and SSL-secured Business Automation Workflow Javamail library that is located in the following file path:
WAS\_INSTALL\_HOME/BPM/Lombardi/lib/mail.jar
- The older WebSphere Javamail library that is located in the following file
path:WAS\_INSTALL\_HOME/plugins/com.ibm.ws.prereq.javamail.jar

When you have an existing Java integration implementation that uses the WebSphere Javamail
library, you may experience exceptions similar to the following one:

```
Caused by: java.lang.ClassCastException: javax.mail.Session incompatible with javax.mail.Session
at com.ibm.db.email.util.EmailSessionHandler.<init>(EmailSessionHandler.java:24)
at com.ibm.db.email.EmailClient.sendMessage(EmailClient.java:70)
```

To resolve this problem, you must create a new mail provider and specify the more secure Business Automation Workflow
mail.jar file in its classpath. For information about how to create a new mail
provider and session attach to it, see the help topic Configuring mail providers and sessions.

When you follow the instructions in the help topic, ensure that you select the Isolate
this mail provider check box and then specify the following class path for the mail
provider:

```
WAS\_INSTALL\_HOME/BPM/Lombardi/lib/mail.jar
```

When finished, update the mail provider value for the Java integration implementation with the
updated JNDI name that was defined in the new mail session.