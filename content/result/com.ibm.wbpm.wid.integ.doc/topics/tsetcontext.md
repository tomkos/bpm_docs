<!-- image -->

# Storing and using elements in the message context

## About this task

Follow
these steps to set a property in the correlation or transient context
of your flow:

## Procedure

1. If you do not have an existing business object, create
one in the business object editor, and add the element you want to
persist as a field.
2. Click the request flow tab, and then click the input node.
3. In the Properties view, switch to the Details tab.
4. In the Correlation context or Transient context field,
click Browse.
5. Select a business object in the data type selection window,
and click OK. An empty business
object is created in the message's context section. In the properties
view, the business object now appears in the input node's context
field, as shown below:
6. Initialize the element later in the flow by using a mediation
primitive such as Message Element Setter to store a value in the business
object field.

## What to do next

<!-- image -->

```
/context/transient/oneWayStreet
```

You
can then use the property in the following ways:

- Set a value for the element directly into the business object
field by using a  Message Element Setter or Database Lookup primitive.
- Use the element in an Endpoint Lookup primitive to query the WebSphere® Service Registry
Repository.
- Map the element between the context and the message body by using
a Mapping primitive or a business object map primitive.
- Write your own custom mediation primitive to set or get the element.