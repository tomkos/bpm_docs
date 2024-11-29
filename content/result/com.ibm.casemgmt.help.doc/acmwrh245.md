# Filtering and sorting process work items in in-baskets

## Procedure

To filter and sort the work items, complete the following steps:

1. Enable Automatically sync shared business objects for each case
activity process. See the Variables that are passed by value with reference
section in How variables are passed in Process Designer (by value or by reference).
2 Verify whether aliases are generated for the case properties and activity properties thatare shown in in-baskets in solution design: Aliases are generated to populate the searchable value for the case properties and activityproperties that are shown in in-baskets. You can verify whether aliases are generated for each caseproperty and activity property that is shown as column or filter in the solution design.

Aliases are generated to populate the searchable value for the case properties and activity
properties that are shown in in-baskets. You can verify whether aliases are generated for each case
property and activity property that is shown as column or filter in the solution design.

    1. Open the REST API
/rest/bpm/wle/v1/searches/tasks/meta/businessDataFields?includeCaseAlias=true. For
example,https://ip:port/<contextroot>/rest/bpm/wle/v1/searches/tasks/meta/businessDataFields?includeCaseAlias=true
    2. Verify whether the caseResult node is generated for each case property and activity
property, which is shown in in-baskets in solution design. Sample caseResult
node:<caseResult xsi:type="savedsrchdefn:SearchDefinitionMetaDataWithId">
	<name><Alias Name></name>
	<type><Data type></type>
	<symbolicName><Case/Activity Property Unique Identifier></symbolicName>
	<caseContext><Case/Activity></caseContext>
	<full\_text\_searchable><true></full\_text\_searchable>
	<id><guid></id>
</caseResult>For example, 
<caseResult xsi:type="savedsrchdefn:SearchDefinitionMetaDataWithId">
	<name>CF\_TAP1\_CaseName1</name>
	<type>String</type>
	<symbolicName>TAP1\_CaseName1</symbolicName>
	<caseContext>Case</caseContext>
	<full\_text\_searchable>true</full\_text\_searchable>
	<id>{F9E43D9A-41FA-401D-9639-D5276D45B0DD}</id>
</caseResult>
<caseResult xsi:type="savedsrchdefn:SearchDefinitionMetaDataWithId">
	<name>CT\_TAP1\_ActName1</name>
	<type>String</type>
	<symbolicName>TAP1\_ActName1</symbolicName>
	<caseContext>Activity</caseContext>
	<full\_text\_searchable>true</full\_text\_searchable>
	<id>{115EE80E-D4D9-4F25-91BF-3A2CC74F3268}</id>
</caseResult>
    3. Optional: If you do not find the equivalent caseResult node in the
REST API response, open the solution in design, go to In-baskets > edit, and
save. Complete the step 2b again.
3 Optional: Display more than 500 process work items in eachin-baskets: Restriction: Use the supported operators for filtering workflow process work items: Table 1. Stringsoperator Operator Description is equal for single value in for multiple values of "is equal" is like supported but not recommended since it has performance impact is not equal supported is not like not supported is greater than supported is greater than or equal not supported but works same as "is greater than" is less than is less than or equal not supported but works same as "is less than" Table 2. Booleanoperator Operator Description is equal for single value in for multiple values of "is equal" is not equal supported Table 3. Integeroperator Operator Description is equal for single value in for multiple values of "is equal" is not equal supported is greater than supported is greater than or equal not supported but works same as "is greater than" is less than supported is less than or equal not supported but works same as "is less than" Table 4. Float operator Operator Description is equal for single value in for multiple values of "is equal" is not equal supported is greater than supported is greater than or equal not supported but works same as "is greater than" is less than supported is less than or equal not supported but works same as "is less than" Table 5. Date operator Operator Description is equal for single value in for multiple values of "is equal" is not equal supported is greater than supported is greater than or equal not supported but works same as "is greater than" is less than supported is less than or equal not supported but works same as "is less than"

1. To display process work items in in-basket, a search is applied against the workflow
server to get the result set.
2. The default number of work items that are returned from a process work item search is
500. To know how to further tune this value, see Tuning Process Portal searches  topic.

- The indexes or searchable business properties values are applied for the new workflow process
instances. For existing workflow process work items of the created process instances, the values are
empty.
- For Float data type, filtering and sorting work for two decimal points.

Use the supported operators for filtering workflow process work items:

| Operator                           | Description                                                   |
|------------------------------------|---------------------------------------------------------------|
| is equal                           | for single value                                              |
| in                                 | for multiple values of "is equal"                             |
| is like                            | supported but not recommended since it has performance impact |
| is not equal                       | supported                                                     |
| is not like                        | not supported                                                 |
| is greater than                    | supported                                                     |
| is greater than or equal           | not supported but works same as "is greater than"             |
| is less than is less than or equal | not supported but works same as "is less than"                |

| Operator     | Description                       |
|--------------|-----------------------------------|
| is equal     | for single value                  |
| in           | for multiple values of "is equal" |
| is not equal | supported                         |

| Operator                 | Description                                       |
|--------------------------|---------------------------------------------------|
| is equal                 | for single value                                  |
| in                       | for multiple values of "is equal"                 |
| is not equal             | supported                                         |
| is greater than          | supported                                         |
| is greater than or equal | not supported but works same as "is greater than" |
| is less than             | supported                                         |
| is less than or equal    | not supported but works same as "is less than"    |

| Operator                 | Description                                       |
|--------------------------|---------------------------------------------------|
| is equal                 | for single value                                  |
| in                       | for multiple values of "is equal"                 |
| is not equal             | supported                                         |
| is greater than          | supported                                         |
| is greater than or equal | not supported but works same as "is greater than" |
| is less than             | supported                                         |
| is less than or equal    | not supported but works same as "is less than"    |

| Operator                 | Description                                       |
|--------------------------|---------------------------------------------------|
| is equal                 | for single value                                  |
| in                       | for multiple values of "is equal"                 |
| is not equal             | supported                                         |
| is greater than          | supported                                         |
| is greater than or equal | not supported but works same as "is greater than" |
| is less than             | supported                                         |
| is less than or equal    | not supported but works same as "is less than"    |