<!-- image -->

# WebSphere eXtreme
Scale

IBM Business Automation Workflow  provided functionality that can
improve integration with WebSphere eXtreme
Scale by introducing
two new mediation primitives.

eXtreme Scale is an elastic, scalable, in-memory data grid. The
data grid dynamically caches, partitions, replicates, and manages application data across multiple
servers. eXtreme Scale performs high volumes of
transaction processing with high efficiency and linear scalability. eXtreme Scale provides qualities of service, such as
transactional integrity, high availability, and predictable response times.

You can use mediation flows to access the eXtreme Scale caching function. When you develop a Service
Component Architecture (SCA) module that needs to store information in an eXtreme Scale cache, you must include the WebSphere eXtreme
Scale Store mediation primitive in the mediation flow. If
you want to retrieve information from an eXtreme Scale cache, you
must include the WebSphere eXtreme
Scale Retrieve mediation primitive.
By combining the two mediation primitives in a mediation flow you can cache the response from a
back-end system, so that future requests can retrieve the response from the cache.

To configure access to eXtreme Scale, you must create an eXtreme Scale definition for your IBM Business Automation Workflow profile. An eXtreme Scale definition is the mechanism used by the WebSphere eXtreme
Scale Retrieve and Store mediation primitives to connect
to an eXtreme Scale server.

In IBM Business Automation Workflow, eXtreme Scale definitions are defined using administrative
commands or by using the integrated solutions console. The definitions are accessed through a Java
SPI or through built-in mediation primitives. This chapter describes the benefits of using eXtreme Scale in a IBM Business Automation Workflow environment, the topologies available for
IBM Business Automation Workflow and eXtreme Scale integration, and how to secure the interaction
between products.

- Common WebSphere eXtreme Scale scenarios

You can use WebSphere eXtreme Scale together with IBM Business Automation Workflow in a number of business situations.
- WebSphere eXtreme Scale topologies

You can use different topologies to set up WebSphere eXtreme Scale, dependent on your resource considerations, your existing WebSphere Application Serverset-up, performance considerations, scalability and reliability considerations.
- WebSphere eXtreme Scale authentication

When integrating with a secure WebSphere eXtreme Scale (eXtreme Scale) deployment, IBM Business Automation Workflow must authenticate with the eXtreme Scale catalog server.
- WebSphere eXtreme Scale security aspects

Consider these security aspects before using WebSphere eXtreme Scale (eXtreme Scale) with IBM Business Automation Workflow.
- Administering access to WebSphere eXtreme Scale

Using the administrative console you can create, configure, and view all your WebSphere eXtreme Scale server definitions.

<!-- image -->