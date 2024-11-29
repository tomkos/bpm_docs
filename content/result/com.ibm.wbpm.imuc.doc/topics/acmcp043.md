# Adding business rules from IBM Operational Decision
Manager to a solution

## Before you begin

Before
you add a business rule to a solution, review the rule and verify
that the rule was deployed in IBM Operational Decision
Manager.

## About this task

A business rule captures and implements business policies
and practices, such as enforcing a business policy or making a decision
that is based on specific data. For example, a business rule can update
a particular case property to indicate that a fraud investigation
task is required if an automobile insurance claim is filed by the
driver of a sports car.

You can use rules software, such as IBM Operational Decision
Manager, to separate the business
rules from the process, which makes it easier for a business analyst
to independently manage the process and the rules for the process,
rather than modifying a workflow definition.

## Procedure

To add business rules from IBM Operational Decision
Manager to a solution:

1. Open the solution in Case Builder and add case properties,
case types, tasks, steps, and roles as necessary.
Include
properties that can be parameters for the Operational Decision Manager rule in this solution.
For example, an automobile insurance claims solution might have case
properties that include Vehicle Year (integer), Vehicle Make (string),
Policy Number (string), Claimant Age (integer), and Potential Fraud
(Boolean).
2. Deploy and test the solution.
3. In the Operational Decision Manager Rule
Execution Server console, select the ruleset that contains the rules
that are related to your solution to verify that the rules are deployed
in Operational Decision Manager.
4 Obtain the URL for the Web Service Definition Language(WSDL) file.
    1. In the Rule Execution Server console, click Explorer and
click the RuleApp that contains your ruleset.
    2. In the RuleApp view, click the
ruleset and click Retrieve HTDS Description File.
    3. Select the Latest ruleset version and Latest
RuleApp version options.
    4. Click View to open the file in
a web browser.
    5. Copy the URL from the address bar of the browser and
paste it into a text document so that you can refer to the URL in
the next step.
For example, the URL might be http://localhost:9082/DecisionService/ws/AutomobileFraudCheckRuleApp/1.0/AutomobileFraudCheck/1.0?WSDL
5 Define the partner link to the web service. Apartner link consists of a name and the WSDL URL for Invoke functions.

1. Open the solution in IBM
FileNet® Process Designer.
On the Manage
Solutions page in Case Builder,
click Open IBM
FileNet Process Designer from
the More Actions option for your solution.
2. Select a case type and a task.
3. Click Workflow Properties > Web Services > Partner
Links.
4. Specify a name for the partner link.
5. Select Invoke and paste the WSDL
URL into the WSDL URL field.
6. Click the Browse icon (...),
which populates the available port types and select the port type
from the menu.
6. Add the following parameters to the workflow definition
on the Workflow Properties > Data Fields tab in IBM
FileNet Process Designer.

ODMDecisionID
String
ODMOutput
String
ODMRulesCount
Integer

The parameters are specific to Operational Decision Manager and therefore are not
included in your solution.
7. Complete this step for business rules that you created
in Case Builder and exported
to Operational Decision Manager, and any other
rules that use a case object to represent the set of case properties
in a single object:

Create an XML data field to store
the execution results that are returned from the IBM Operational Decision
Manager web services. In IBM
FileNet Process Designer, click Workflow Properties > Web Services > XML Data Fields and add a field
with the name ODMOutputXML.
8 Create a system step to implement the rules:

1. Add a system step to your solution workflow in IBM
FileNet Process Designer.
You might
have created a stub step for this purpose in Case Builder.
2. Connect the final workflow step to the new system step.
3. Specify a name for the step.
4. Select the Invoke function from
the Available Functions list and move it to
the Selected Functions list.
5. In the Selected Functions list,
double-click Invoke.
6. Click Messages. Then, select
the partner link and the operation.
The incoming and outgoing
parameters are automatically populated with the Operational Decision Manager rules parameters
7 Define the outgoing and incoming values.
    - For typical business rules that you created in Operational Decision Manager :
        1. In the Outgoing Parameters list, select
the matching case property for each parameter from the Expression menu.
        2. In the Incoming Parameters list, select
the matching data field for each parameter from the Field
Name menu. You created the data fields in a previous step.
You can also use a field assignment to assign values.
- For business rules that you created in Case Builder and exported to Operational Decision Manager , and any other rules thatuse a case object to represent the set of case properties in a singleobject:
    1. For the Message Type option, select XML.
    2. In the Outgoing Message field, replace
the place holder values in the <caseObject> XML element with expressions
that represent the case properties and data fields that are mapped
to custom rule parameters. Use the format F\_CaseFolder.attribute\_name.
For example, change the value "<Creator>" + "Creator" +"</Creator>" to "<Creator>"
+ F\_CaseFolder.Creator +"</Creator>". For the CmAcmCaseState
property, set the value to <CmAcmCaseState>"+ "Working"
+"</CmAcmCaseState>.Tip: All parameter values
in the <caseObject> XML element must be strings. To avoid validation
errors, use Expression builder to change time and date values to timetostring
functions and numbertostring functions.
    3. In the Incoming XML Data Field field, specify ODMOutputXML.
    4. Select the Assign function from the Available
Functions list and move it to the Selected
Functions list.
    5. In the Selected Functions list, double-click Assign to
view the assignment parameters that correspond to case properties
and data fields that are mapped to custom rule parameters.
    6. For the ODMOutputXML parameter, specify the following expression: substitute(ODMOutputXML,
"xsi:type=""ns0:caseType""", "")
    7. For each case property or data field whose value is set by the
business rule, specify an XPath expression that returns the corresponding
value from the ODMOutputXML data field. For example, specify the following
XPath expression to the value of a case property: xmlstringexpr(ODMOutputXML,
"/", "/*[local-name()=""CSR1\_CT1\_RuleName""]/*[local-name()=""caseObject""]/*[local-name()=""caseObject""]/*[local-name()=""F\_CaseFolder.CSR1\_StringProperty""]")
9. Validate, transfer, and check the workflow.
10. In Case Builder,
click Manage Solutions and deploy the solution
to the development environment for testing.

## Related tasks

- Exporting business rules to IBM Operational Decision Manager