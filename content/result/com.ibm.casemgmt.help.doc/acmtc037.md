# Cannot open a view that contains a datetime property with an invalid mask or pattern

For example, hh - mm - ss A is an invalid time pattern for a single value
datetime property. The correct syntax is hh - mm - ss a (where the
a is lowercase).

After you set a mask or pattern for a datetime property, you can test it by assigning a default
date for the property in Properties View Designer. If the mask or pattern does
not seem to be applied correctly for the default value, then it is likely that the mask or pattern
is not valid in Properties View Designer. For example, if you specify
A instead of a, then AM or PM does not display as part of the
default value. You can also deploy the solution and verify that the datetime properties are
displayed correctly in Case Client.