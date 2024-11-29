<!-- image -->

# EJB bindings

- EJB import bindings

EJB import bindings allow an SCA module to call EJB implementations by specifying the way that the consuming module is bound to the external EJB. Importing services from an external EJB implementation allows users to plug their business logic into the IBM® Integration Designer environment and participate in a business process.
- EJB export bindings

External Java™ EE applications can invoke an SCA component by way of an EJB export binding. Using an EJB export lets you expose SCA components so that external Java EE applications can invoke those components using the EJB programming model.
- EJB binding properties

EJB import bindings use their configured JNDI names to determine the EJB programming model level and type of invocation (local or remote). EJB import and export bindings use the JAX-WS data handler for data transformation. The EJB import binding uses an EJB import function selector and an EJB fault selector, and the EJB export binding uses an EJB export function selector.