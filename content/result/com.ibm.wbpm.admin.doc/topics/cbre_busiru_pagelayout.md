<!-- image -->

# Business Rule Groups page and the business process rules manager page layout

The Business Rule Groups page is the first level of navigation. Its page layout includes many
elements generic to the other business rules manager pages.

## Toolbar

## Navigation pane

## Content area

## Title section

BusinessRuleGroup01 >
Table1\_operation1

Example:
CalculateDiscountBRG > CalculateDiscount

Ruleset112 - Ruleset

Examples:
calculateDiscount-Rule Schedule, CalculateDiscountRS - Rule
Set

| Button Name   | Function                                                                                                                                                                                                                           |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add Property  | Adds properties to a business rule group in the Business Rule Group page or to create a search query in the Search for Business Rule Groups page.                                                                                  |
| Back          | Returns to the previous page.                                                                                                                                                                                                      |
| Cancel        | Discards any changes to the resource and returns to the previous page.                                                                                                                                                             |
| Copy          | Copies either a decision table or rule set in order to create a new decision table or rule set. You must copy an existing decision table or rule set and then modify its values in order to make a new decision table or rule set. |
| Edit          | Enables editing of the business rule group, rule schedule, rule set, or decision table.                                                                                                                                            |
| Publish       | Publishes the business rule group or rule schedule to the repository.                                                                                                                                                              |
| Revert        | Cancels all changes to the rule that have been saved locally and reverts the rule to the original copy that resides in the server memory. Rules cannot be reverted after publishing.                                               |
| Save          | Validates and saves the changes to the local copy and goes back to the previous page. Note that the running state of the server has not been changed. See Publish for how to change the server's state.                            |
| Search        | Initiates the search query on the Search for Business Rule Groups page and returns the business rule groups that match the query as search results on the same Search for Business Rule Groups page.                               |
| Sort          | Sorts the properties on the business rule groups by the property names in alphabetic ascending order.                                                                                                                              |

"calculateDiscount" has been temporarily
saved.

You may publish the changes from the Publish and
Revert page.

## General Information section

If the display
name is set, it is used instead of the name value everywhere name values are used, including the
navigation pane and when artifacts are displayed in detail. If the display name of a business rule
artifact is not set, its name value is used instead. Selecting the Synchronize with the
name check box synchronizes the display name with the corresponding name value of the
target business rule group, rule set, or decision table. The new name takes effect on all pages of
the business rules manager when you save the changes made in the edit page.

## Page-specific information section

The content of the page-specific information section depends on whether you are viewing a
Business Rule Group page, Rule Schedule page,
Rule Set page, or Decision Table page. For specific
information for each of these pages, see the individual topics.

- Publish and Revert page

The Publish and Revert page is for publishing locally saved changes for business rule groups and rule schedules to the repository. It is also for reverting business rule groups and rule schedules back to the original copy that was in the server memory before the business rule resource was saved locally.
- Business Rule Group page

The Business Rule Group page lists all the business rules resources associated with the business rule group.
- Rule Schedule page

The Rule Schedule page provides an interface for modifying the values of a business rule group in the scheduled rule logic entries. The information is displayed in table format.
- Search for Business Rule Groups page

The Search for Business Rule Groups page is for creating a search query to locate or narrow a specified set of business rules groups that you want to work with. You open the Search for Business Rule Groups page by clicking Search in the toolbar of the business process rules manager.