<!-- image -->

# JMS binding

## Available JMS bindings

IBM® Workflow
Server provides three JMS bindings:

- JMS binding, which is a Service integration bus provider binding, compliant with JMS J2EE
Connector Architecture (JCA) 1.5
- WebSphere MQ JMS binding, providing JMS provider support for WebSphere MQ
- Generic JMS binding, providing support for non-JCA providers, compliant with the JMS 1.1
specification

- Configuring the JMS binding

All JMS bindings provide a common configuration. Depending on the type of JMS binding used, there are minor differences that are highlighted in the configuration descriptions.
- Accessing the JMS header

You can access the JMS header using Java, or the mediation flow component.
- Using dynamic JMS endpoints

You can dynamically invoke services using JMS import bindings. The import that you invoke is decided at run time and does not need to be wired directly to a component. During a dynamic invocation, you do not specify the endpoints that you use in the import bindings. If you use a mediation flow component, you can specify a target import and dynamic endpoint address using some mediation primitives. For example, the Message Element Setter mediation primitive.

<!-- image -->