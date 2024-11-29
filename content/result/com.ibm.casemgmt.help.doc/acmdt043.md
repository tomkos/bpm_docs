# Adding rule operations to an activity by using IBM
FileNet Process Designer

## Before you begin

In Case Builder,
define the business rule that you want to run.

In IBM
FileNet Process Designer, define a data field
of type string to store the return value that is the output of the
rule operation.

Also define a data field for each custom rule parameter that is associated with the rule that you
want to run. If your rule includes a custom rule parameter in a condition, you must define a data
field whose value is populated by a previous step in the workflow. If your rule includes an action
that sets the value of a custom rule parameter, you must define a data field whose value is set by a
later step in the workflow.

## About this task

To add rule operations, you open the activity in IBM
FileNet Process Designer and add a component step to the workflow with which
you associate the rule operation. The return value of the rule operation is a string that contains a
concatenation of all the print statements that are outputs of the rule.

All case properties that are updated by the rule are updated
in Content Platform Engine.

## Procedure

To add rule operations to a workflow step:

1. In a stand-alone IBM
FileNet Process Designer, open the solution for
editing the FileNet P8 activity workflow, which you want to add the rule operation.
2. In IBM
FileNet Process Designer, drag the
Component icon to the location in the activity flow where you want the
operation to be run.
3. On the Component tab, click the Add icon.
4. From the Component list, select ICM\_RuleOperations.
5. Select the executeRule operation.
6 In the Operation Parameters area, enter an expression for each operationparameter by clicking in the Expression field and selecting BuildExpression . Note: Commit the changes in Case Builder to save the changes inIBMFileNet Process Designer .
    1. For the caseID parameter, select F\_CaseFolder from
the Business Object Fields list.
    2. For the ruleName parameter, specify the unique identifier of the rule that
you want to run.
For example, specify "myRule".
    3. For the customRuleParameterNames parameter, enter a string expression that
lists the unique identifiers of all custom rule parameters that are associated with the rule. 
For example, specify the expression
{"Param1","Param2","Param3"}.
    4. For the customRuleParameterValues parameter, enter a string expression
that specifies the data fields to map to the custom rule parameters that are associated with the
rule.
Ensure that you specify a value for each custom rule parameter and that you list the values in
the same order as the custom rule parameter names are listed in the
CustomRuleParameterNames parameter.
For example, specify the expression
{dataField1,dataField2,dataField3}.

For data types other than string, you must create an expression that gives the value of the data
field in a textual form. For example, to convert the Created Date property of the case to a string,
use the following pattern: timetostring(F\_CaseFolder.DateCreated,"yyyy-mm-dd
hh:tt:ss")
For multiple-value custom rule parameters, specify the value in the format
arraytoString(data\_field,"{","}",","). For example, if your rule
uses the InterestRate and CreditRatings custom rule parameters, and you defined data fields with the
same names, specify the following value for the CustomRuleParameterValues
parameter: 
{InterestRate,arraytoString(CreditRatings,"{","}",",")}.
    5. For the return\_value parameter, specify the name of the data field to
store the return value that is the output of the rule operation.
For example, specify "dataField4".