<!-- image -->

# Accessing the EJB APIs

## About this task

The BusinessFlowManagerService interface provides the methods
for BPEL process applications, and the HumanTaskManagerService interface
provides the methods for task-based applications. The application can be any Java™ application,
including another Enterprise JavaBeans (EJB) application.

- Accessing the remote interface of the session bean

An EJB client application for BPEL processes or human tasks accesses the remote interface of the session bean through the remote home interface of the bean.
- Accessing the local interface of the session bean

An EJB client application for BPEL processes or human tasks accesses the local interface of the session bean through the local home interface of the bean.