<!-- image -->

# Skip-tuples parameter

Use this parameter with the threshold parameter to implement paging
in a client application, for example, to retrieve the first 20 items,
then the next 20 items, and so on.

If this parameter is set to null and the
threshold parameter is not set, all of the qualifying tuples are returned.

## Example of a skip-tuples parameter

- new Integer(5) Specifies that the first five qualifying tuples
are not to be returned.