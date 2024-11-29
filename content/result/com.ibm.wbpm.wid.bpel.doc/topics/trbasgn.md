<!-- image -->

# Troubleshooting errors related to assign activities

## Assigning fixed values to arrays

If you
plan to assign a fixed value to an element inside an array then you
will receive an error when you run the process in a runtime environment.
This occurs because the XPath that gets generated is unable to address
all of the elements in the array. You can work around this by modifying
the assign activity's Assign To field to identify
the elements in the array. For example, you would change an existing
entry from /attribute2 to /attribute2[1] to identify it as the first element of the array.

## Assigning values to a BO attribute

```
org.apache.commons.jxpath.JXPathException: Exception trying to create xpath Result/@resultStatusFlag; Cannot create an attribute for path /root/Result/@resultStatusFlag, operation is not allowed for this type of node
```

1. Assign the value to a non-attribute value within the BO, and then
to the attribute.
2. Use a Java™ Snippet activity
to create the BO.