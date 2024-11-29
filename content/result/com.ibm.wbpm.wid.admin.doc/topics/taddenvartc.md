<!-- image -->

# Referencing environment variables in the test client

## Procedure

1. In the assembly editor, right-click a component and select Test
Component. The integration test client opens to the Events
page.
2. In the Events area, ensure that the Invoke event
is selected.
3. In the Name column of the value
editor, locate the name of the field for which you want to reference
an environment variable. The field must have a simple data type, such
as string or integer.
4. In the row that contains the field name, type the environment
variable that you want to reference in either the Value column
and then press Enter. Alternatively, you can
select XML editor to open the XML editor and
type the environment variable. Regardless of which approach you use,
you can reference one of the following three types of environment
variables:

Environment variable type
Description

Proprietary
These environment variables are referenced in the test client
or in the test suite editor, but they are generally defined in the
test client, Component Test Explorer, or by using command-line invocation.
The syntax for these environment variables is:${proprietary\_variable\_name}
For
example:
${MY\_VAR}

WebSphere Application Server
These environment variables are defined in the server Administrative
Console and referenced in either the test client or the test suite
editor. The syntax for these environment variables is:$WAS{WAS\_variable\_name}
For
example:
$WAS{INSTALL\_ROOT}

JVM property
These environment variables are defined in the server Administrative
Console and referenced in either the test client or the test suite
editor. The syntax for these environment variables is:$JVM{JVM\_property\_name}
For
example:
$JVM{file.encoding}

If you want, you can concatenate different types of environment
variables using a forward slash (/) character. For example:$WAS{INSTALL\_ROOT}/${MY\_LOG\_DIR\_NAME}
5. If you are referencing an environment variable that will
not have a value defined at run time, you can specify a default value
for the environment variable in the value editor. For example:
${MY\_VAR, customer}
In the example, the default value customer is
specified. If the environment variable is not defined at run time,
it will be substituted by the string customer.
Note: If
your value editor contains environment variables and you plan to export
the value editor to an XML file, you need to exercise caution. Environment
variables that are referenced in the value editor are generally defined
at run time rather than in the value editor, which means that they
will be exported from the value editor to the XML file "as is" with
only a name and without any defined value. However, if you have specified
a default value for the environment variable in the value editor,
it will be exported to the XML file with the defined value.

## What to do next