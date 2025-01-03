# Incrementing float values in number spinner property fields

## Symptoms

- No default value is specified for the property in Case Builder. When a Case Client user increments a number
spinner property field up or down with no starting value, then the
minimum or maximum value for that float value will be displayed.
- The value specified for either the large or small increment is
a decimal with a specified number of decimal places. Due to certain
javascript storage factors, incrementing by decimals can result in
numbers that are slightly more or less than the expected value.  For
example, if the value for a property is meant to contain a US Dollar
amount, then the number of significant decimal places is 2, and the
number spinner might reasonably be set to increment by 0.01.
 However, a user incrementing 1.05 up might get a
result of 1.060000000997, instead of 1.06 as
expected.
- The value specified for either the large or small increment is
not accurate due to rounding errors.  For example, if the number spinner
is set to increment by 1/3, and the number of decimal
places is 2, the value for the increment will be inaccurate since 1/3 cannot
be expressed by a decimal with two digits (either 0.33 or 0.34 might
be used, neither of which is precisely accurate). Consequently, incrementing
the number spinner will begin to cause number errors with each increment.
 In the example, incrementing up by 1/3 from a starting
value of 0.00, using increments of 0.33,
will first yield results of 0.33 and then 0.66 after
two increments. However, the second increment value of 0.66 is
not accurate, as the correct rounded value for 2/3 is 0.67.
While this might be temporarily corrected by using a more precise
increment (for example, 0.333 instead of 0.33,
this will only delay the first inaccurate number until more increments
have been applied.

## Resolving the problem

- You should always define a default value for the property.  This
will prevent Case Client from
using the maximum or minimum value for a float number as the result
of a first increment.
- When a property is to be incremented by a specified decimal value,
you should specify the number of decimal places when designing the
property in Case Builder.
 You should also specify that the number should be automatically rounded.
When dealing with increments with repeating decimals, choose a meaningful
number of decimal places and specify the increment as accurately as
possible to avoid rounding errors as best as possible for your solutions
needs.

1. Open the solution in Case Builder and
click on the property with the number spinner that you want to modify.
2. Click on the Case Types tab, and click
on the desired case type.
3. Click Views in the left navigation.
4. Click the Properties Layout tab, and click
the desired view.
5. In the Properties area, click on the property that contains the
number spinner field that you want to modify.
6. Click on the number spinner field. The settings for the number
spinner can be found in the Control Settings area.