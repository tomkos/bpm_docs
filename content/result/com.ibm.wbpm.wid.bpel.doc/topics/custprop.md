<!-- image -->

# Using custom properties for human tasks

Search criteria can be defined for tasks, escalations and for the
dynamic people assignment via custom properties.

```
Name = branch, Value = Chicago
Name = skill-level, Value = 3
```

Custom properties are defined on the Environment tab in the properties
area.

There are a number of predefined custom properties, also called
inline custom properties, that allow for optimized queries. Those
properties have predefined names: CUSTOM\_TEXT1 thru CUSTOM\_TEXT8.
The predefined query table (TASK) has corresponding query table attributes
- CUSTOM\_TEXT1 thru CUSTOM\_TEXT8. In order to use inline custom properties,
you choose one of the predefined query table attributes from the drop-down
list in the Custom Property window. When you use an inline custom
property, the name that is entered in the name field is ignored by
the runtime engine, so you must not rely on it.

For more information about query tables, see Query tables in Business Process Choreographer.

## Related concepts

- Replacement variables and context variables
- Using Java methods in process snippets
- Using event handlers

## Related tasks

- Modifying the properties of an activity
- Modifying the type of an activity
- Working with basic activities
- Working with structured activities
- Modeling human workflows

## Related reference

- Environment tab: Human Task editor