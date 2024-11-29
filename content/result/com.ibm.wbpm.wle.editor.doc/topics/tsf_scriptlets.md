# Using scriptlets in script tasks

## About this task

## Procedure

1. Specify the binding with a variable of the service flow,
to which the computed result will be assigned. The variable
is usually of type String. If it is not of type String, it should
be a basic type (such as Integer, Decimal, Boolean, or XMLElement,
from the System Data toolkit); then the string that is the result
of the text with embedded JavaScript is converted to the required
type before the assignment.
2. Specify the text that contains embedded JavaScript, as
described in Syntax for text with embedded JavaScript. This is the
text with JavaScript computations that produces the resulting string.

## Results