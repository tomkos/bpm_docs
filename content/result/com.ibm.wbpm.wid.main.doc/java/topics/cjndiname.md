<!-- image -->

# JNDI names

JNDI (Java Naming and Directory Interface) names are used to provide a usable name for a Java objects. IBM® Integration
Designer uses the JNDI name to determine the EJB programming model level and the type of invocation (local or remote). You may sometimes need to provide the JNDI name when creating EJB imports and the format of the JNDI name required in an interface depends on the type of invocation you are using.

| Invocation type   | JNDI name format          |
|-------------------|---------------------------|
| EJB 2.1 (remote)  | com/test/example          |
| EJB 2.1 (local)   | ejblocal:com/test/example |
| EJB 3.0 (remote)  | com.test.example          |
| EJB 3.0 (local)   | ejblocal:com.test.example |