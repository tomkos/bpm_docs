<!-- image -->

# EJB 3.0 and EJB 2.1

EJB 3.0 has some significant differences with EJB 2.1.
You should be aware of these differences when developing applications
with EJB bindings based on 3.0 or higher.

EJB 3.0 was a rethinking of Enterprise JavaBeans (EJBs)
based on an analysis of growing difficulties that developers had experienced
as they developed applications using EJBs. The challenges addressed
by EJB 3.0, the differences between EJB 3.0 and its predecessor, EJB
2.1, and a change to the local interface in EJB 3.0 are discussed
below.

## Challenges addressed by EJB 3.0

The EJB
architecture was designed for applications with distributed components.
BeforeEJBs, Common Object Request Broker Architecture (CORBA) had
become one well-known standard that handled distributed objects but
CORBA became complex and synonymous with difficult to use. As the
EJB standard evolved, it too began to pick up many features and acquired
a reputation as being too complex to use for developers. The following
list of complaints were associated with EJBs by the time of EJB 3.0:

- Container-managed persistence made development difficult.
- You could not test EJB modules outside of an EJB container.
- Several interfaces were required plus the implementation of unnecessary
methods.
- The EJBObject and EJBLocalObject interfaces themselves had to
be implemented.
- Many exceptions had to be handled.
- Debugging was difficult when using the EJB container.
- You needed to have in-depth JNDI knowledge.
- The deployment descriptor was awkward to use.

- An Introduction to the Enterprise JavaBeans 3.0 (EJB 3) Specification
- Migrating EJB 2.x applications to EJB 3.0

## Differences between EJB 3.0 and EJB 2.1

For
over a decade EJBs have been a key element of large-scale application
development written in Java. Over this period EJBs evolved into a
standard framework for the development, deployment and execution of
distributed components that are used in multi-user environments. The
framework included services for lifecycle monitoring, concurrency,
pooling resources, transactions, security and persistence.

By
the time of EJB 2.1, these standard features were available to developers
working with EJBs: session beans for non-persistent data and entity
beans for persistent data; an XML deployment descriptor; a local or
home interface though only clients inside the Java 2 Platform Enterprise
Edition container could access it; message-driven beans for asynchronous
messages; and support for web services that exposed an endpoint so
that an EJB could be invoked when needed. The result of these features
though was that developers had to write a lot of code just to create
an EJB. For example, developers needed to code a home interface, a
component interface, a bean class, and a deployment descriptor which
for an entity bean could be itself complex. Developers were also required
to code methods for lifecycle management even if they were not called.

EJB
3.0 introduced the following major changes, which have led to a simplified
programming model:

- The key difference between EJB 3.0 and EJB 2.1 is that entity
beans have been replaced with plain old Java objects (POJOs) now just
called entities. These POJOs do not require an EJB container, special
interfaces or specific EJB code.
- Session beans no longer require a local or EJB-specific interface.
- You no longer need to capture EJB metadata in an XML deployment
descriptor. Instead you can put the EJB metadata in your bean source
code using annotations, which for many developers is much easier.
The XML deployment descriptor is still supported for those applications
where you want to separate Java source from EJB metadata.
- In EJB 2.1 you had to use a JNDI lookup in order to access another
EJB. With EJB 3.0 you can use an annotation (@EJB) to access an EJB,
which simplifies your configuration.
- Persistence was simplified by a published Java Persistence API
that uses standard Create, Read, Update and Delete (CRUD) operations.
- With EJB 2.1 and JAX-RPC the configuration for web services was
difficult as you had to generate WSDL describing the service, create
a service endpoint interface, and a few more tasks. EJB 3.0 using
the Java API for XML Web Services (JAX-WS) works easily with web services
and most of the manual work done in EJB 2.1 is automatically generated
at deployment time.
- Only the major changes have been listed above. The formal JSR
220 for EJB 3.0 is over 800 pages and books about EJB 3.0 range between
400 and 600 pages.

EJB 3.0 is formally defined in JSR 220: Enterprise JavaBeans 3.0.. This JSR
is over 800 pages and is divided into three sections: the Java Persistence
API defines the persistence framework and discusses entities; the
EJB Core Contracts and Requirements section covers message-driven
and session beans; and the EJB Simplified API provides an overview
of the EJB development model;

## How an EJB with a local interface works

Based
on the previous sections, EJB 3.0 led to a significant simplification
of the EJB specification. This is especially true for an EJB with
a local interface (that is, an EJB that will run in the same JVM as
the client). How simple? The following lines of code create an EJB
interface.

```
package ejbeasy;

public interface EasyEJBClaim {
	public void stateClaim(String myName);
}
```

These lines create the implementation in a stateless
session bean.

```
package ejbeasy;

import javax.ejb.Stateless;

@Stateless
public class EasyEJBClaimBean implements EasyEJBClaim {
	public void stateClaim(String myName){
		System.out.println(myName + "says What could be simpler?");
	}
}
```

The interface is a POJO interface and the bean
class is a POJO. The @Stateless annotation converts
the POJO to a stateless EJB.