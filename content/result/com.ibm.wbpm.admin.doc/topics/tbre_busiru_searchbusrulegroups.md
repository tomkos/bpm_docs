<!-- image -->

# Searching business rule groups

## Before you begin

## About this task

## Procedure

1. In the Name field enter the name of the business rule group to search
for. 
You can leave this value empty; however, it will not be included in the search context. The
value you enter is used as both a name and a display name. Consequently, the search will look for
business rule groups with either the names or the display names that match the entered name value.
If you want to specifically search by either name or display name, but not both, you need to
indicate such a search through property names.Example: If you enter IBMSystemName for the
name of a property and VIPGroup for the value of the property, the business process rules manager
will search for business rule groups with the names, but not display names, matching VIPGroup.
2. In the Target Namespace field enter the URL of the business rule group. 
You can leave this value empty; however, it will not be included in the search context.
3 For each Search Data field select one of the following four queryoperators. Option Description Query Operator Description is equal to Indicates that the value of a business rule group name, target name space, or property mustmatch the specified string exactly. is like Indicates that the query should look for business rule groups where the value of a businessrule group name, target name space, or property is like the specified string. The string can containwildcard characters. Use the percent character ('%') to specify a wildcard for any number ofcharacters and use the underscore character ('\_') to specify a single character wildcard. Thesewildcard characters must follow SQL syntax.Examples: is not equal to Indicates that the value of the business rule group name, target name space, or propertymust not match the specified string. is not like Indicates that the query should look for business rule groups where the value of a businessrule group name, target name space, or property is not like the specified string. The string cancontain wildcard characters as defined in the "like" operator.

| Option          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Query Operator  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| is equal to     | Indicates that the value of a business rule group name, target name space, or property must match the specified string exactly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| is like         | Indicates that the query should look for business rule groups where the value of a business rule group name, target name space, or property is like the specified string. The string can contain wildcard characters. Use the percent character ('%') to specify a wildcard for any number of characters and use the underscore character ('\_') to specify a single character wildcard. These wildcard characters must follow SQL syntax.Examples:  If you enter "is like" "Discount" for the business rule group name and "http://calculateDiscounts" as the target name space, the search will return all the business rule groups containing that string and with that URL. If you enter "is like" "%Discount%" for the business rule group name, the search will return all the business rule groups with names such as AirlineTicketDiscount and MovieTicketDiscountRules. |
| is not equal to | Indicates that the value of the business rule group name, target name space, or property must not match the specified string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| is not like     | Indicates that the query should look for business rule groups where the value of a business rule group name, target name space, or property is not like the specified string. The string can contain wildcard characters as defined in the "like" operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

4 Optional: Click Add Property to add as many properties as neededfor the search context. Tip: You can combine the properties in the Logical Operator fieldusing "And" , "Or" , or "Not" tocreate a search query containing multiple properties.Example: To search for all thebusiness rule groups in target namespace "http://calculateDiscounts" and withthe DiscountedItem property containing string "men T-Shirts" and with theShip Handling property set to value "Free" , you would use the logicalproperty "And" . Note: Adding, deleting, or modifying the properties on the Search for Business Rule Groups page onlyapplies within the search context. It does not affect the properties of any rule object inside thebusiness process rules manager.

1. Specify the Name.
It must be unique inside the Properties table of the search context and must not be
empty.
2. Specify the Query Operator.
3. Specify the Value.
The value can be empty and is taken into the search context.Example: If the value of
property PayMethod is left empty and its query operator is set to is not equal to,
the search will find all the business rule groups whose PayMethod property has the value set to a
non-empty string.
4. Click the up and down arrows in the Action field to order the
properties.

Example: To search for all the
business rule groups in target namespace "http://calculateDiscounts" and with
the DiscountedItem property containing string "men T-Shirts" and with the
Ship Handling property set to value "Free", you would use the logical
property "And".

5. Click Search.

## Results

| Status                | Description                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Same as Local         | Indicates that a copy of the result business rule group already exists in the business process rules manager and that its content and the content of the result business rule group are exactly similar. Consequently, no further action is taken after the search.                                                                                                          |
| Modified from Runtime | Indicates that a copy of the result business rule group already exists in the business process rules manager. However, another user session modified the master copy, and so the contents of the local and result business rule groups are different. The business process rules manager will automatically update the local copy to get new modifications from the runtime. |
| Modified in Local     | Indicates that a copy of the result business rule group already exists in the business process rules manager. However, it has been modified by the current user. The business process rules manager will use the local copy for any further actions by the user.                                                                                                             |
| New to Local          | Indicates that a copy of the result business rule group does not exist in the business process rules manager. In this case, the business process rules manager will create a local copy of the result business rule group and will also display it in the navigation pane, too.                                                                                              |

## Example

- Name: BRDCR002BRG2.brg
- Target namespace: http://BRDCR002BRG2/com/ibm/br/rulegroup
- Properties:
    - organization, 7GAA
    - department, accounting
    - ID, 0000047
    - ID\_cert45, ABC
    - region, NorthRegion

- Name: BRDCR002BRG3.brg
- Target namespace: http://BRDCR002BRG3/com/ibm/br/rulegroup
- Properties:
    - organization, 7FAB
    - department, finance
    - ID, 0000053
    - ID\_app45, DEF
    - region, NorthCentralRegion

- Name: BRDCR002BRG4.brg
- Target namespace: http://BRDCR002BRG4/com/ibm/br/rulegroup
- Properties:
    - organization, 7HAA
    - department, shipping
    - ID, 0000023
    - ID\_app45, GHI
    - region, SouthRegion

- Name: BRDCR002BRG5.brg
- Target namespace: http://BRDCR002BRG5/com/ibm/br/rulegroup
- Properties:
    - organization, 8JAA
    - department, claims
    - ID, 00000567
    - region, SouthCentralRegion
    - manager, Joe Bean

| Logical Operator   | Name       | Query Operator   | Value      |
|--------------------|------------|------------------|------------|
|                    | department | is equal to      | accounting |

| Logical Operator   | Name   | Query Operator   | Value   |
|--------------------|--------|------------------|---------|
|                    | region | is like          | %Region |
| AND                | ID     | is like          | 00000%  |

| Logical Operator   | Name   | Query Operator   |   Value |
|--------------------|--------|------------------|---------|
|                    | ID     | is like          | 00000\_3 |

| Logical Operator   | Name   | Query Operator   | Value        |
|--------------------|--------|------------------|--------------|
|                    | region | is like          | \_\_uth%Region |

| Logical Operator   | Name         | Query Operator   | Value   |
|--------------------|--------------|------------------|---------|
|                    | organization | is not like      | 7\_\_A    |

| Logical Operator   | Name         | Query Operator   | Value   |
|--------------------|--------------|------------------|---------|
|                    | organization | is not like      | 7%      |

## What to do next