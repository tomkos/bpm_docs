<!-- image -->

# Business rules manager examples

The project interchange contains a number of projects.

- BRMgmtExamples - Module project with business rules artifacts
that are used in the various examples.
- BRMgmt - Java™ project
with the examples located in the com.ibm.websphere.sample.brules.mgmt
package.
- BRMgmtDriverWeb - Web project with interface for executing
the samples.

The examples are also provided as an EAR file (BRMgmtExamples.ear)
that can be issued once after installed in Workflow Server. A
web interface is provided with the examples. The web interface is
purposely simple as the examples focus on using the classes to retrieve
artifacts, make modifications, and publish changes. It is not meant
to be a high-functioning web interface. The classes can however, be
easily used to build robust web interfaces or used in other Java applications focused on modifying
the business rules.

The example application can be installed on WebSphere® Process Server v6.1 and the index
page can be accessed at:

http://<hostname>:<port>/BRMgmtDriverWeb/

For example, http://localhost:9080/BRMgmtDriverWeb/

As the examples are issued, changes will be made to the rule artifacts.
If all examples are issued, the application will need to be reinstalled
to see the same results for all examples again.

The examples are explained in detail with complete code samples
as well as the result as displayed in a web browser.

A number of additional classes were created in order to perform
common operations and assist with displaying the information within
the example web application. See the appendix for more information
on the Formatter and RuleArtifactUtility classes.

To fully understand these examples, a study of the different artifacts
within IBM Integration
Designer will
greatly help.

- Example 1: Retrieve and print all business rule groups

This example will retrieve all business rule groups and print out the attributes, the properties, and the operations for each business rule group.
- Example 2: Retrieve and print business rule groups, rule sets and decision tables

Besides the function in example 1, this example will print out the selection table for each operation and then the default business rule destination (either rule set or decision table) and the other business rules scheduled for the operation. It prints out both rule sets and decision tables.
- Example 3: Retrieve business rule groups by multiple properties with AND

This example is also similar to example 1, but will only retrieve those business rule groups which have a property named Department and a value of "accounting" and a property named RuleType and a value of "regulatory".
- Example 4: Retrieve business rule groups by multiple properties with OR

This example is similar to example 3; however it will only retrieve those business rule groups which have a property named Department and a value of "accounting" or a property named RuleType and a value of "monetary".
- Example 5: Retrieve business rule groups with a complex query

This example is a combination of examples 3 and 4 and it is meant to show how more complex queries can be created. In this example a search is performed with a query that combines 2 query conditions. The first query condition is to retrieve those business rule groups which have a property named Department and a value of "General" or a property named MissingProperty and a value of "somevalue". This query condition is then combined with an AND to a condition where the property is named RuleType and a value of "messages".
- Example 6: Update a business rule group property and publish

In this example, a property in a business rule group is updated and then the business rule group is published.
- Example 7: Update properties in multiple business rule groups and publish

In this example, properties in multiple business rule groups are updated before publish.
- Example 8: Change the default business rule for a business rule group

In this example, the default business rule is changed with another business rule that is part of the available targets list for a specific operation.
- Example 9: Schedule another rule for an operation in a business rule group

In this example, a business rule is scheduled to be active for 1 hour from the time of publish for a specific operation.
- Example 10: Modify a parameter value in a template in a rule set

In this example a rule instance defined with a template is modified by changing a parameter value and then publish.
- Example 11: Add a new rule from a template to a rule set

In this example, a new rule is added from a template to a rule set. Before the new rule instance is created, parameters for the new rule instance are created.
- Example 12: Modify a template in a decision table by changing a parameter value and then publish

In this example, a condition and action, both defined with templates, are modified in a decision table by changing the parameter values before it is published.
- Example 13: Add a condition value and actions to a decision table

In this example, a condition value and action are added to a decision table. Condition values can be added to a decision table through the use of a template.
- Example 14: Handle errors in a rule set

This example focuses on how to catch problems in a rule set and find out what problem has occurred such that the appropriate message can be displayed or action can be taken to correct the situation.
- Example 15: Handle errors in a business rule group

This example is similar to example 14 as it shows how to handle problems that occur when a business rule group is published. It shows how the problem can be determined and the correct message can be printed or action performed.
- Additional Query Examples

The following examples are not included with the application containing examples 1-15, however they provide more examples on creating queries to retrieve business rule groups.