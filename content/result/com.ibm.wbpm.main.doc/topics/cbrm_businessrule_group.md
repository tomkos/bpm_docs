# Business Rule Group

Rule sets and decision tables can only be reached through the business
rule group that they are associated with.  Methods are provided on
the class to retrieve information about the business rule group and
to reach the rule sets and decision tables.  Through the methods the
following information can be retrieved:

- Target name space
- Name of business rule group
- Display name
- Name/Display name synchronization
- Description
- Presentation time zone which indicates whether dates should be
displayed in UTC format or local to the system
- Operations defined in the interface associated with the business
rule group
- Custom properties defined on the business rule group

The different rule sets and decision tables associated with the
business rule group can be reached through the business rule group's
operation.

There are also methods that allow for information to be updated
on the business rule group.  Through the methods, the following information
can be updated:

- Description
- Display name
- Name/Display name synchronization
- Custom properties defined on the business rule group

The Display name for the business rule group can be set explicitly
or it can be set to the value of the Name using the setDisplayNameIsSynchronizedToName
method.

Other values cannot be modified as these are part of the business
rule group component definition and changes to these values would
require a redeploy as well as reinstallation.

The business rule group class also provides a refresh method. 
This method will make a call to the persistent storage or repository
where the business rules are stored and return the business rule group
and all of the associated rule sets and decision tables with the persisted
information.  The returned business rule group is the latest copy
and the previous object is obsolete.

The isShell method can be used to tell if a business rule group
instance is of a version that is not supported by the current runtime.
For example, if a web client was created with the current business
rule management classes, and in the future new capabilities are added
to the business rule group that are not supported by the classes,
a shell business rule group will be created when the business rule
group is retrieved.  This allows the web client to continue to work
with business rules that are supported and still retrieve business
rule groups with limited attributes and capabilities.  When isShell
is true, only the methods getName, getTargetNameSpace, getProperties,
getPropertyValue, and getProperty will return values.  All other methods
will result in an UnsupportedOperationException.  Besides using the
isShell method, the type of the BusinessRuleGroup can also be checked
if it is an instance of BusinessRuleGroupShell in order to determine
if it is of a supported version.

Figure 1. Class diagram of BusinessRuleGroup and
related classes

<!-- image -->