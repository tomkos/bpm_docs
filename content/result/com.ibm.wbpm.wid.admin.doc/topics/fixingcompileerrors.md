<!-- image -->

# Fixing compilation errors in integration projects

This topic applies only to IBM Business Process Manager
Advanced.

If a process application or toolkit contains content that was authored
in both Process Designer and Integration Designer, you must
take extra caution to avoid unintended or unnoticed breakages.

The set of artifacts visible to a business analyst who is working
in Process Designer is
different from the set seen by the integration developer who is working
in Integration Designer.
For example, a mediation flow that is authored in Integration Designer is not
seen by the business analyst. Conversely, an undercover agent that
is authored in Process Designer is
not seen by the integration developer. However, some artifacts are
visible to both roles, such as data types, business process definitions,
and advanced integration services.

There are dependencies between process applications and toolkits
that enable artifact visibility across project dependencies. For example,
a project dependency in Integration Designer must be
resolved in the scope of the process application or toolkit. If a
module in a process application depends on a library, the library
must be in the same process application as the module or in a dependent
toolkit. Integration developers and business analysts can change these
artifacts or dependencies, which causes problems with artifacts that
are seen only in one component.

To ensure that an entire process application or toolkit is error-free,
open and analyze it in both editors. Using a new workspace in Integration Designer, select
all modules and libraries when you open the process application or
toolkit. After the build is complete, you can see errors in the Problems
view. The examples show two typical problems and suggest ways to resolve
them.

## Example 1

If you move a dependent business
object in Process Designer,
you might need to make changes in Integration Designer. Let's
say you move an artifact in Process Designer from
a process application into a toolkit or another process application.
If the moved artifact or any of its dependencies belong to advanced
contents (for example, an implemented advanced integration service
or a business object referenced by SCA modules or libraries in the
process application), the SCA modules or libraries might fail to build.
In this case, you need to make the appropriate changes to ensure that
the dependent business object is still accessible. You also need to
change related unique resource identifiers in the maps that depend
on the moved business object.

## Example 2

In Process Designer, if
you rename a business object or change the type name or namespace
name in the Advanced Properties page of the Business Objects editor, Integration Designer artifacts
that reference that business object are not synchronized. After you
synchronize the process application with the repository from Integration Designer, broken
references display.

If you find broken references of this kind,
you can correct the situation by manually updating the references
in Integration Designer.
If there are a few errors, this action is the best choice. If you
have many errors, you can revert back to the original name that you
used in Process Designer.
You can also revert back to the original business object XML properties.
You can modify the referencing artifacts as well. When you refresh
the process application in Integration Designer from the
repository, the broken references are corrected.