<!-- image -->

# Selecting the indexes of input and output array elements

For each input array, you can select the indexes of the elements
that you want the transform to operate on. To specify the indexes,
enter a value in the Input array indices field
of the Cardinality properties page for the transform.

| Selected index elements        | Value in input array indices field   |
|--------------------------------|--------------------------------------|
| All indices                    | * (or leave empty)                   |
| Only index 5                   | 5                                    |
| Indices 1 through 3            | 1:3                                  |
| Indices 1, 3, and 5            | 1,3,5                                |
| Indices 2 and up               | 2*                                   |
| Indices 1, 3, 5 and up         | 1,3,5:*                              |
| Indices 2 through 8, but not 5 | 2:4,6:8                              |
| All indices but 5              | 1:4,6:*                              |

To set the index of the output array element that the transform
will operate on, enter a value in the Output array indices field
of the Cardinality properties page. This is slightly different from
input index entries since only a single index is allowed.  Leave the
field empty to indicate that the whole output array will be utilized.