<!-- image -->

# Threshold parameter

Because query result sets in production scenarios can contain thousands
or even millions of items, specify a value for the threshold parameter.
If you set the threshold parameter accordingly, the database query
is faster and less data needs to transfer from the server to the client.
The threshold parameter can be useful, for example, in a graphical
user interface where only a small number of items should be displayed
at one time.

If this parameter is set to null and the
skip-tuples parameter is not set, all of the qualifying objects are
returned.

## Example of a threshold parameter

- new Integer(50) Specifies that 50 qualifying tuples are to
be returned.