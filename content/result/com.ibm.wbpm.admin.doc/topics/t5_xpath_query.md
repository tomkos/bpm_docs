<!-- image -->

# XPath query returns an unexpected value from an array

## Reason

A common cause for this problem is assuming
that the first element in the array has an index value of zero. In XPath queries
in arrays, the first element has the index value one.

## Resolution

Check that your use of index values into
arrays start with element one.