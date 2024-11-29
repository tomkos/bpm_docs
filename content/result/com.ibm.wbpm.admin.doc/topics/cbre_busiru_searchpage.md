<!-- image -->

# Search for Business Rule Groups page

On the Search for Business Rule Groups page, you can search by the target namespace, business
rule group name, custom properties or any combination of these; you can add one or many custom
properties, sort custom properties by their names in alphabetic ascending order, move properties up
or down inside the property table, or delete custom properties.

The content area of the Search for Business Rule Groups page includes a
Messages field and page-specific information sections with the following
elements.

## Search Data section

Example: If you enter IBMSystemName for the name of a property and VIPGroup
for the value of the property, the business process rules manager will search for business rule
groups with the names, but not display names, matching VIPGroup.

## Properties section

| Query Operator   | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| is equal to      | Indicates that the value of a business rule group name, target name space, or property must match the specified string exactly.                                                                                                                                                                                                                                                                                                           |
| is like          | Indicates that the query should look for business rule groups where the value of a business rule group name, target name space, or property is like the specified string. The string can contain wildcard characters. Use the percent character ('%') to specify a wildcard for any number of characters and use the underscore character ('\_') to specify a single character wildcard. These wildcard characters must follow SQL syntax. |
| is not equal to  | Indicates that the value of the business rule group name, target name space, or property must not match the specified string.                                                                                                                                                                                                                                                                                                             |
| is not like      | Indicates that the query should look for business rule groups where the value of a business rule group name, target name space, or property is not like the specified string. The string can contain wildcard characters as defined in the like operator.                                                                                                                                                                                 |

Example: If the value of property PayMethod is left empty and its query
operator is set to is not equal to, the Search will find all the business rule
groups whose PayMethod property has the value set to a non-empty string.

## Search Results section

| Status                | Description                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Same as Local         | Indicates that a copy of the result business rule group already exists in the business process rules manager and that its content and the content of the result business rule group are exactly the same. Thus, no further action is taken after the search.                                                                                                                 |
| Modified from Runtime | Indicates that a copy of the result business rule group already exists in the business process rules manager. However, another user session modified the master copy, and so the contents of the local and result business rule groups are different. The business process rules manager will automatically update the local copy to get new modifications from the runtime. |
| Modified in Local     | Indicates that a copy of the result business rule group already exists in the business process rules manager. However, it has been modified by the current user. The business process rules manager will use the local copy for any further actions by the user.                                                                                                             |
| New to Local          | Indicates that a copy of the result business rule group does not exist in the business process rules manager. In this case, the business process rules manager will create a local copy of the result business rule group and will also display it in the navigation pane.                                                                                                   |

## Related concepts

- Business Rule Group page
- Rule Schedule page

## Related information

- Publish and Revert page