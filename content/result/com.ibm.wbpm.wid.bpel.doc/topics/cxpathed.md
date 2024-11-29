<!-- image -->

# Working with XPath in the BPEL process editor

In places where you can use the XPath standard, you can compose
the XPath expression in one of two ways. You can use the XPath Expression
Builder to visually create the message, or you can build it yourself
manually.

For information on how to use the XPath Expression Builder, see XPath Expression Builder.

For more information on XPath 1.0, see http://www.w3.org/TR/xpath.

## Example: Using XPath to iterate an array

The following example shows how XPath can be used to iterate through
the members of an array within a Business Object.

```
count(bpws:getVariableData('Input1', 'values'))
bpws:getVariableData('index') <= bpws:getVariableData('size') 
concat('values[', bpws:getVariableData('index'), ']')
bpws:getVariableData('Input1', bpws:getVariableData('query')) 
variable is incremented:  bpws:getVariableData('index') + 1
```

This code snippet begins by counting the array elements that need
to be copied. Then, it assigns that value to an integer called size. The BO is contained in the Input1 variable, which contains an array of items in the values
array element. Then, it uses a while loop to iterate through
the array and builds a string with the value of values[n], where n is the value of the index variable. The string is stored in a variable called query. Then, the code retrieves the actual value of the array element,
and increments the index variable.

## Related tasks

- Using assign