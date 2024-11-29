# Adding a BAL Rule component to a service (deprecated)

## About this task

The following steps describe how to add a BAL Rule component
to a sample Decision service. The purpose of the sample service is
to determine whether approval is required for certain employee expenses.
The sample service is a single-function Rule that can be called from
any other service.

- ConditionalActivity
- IndexedMap
- Map
- NameValuePair
- Record
- SLAViolationRecord
- SQLDatabaseType
- SQLParameter
- SQLResult
- SQLResultSetColumn
- SQLResultSetRow
- SQLStatement
- TWHolidaySchedule
- TWTimePeriod
- TWTimeSchedule
- TWWorkSchedule
- TaskListData
- TaskListItem
- TaskListProperties
- TaskListFilterProperties
- TaskListSortBySelectionType
- XMLDocument
- XMLElement
- XMLNodeList

## Procedure

1. Open the process application in the Designer view.
2. Create a Decision service.
3. In the diagram of the new Decision service, click BAL
Rule in the component palette and drag the BAL Rule component
icon from the palette to the service diagram.
4. In the Properties tab, enter a name
for the new BAL Rule component, such as ExpenseApproval.
5. Click the Variables tab.
6 Click Add Private to add a privatevariable to the Decision service. For this sample Decisionservice, add the private variable, request .
    1. Replace Untitled1 in the Name field
with request .
    2. Click Select next to Variable
Type and select the type from the list.
7. If you use the Activity Wizard to create a Decision service,
you can choose existing variables to add as input and output. You
should use the Activity Wizard when you start with an existing activity
and want to quickly create a service to implement the activity. To
access the wizard, right-click an activity icon in a process diagram
and select Activity Wizard from the list of
options.
8. Click Add Private.
9. Replace Untitled1 in the Name field
with approvalRequired .
10. Click Select next to Variable Type
and select the Boolean type from the list. The
Boolean variable type is included in the Business Automation Workflow System
Data toolkit. The System Data toolkit is included in each process
application by default.
11. Click the Decisions tab to open
the rules editor.

## What to do next

- Creating rules using the rule editor (deprecated)

 Traditional: 
You can create rules using the Business Action Language (BAL) rule editor. The rule editor uses natural language technology to express business decisions in a form that is readable by humans but can also be run by a rule service runtime such as the IBM® Operational Decision Manager Rule Execution Server.
- Business rule parts and structure (deprecated)

 Traditional: 
Business rules, such as action rules or decision tables, express business policy statements using a predefined business vocabulary that can be interpreted by a computer. Rules authored in the Business Action Language (BAL) are also easily readable by humans.
- Defining variables in the rule editor (deprecated)

 Traditional: 
Variables are defined in the definitions part of a business rule.
- Copying and pasting content in the rule editor (deprecated)

 Traditional: 
You can copy content from a rule to the system clipboard, or paste content written outside the rule editor into the editor window.
- Setting the rule language (deprecated)

 Traditional: 
You can use the locale preference setting provided in IBM Process Designer to set the language used in a BAL Rule component.
- Troubleshooting BAL rule editor errors (deprecated)

 Traditional: 
The Business Action Language (BAL) rule editor highlights errors with red underline in the editing window.