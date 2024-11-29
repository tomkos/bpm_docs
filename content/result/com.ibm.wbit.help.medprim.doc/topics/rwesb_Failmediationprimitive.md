# Fail mediation primitive

## Introduction

You can use the Fail mediation
primitive to halt a mediation flow and raise an exception at a point
you choose in the flow. You can also add information about a failure.

The
Fail mediation primitive has one input terminal (in).
The input terminal is wired to accept a message that triggers a FailFlowException.
A FailFlowException is a specific runtime exception
that causes the flow instance to fail. You can wire the output terminal
of another mediation primitive to the in terminal
of a Fail mediation primitive, to cause a FailFlowException.

## Usage

You can use the Fail mediation primitive
to define your own error conditions, based on the business logic of
the flow.

You can use the Error message property
to provide an additional error message that is specific to your business
logic or domain. The Error message you create is
added to the automatically generated exception.

- {0} would be substituted with the Time Stamp value
- {1} would be substituted with the SMO Message ID value
- {2} would be substituted with the Mediation Name value
- {3} would be substituted with the Module Name value
- {4} would be substituted with the SMO part defined by the Root
property XPath. By default this is /context/failInfo
- {5} would be substituted with the SMO Version value

```
'29/04/09 15:11, 9A85B1D2-0119-4000-E000-13E4091443BC, Fail1, MyModule, <failInfo>...</failInfo>, 6'
```

You
can use the Fail mediation primitive to roll back a global transaction
under certain conditions. For example, if you wire an output terminal
of a Message Filter mediation primitive to a Fail mediation primitive,
the transaction is rolled back if the filter condition occurs.

- Fail mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)