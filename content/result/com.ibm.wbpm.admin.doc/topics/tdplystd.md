<!-- image -->

# Deploying your application with a stand-alone adapter

## About this task

Learn how to how to deploy a stand-alone adapter, how to set up a Java Naming and Directory
Interface (JNDI) service for an application that uses an adapter, and then how to install an
application on an application server that has a stand-alone adapter.

- Deploying a stand-alone adapter

You deploy a stand-alone adapter to an application cluster. Then, application adapter bindings and related Java Naming and Directory Interface (JNDI) services can refer to it.
- Creating a JNDI adapter reference for an application

When a stand-alone adapter is deployed to a cluster, the application must provide a JNDI reference to the related adapter binding configuration of the stand-alone adapter to use the JNDI resources.
- Installing applications associated with a stand-alone adapter

When you deploy an application that uses a stand-alone adapter, extra steps are needed to reference the adapter.