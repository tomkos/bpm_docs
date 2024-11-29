# Auto stage completion fails in Case Builder with WSIloginModule

## About this task

The following error is seen in Case Builder:

The bus BPM.De1.Bus could not authenticate the user deadmin.

000001c0 SystemOut O JMS exception: javax.jms.JMSSecurityException: CWSIA0004E: The
authentication for the supplied user name deadmin and the associated password was not
successful.

## Procedure

To resolve the problem remove WSILoginModule for the node on
Case Builder. Complete the
following steps:

1. Go to Servers -> SingleClusterMember1 ->
Server Infrastructure -> Java and Process Management
-> Process Definition -> Java Virtual
Machine
2. Under the generic JVM arguments, remove the following line:
-Djava.security.auth.login.config=<pathofJAASfile>
3. Restart Case Builder.