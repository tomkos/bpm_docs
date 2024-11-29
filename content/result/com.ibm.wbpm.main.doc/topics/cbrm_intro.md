<!-- image -->

# Business rule management programming

You can use business rules management classes in a web application
where they are combined with other management capabilities for things
such as a BPEL process or human tasks in order to manage all components
from a single client. Any custom management clients can be used along
side the business process rules manager web application. You can also use the classes to automate changes to business
rules within an application. For example, business rules might be
changed when the result of a business process, which uses the business
rules, exceeds some threshold or limit.

The business rule management classes must be used in an application
installed on the process server. The classes do not provide a remote
interface, however you can wrap them in a facade that is then exposed
by a specific protocol for remote execution.

<!-- image -->

- Programming model

IBM Integration Designer business rules are authored with two different authoring tools and issued by the rule run time. All three environments share the same model for the business rule artifacts.
- Business rules manager examples

A number of examples are provided that show how the different classes can be used to retrieve business rule groups and to make modifications to rule sets and decision tables. The examples are provided in a project interchange file (ZIP) that can be imported into IBM® Integration Designer where they can be browsed and reused.
- Common operations classes

This section contains additional classes that were used in the examples to simplify common operations.