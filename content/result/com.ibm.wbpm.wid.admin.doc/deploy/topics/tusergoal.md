<!-- image -->

# Editing module deployment properties

## Before you begin

## About this task

The following topics describe the key concepts in editing
module deployment properties and explain how to open and use the module
deployment editor.

- Module deployment properties

In IBM Integration Designer, you can use the module deployment editor to specify and retain changes to module deployment properties in deployment descriptor files.
- WS-Security specification

The web services WS-Security specification describes enhancements to SOAP messaging to provide quality of protection through message integrity, message confidentiality, and single message authentication. These mechanisms can be used to accommodate a wide variety of security models and encryption technologies.
- Module deployment editor

In IBM Integration Designer, the module deployment editor is the designated tool for editing module deployment properties for web services exports and imports. It enables you to specify and persist changes to module deployment properties in deployment descriptor files. The module deployment editor features a simple user interface that enables you to easily manage module deployment properties.
- Mappings to Java EE deployment descriptor editors

The module deployment editor maps to several Java EE deployment descriptor editors.
- Opening the module deployment editor

You can open the module deployment editor from the Business Integration view, Physical Resources view, or the assembly diagram of your module.
- Editing WS-Security properties

Using the module deployment editor, you can edit WS-Security properties for your web services exports and imports. The high-level tasks in editing these web services security properties are essentially the same regardless of whether you are securing your exports and imports with authentication, signing, or encryption.
- Implementing authentication

WS-Security supports a variety of security token types for authentication, such as username tokens, binary tokens, and custom tokens. Username tokens are used in basic authentication, whereas binary tokens (like x.509 and LTPA tokens) are used in more advanced forms of authentication. In this release of IBM Integration Designer, the module deployment editor documentation describes how to implement basic authentication using username tokens.
- Creating and assigning security roles to web service exports

In the module deployment editor, you can create and assign security roles to web service exports.
- Binding roles defined in assembly diagrams

In the Module Deployment editor, you can bind security roles that are defined in your assembly diagrams, such as the roles related to security identity and permission.
- Changing URLs for web service exports

In the module deployment editor, you can change the endpoint (URL) of an SCA export with a SOAP/HTTP web service binding, including both the context root and the URL mapping.
- Adding JAX-RPC handlers for web service exports

In the module deployment editor, you can add a JAX-RPC handler before an SCA export with a SOAP1.1/HTTP using a JAX-RPC web service binding or a SOAP1.1/JMS web service binding and change the message request.
- Adding JAX-RPC handlers for web service imports

In the module deployment editor, you can add a JAX-RPC handler after an SCA import with a SOAP1.1/HTTP using JAX-RPC web service binding or a SOAP1.1/JMS web service binding and change the message request.
- Using a resource reference in an assembly diagram

In the module deployment editor, you can add a resource reference that enables a Java component in the assembly diagram to access the resource. For example, you can add a JDBC data source reference that enables a Java component in the assembly diagram to access data in a relational database.
- Limitations of the module deployment editor

From time to time, you may encounter some limitations in using the module deployment editor.