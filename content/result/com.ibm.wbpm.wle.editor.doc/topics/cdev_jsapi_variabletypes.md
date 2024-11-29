# Variable types

System toolkits are provided in Workflow Center
so that each process application and toolkit that you create has access to common system data. System toolkits
provide the following categories of variables:

| Base types   | Description                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String       | Allows alpha-numeric characters to be entered into the variable                                                                                                                                                                                                                      |
| Integer      | Accepts digits without a decimal place in the range from -2147483648 to 2147483647, such as 45 or 20                                                                                                                                                                                 |
| Decimal      | Accepts digits with decimal places with IEEE 754 double precision, such as 45.3 or 20.13                                                                                                                                                                                             |
| Date         | Allows date and time formats to be entered into the variable                                                                                                                                                                                                                         |
| Time         | Allows date formats to be entered into the variable as times. The user enters a time; before the variable is entered into the symbol table, it is converted into a date.                                                                                                             |
| Selection    | Allows you to provide a list of possible entries to a user, from which the user can select only one. A selection is a list of different values; each value is a string. At run time, a selection variable appears on a coach form as a list or as radio buttons.                     |
| Boolean      | Accepts either true or false as values. The Boolean value appears at run time on a coach form as a check box.                                                                                                                                                                        |
| Structure    | To use a structure type, you must create a custom structure type and define its properties. A structure regroups business data that is related to the same subject. For example, a Customer structure might contain elements such as lastName, firstName, homeNumber, streetAddress. |

## Custom variable types

Custom variable types
are defined by using business objects. If the predefined business
objects that are provided in the system toolkits do not represent
your needs, you can create your own business objects.

- When you assign a value to a variable in a process or service of such a type, such as when a
script assigns a value to a tw.local variable or an output mapping where a
service result is mapped into a tw.local variable, the value is validated.
- When you have a heritage human service (deprecated) with a heritage coach
(deprecated), the input fields that are bound to a service variable are validated when you submit
the heritage coach. To enable validation on the coach view, you must define the validation rules
again in the coach view configuration where you bound your variable.

By specifying
the precision and scale, you can restrict the decimal number and the
decimal places of a number.

You specify how the validation
settings must be interpreted in the business object configuration
of the server configuration.

| Properties                                | Type                        | Default value   | Description                                                                                                                                                                                                                                                             |
|-------------------------------------------|-----------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| precision-validation-on-server-enabled    | Boolean                     | false           | Used to enable the validation of the precision setting when a variable is set. If it is not enabled, it is checked only in heritage coaches.                                                                                                                            |
| precision-validation-strip-trailing-zeros | Boolean                     | false           | Used to remove trailing zeros from behind the decimal point before the precision is validated                                                                                                                                                                           |
| precision-validation-type                 | enum (equals, lessOrEquals) | equals          | If this property is set to equal, the precision of the variable value must equal what is specified in the variable type. If the property is set to lessOrEquals, the precision of the variable value must equal or be less than what is specified in the variable type. |
| scale-validation-strip-trailing-zeros     | Boolean                     | false           | Used to remove trailing zeros from behind the decimal point before the scale is validated                                                                                                                                                                               |
| scale-validation-type                     | enum (equals, lessOrEquals) | equals          | If this property is set to equals, the scale of the variable value must equal what is specified in the variable type. If the property is set to lessOrEquals, the scale of the value must equal or be less than what is specified in the variable type.                 |

- 123.45

- 1234.56 (wrong precision, 6 instead of 5)
- 12.34 (wrong precision, 4 instead of 5)
- 12.345 (wrong scale, 3 instead of 2)
- 1234.1 (wrong scale, 1 instead of 2)

The following JavaScript expression also causes a validation
error because JavaScript removes trailing zeros at run time before
it assigns the value:

tw.local.variable = 123.40

The
following JavaScript expression does not cause a validation error
because the string is validated correctly and then is automatically
converted into a number to set the variable value:

tw.local.variable = "123.40"

| Setting                                   | Type         |
|-------------------------------------------|--------------|
| precision-validation-on-server-enabled    | true         |
| precision-validation-strip-trailing-zeros | true         |
| precision-validation-type                 | lessOrEquals |
| scale-validation-strip-trailing-zeros     | true         |
| scale-validation-type                     | lessOrEquals |

- 123.45
- 12.34
- 123.4
- 123

- 1234.56 (wrong precision, 6 instead of a maximum of 5)
- 12.345 (wrong scale, 3 instead of a maximum of 2)

## Numeric calculations in scripts

You can use JavaScript to program within a process or service step. Double precision is used to
store numeric values for variables.

When you perform
calculations in scripts, be careful of limits that can come to this
precision. For example, when you add 1000.06 + 0.01, the mathematically
correct result is 1000.07. However, if you add the numbers in JavaScript,
the result is 1000.0699999999999.

If you require mathematically
correct calculations, perform these calculations outside of the JavaScript
code. For example, you can use the BigDecimal and BigInteger classes
to do calculations with full precision in a Java program. If you must
store the result with full precision in a process or service variable,
you can format the number as a string and use the String data type
for your variable.