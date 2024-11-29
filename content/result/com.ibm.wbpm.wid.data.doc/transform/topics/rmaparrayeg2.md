<!-- image -->

# Example: Extract a selected element of the input array to a
single output

Select the third rewardPoints element
of type int from the input array goldStar\_Client
rewardPoints and copy it to a single output element frequent\_flyer\_points of
the same type.

1. Map the elements using a Move  transform.
The following image shows how this looks in the map editor:
2 Select element 3 by setting the cardinality of the Inputarray indices for the Move transformto 3. There is no option to set the cardinality of the output element,because it is a single element. To set the cardinality, follow thesesteps: Tip: The first index element has a cardinality of1.
    1. Click the Move transform.
    2. Right click the white space in the map editor, and select Show
In > Properties View.
    3. Click the Cardinality tab.
    4. Enter 3 in the Input array indices field.

<!-- image -->

3. Right-click the map canvas, and select Test Map to
see the output of the map based on the input specified, as shown in
the following image.  Note that goldStar\_client[0] is the first index
element with a cardinality of 1, and the third index element is goldStar\_client[2]
with a cardinality of 3: