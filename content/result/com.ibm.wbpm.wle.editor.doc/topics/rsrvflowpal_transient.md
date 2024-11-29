# Using transient variables in service flows

Transient variables are private service flow variables that are not persisted in the database as
part of the execution context of a service flow. Use cases for transient variables include
performance optimization and preventing persistent storage of sensitive information such as API
keys. The value of a transient variable lives in memory for the time that its service flow is being
executed on the same thread.

You can mark any variable that is created as a private variable on the service flow's
Variables tab as transient by selecting Is transient
in the Details section.

Such variables are not written to the database even if an activity specifies Save
execution context on the General tab. Variables of a shared
business object type cannot be transient. The concept of a transient variable contradicts the
concept of a shared business object.

The transience behavior of a variable is scoped to its service flow. To preserve the transience
of the information, you should never assign the value of a transient variable to a non-transient
variable, assign the value of a transient variable to a parameter in the data mapping of an
activity, or use a transient variable for a tracking event.