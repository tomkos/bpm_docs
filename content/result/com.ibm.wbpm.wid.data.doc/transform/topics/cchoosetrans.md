<!-- image -->

# Choosing a transform for an XML map

The first step in choosing a transform is to connect the input
and output element in the XML map editor. The editor does some of
the work for you by automatically assigning a transform depending
on the input and output types. You can then change the transform by
choosing from a list of available transforms. If you don't see a particular
transform type on the list, that transform is not valid for your input
and output elements.

- If you have a single array as input, with the same array type
as output, and want to move all elements to the output, use Move.
- If you have a single array as input, and want to iterate over
the each element in the array, for example to remove some elements,
use the For each transform and set the cardinality
options.
- If you have multiple input elements, you can use Join or Append. If you use Join, the number of output elements depend on the number of entries of
the input arrays that satisfy the Join expression.  If you use Append, the number of output elements is the total of
the input elements.