<!-- image -->

# XML Transform: Append

The append transform takes multiple inputs of either simple
type or complex type that can contain nested transforms. The output
must be an array of either a simple type or a complex type.

The
order of inputs into the transform is recognized, and is set in the
Order property page.

The Cardinality property page on the
transform specifies which indexes the transform should process. The
first index element is 1.

During execution,
iteration is performed over each input sequentially (for example,
first over all elements in the first input array, then over all elements
in the second input array, and so on).  Inputs of single elements
are allowed; each element adds an extra count to the iteration process.
 The output array size is the total of the input elements, minus any
elements that are filtered out from the cardinality property page.

See Example: Append the result of two or more input arrays into an output array.