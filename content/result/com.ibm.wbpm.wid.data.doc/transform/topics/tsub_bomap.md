<!-- image -->

# Mapping substitutable elements

## Before you begin

<!-- image -->

As
the above example shows, you can select an element in a substitution
group and map it to an element in another business object. As in all
business object maps, the run order of the transform is significant
here as well. However, for substitution groups there is another consideration.
Let's assume that when this business object map is run, the instance
data that comes into the map is of type StoreName.
This will cause both transformations to run over the same instance
data, and there is potential for the second transform to override
the operation performed by the first transform.

<!-- image -->

Since
the head element is mapped with a Move transformation, regardless
of whether Name or StoreName  is
present on the instance data coming in during runtime of the map,
the Move transform will always run.  Therefore, you only need to define
one type of mapping to handle all substitution group members.

You
can also map substitutable elements in the XML map editor. Note that
the result of executing an XML map of a head element may be different
than the result of executing a business object map of a head element.