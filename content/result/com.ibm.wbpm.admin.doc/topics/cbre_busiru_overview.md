<!-- image -->

# Business process rules manager

Business rules are designed and developed in IBM Integration
Designer using if/then rule sets and decision tables
to implement their operations. Business rules can also be created in IBM
WebSphere® Business Modeler; however Modeler only supports the creation
of business rule tasks, which become rule sets when exported out of Modeler. The rule sets and
decision tables are set into templates. The templates control which aspects of a business rule you
can modify and by exactly how much. They define the structure of if/then rules, condition cases, and
actions for decision tables.

The templates provide the mechanism for business rule runtime authoring in the business process
rules manager. Using the template, you can modify business rule values, create a new rule within a
rule set or a new condition or action within a decision table, and publish changes to business rule
definitions at run time.

Business rules are organized into business rule groups. Business rule groups are used to provide
the interface to business rules and to invoke business rules. Rule sets and decision tables are
never invoked directly.

- How the business process rules manager works

The business process rules manager is the main IBM Workflow Server tool that a business analyst uses for runtime rule authoring.
- Accessing the business process rules manager

You access the business process rules manager using a web browser.
- Business Rule Groups page and the business process rules manager page layout

When the business process rules manager opens, the Business Rule Groups page opens, so you can browse all of the business rule groups and their defined operations.
- Adding, deleting, and modifying business rule group properties

You can use custom properties on business rule groups for searches in order to retrieve subsets of business rule groups that you want to view and modify. You add new custom properties, delete or modify existing properties through the editing pages of business rule groups. The number of custom properties on a business rule group is unlimited.
- Searching business rule groups

You can perform a search query on a business rule group to locate or narrow a specified set of business rule groups that you want to work with. You create a search query based on the name, target name space, custom properties, or any combination of these.
- Working with scheduled rule logic entries

A scheduled rule logic entry identifies information for a rule, such as its effective dates and the if/then rule set or decision table associated with the rule.
- Rule sets

A rule set is a group of if/then statements or rules where the if is the condition and the then is the action of the rule. Rule sets are best suited for those business rules that have very few condition clauses.
- Decision tables

A decision table is a scheduled rule logic entry, in table format, that consists of conditions, represented in the row and column headings, and actions, represented as the intersection points of the conditional cases in the table. Decision tables are best suited for business rules that have multiple conditions. Adding another condition is done by simply adding another row or column.
- Deleting scheduled rule logic entries

You can delete existing scheduled rule logic entries from the scheduled rule logic table. When a scheduled rule logic entry is deleted, the associated rule set or decision table definition remains with the rule group and is listed in the Available Rule Logic section of the page. The scheduled rule logic entry can be added back either as the default rule logic or with a specific date and time.
- Publishing and reverting business rules

When you save any part of a business rule group, the changes are saved locally. In order to store the changes to the data source that resides on the application server, you need to publish the changes. Alternatively, you can cancel the changes that have been saved locally to a business rule by reverting the rule to its original state.
- Troubleshooting the business process rules manager

Some of the problems you might encounter using the business process rules manager are login errors, login conflicts, and access conflicts.

## Related concepts

- Considerations for modules containing business rules and selectors
- Overview of business rules
- Overview of selector components

## Related information

- Business Rules