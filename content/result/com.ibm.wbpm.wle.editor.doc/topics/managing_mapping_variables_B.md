# Variable scope

Local variables are accessible only to the currently executing process instance or service.
Because variables are unique to an individual process or service flow, you can use a variable of the
same name in a nested process or service flow and no conflicts occur at run time.

A variable contains a value or refers to an object. Multiple variables can refer to the same
object. When a running process instance or service flow reaches an exit point, the variable value or
references can be propagated to the calling process instance or service flow. When a running process
instance or service flow encounters an activity, the variable values and references can be
propagated to variables within that activity. A variable that is defined as a Shared Object can
persist its values at these boundaries. For more information, see Declaring and passing variables for more details.

All variables in the designer are JavaScript objects.
Namespaces are used to organize these objects and their methods. The following table describes the
namespaces that are most commonly used during process design and development:

| Namespace     | Description                                                      |
|---------------|------------------------------------------------------------------|
| tw            | Top-level  namespace in the designer                             |
| tw.object     | Access  JavaScript objects and business objects (variable types) |
| tw.local      | Access and update process and service-level variables            |
| tw.system     | Access system features and functionality                         |
| tw.system.org | Access security functionality                                    |
| tw.epv        | Access exposed process values (EPVs)                             |
| tw.env        | Access environment variables                                     |