# Using formatting with variables in a heritage coach (deprecated)

You can apply formatting to a heritage coach control that is bound to a variable. All input
values are treated as numbers, even if they are bound to string variables.

If you create a service that includes a decimal variable named tw.local.amount
with a default value of 251000.0 and you bind a heritage coach control to the
tw.local.amount variable, you can still specify the format in which the value is
displayed even though the value that the control displays during run time is determined by the value
of the variable to which the control is bound. For example, if the US currency (dollars/cents)
format is selected for the heritage coach control, when you run the service the heritage coach
control is populated with the value of the variable, and the value is formatted to $251,000.00.