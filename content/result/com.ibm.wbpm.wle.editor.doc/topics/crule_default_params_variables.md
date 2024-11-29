# Default rule variables and parameters (deprecated)

## Default Decision service variables

The System
Data toolkit is imported into the Workflow Center repository
so that each process application and toolkit that you create has access
to Business Automation Workflow system
data. The System Data toolkit includes assets that all Business Automation Workflow projects
require, including variable types. The Decision service can use most
of the pre-defined variables and variable types, with a few exceptions.

<!-- image -->

- SQLResult
- XMLDocument
- XMLElement
- XMLNodeList

## Decision service parameters

- A business object name
- A variable type
- A direction, which indicates whether a parameter is used as input
to a Decision service, or output from the Decision service, or both.
The direction setting is determined automatically based on how the
parameter or variable is used in the rule. For example, any parameter
or variable that is referenced in a rule, but is not modified or updated
when the service is running, is identified as an IN variable.