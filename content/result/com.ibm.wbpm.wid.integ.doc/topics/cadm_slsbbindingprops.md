<!-- image -->

# EJB binding properties

- JNDI names and EJB import bindings

When it configures the EJB binding on an import, Integration Designer uses the JNDI name to determine the EJB programming model level and type of invocation (local or remote).
- JAX-WS data handler

The Enterprise JavaBeans (EJB) import binding uses the JAX-WS data handler to turn request business objects into Java™ object parameters and to turn the Java object return value into the response business object. The EJB export binding uses the JAX-WS data handler to turn request EJBs into request business objects and to turn the response business object into a return value.
- EJB fault selector

The EJB fault selector determines if an EJB invocation has resulted in a fault, a runtime exception, or a successful response.
- EJB function selector

The EJB bindings use an import function selector (for outbound processing) or an export function selector (for inbound processing) to determine the EJB method to call.