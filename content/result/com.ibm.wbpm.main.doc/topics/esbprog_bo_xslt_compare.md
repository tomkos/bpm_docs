<!-- image -->

# Comparison between the Mapping and BO Mapper mediation primitives

| Use Mapping when                                                              | Use BO Maps when                                                                                              |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| You have an existing stylesheet or want to use custom XSLT in the map.        | You have an existing BO Map or submap.                                                                        |
| You want to use XPath expressions inside the map                              | You want to use the relationship service (particularly dynamic relationships).                                |
| You want to use Java™ snippets that use the DOM API to access or update data. | You want to use Java snippets that use the BO API (SDO API) to access or update data.                         |
| You want to use built-in XPath or EXSLT functions to access or modify data.   | You want to order the completion sequence for the transforms.                                                 |
| You want to combine contents from more than one array (repeating element).    | BO Maps can be faster when used with WebSphere® Adapters, because the BO Maps work directly with the SDO API. |

When performance is important and the advanced functions offered by XSLT are not
required, the BOMapper mediation primitive should always be used.