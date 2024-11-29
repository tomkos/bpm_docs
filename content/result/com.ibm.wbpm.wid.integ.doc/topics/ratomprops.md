<!-- image -->

# Atom feed format properties

You can set properties for the Atom feed
data handler on the Data Handler Properties page.

The following
properties can be configured on the Atom feed data handler.

| Property name        | Explanation                                                                                                                 | Possible values   | Default value   |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------|
| Encoding             | This is the encoding that will be used in converting bytes to string and string to bytes wherever applicable.               | Enum              | All encodings   |
| Mime Type            | This is the mime type of the incoming content. In the case of Atom, this corresponds to the field in content called type.   | None              | None            |
| Data handler binding | This is the configuration that corresponds to a data handler that will be used to transform content in the given mime type. | None              | None            |

## Handling nulls and absence of tags

If a
certain tag is not present in the Atom feed, then we consider this
as unset in the business object. Conversely, if a certain property
in the business object is unset, then the corresponding element does
not appear in the Atom feed.