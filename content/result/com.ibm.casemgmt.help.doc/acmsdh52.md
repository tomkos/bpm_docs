# Mapping custom parameters in rule steps to external data sources

## Before you begin

## Procedure

To map custom rule parameters in a rule step to external
data sources:

1. Open IBM®
FileNet® Process Designer.
On the Case Builder Activities page,
click the Open IBM
FileNet Process Designer icon
that is displayed next to the activity. Alternatively, you can open IBM
FileNet Process Designer from the More menu
of the solution on the Manage Solutions page.
2. Select the rule step that uses custom parameters.
3. From the Operation Parameters list,
open the expression for the CustomRuleParameterValues parameter in
Expression Builder and specify the data fields to map to the custom
rule parameters that are used by the rule step.
Ensure
that you specify the values in the same order as the custom rule parameter
names are listed in the CustomRuleParameterNames parameter. 

Tip: If after you create a rule step you edit the associated
rule and add a custom parameter, the custom parameter is not automatically
included in the CustomRuleParameterNames parameter value. Manually
add the parameter to the list of values.
For multiple-value
custom rule parameters, specify the value in the format arraytoString(data\_field,"{","}",",").
For example, if your rule step uses the InterestRate and
CreditRatings custom rule parameters, and you defined data fields
with the same names, specify the following value for the CustomRuleParameterValues
parameter: {"InterestRate",arraytoString(CreditRatings,"{","}",",")}.
4. Validate the workflow.