# Sample business rules

## Including various types of case properties in a rule

- A salary is directly deposited into the account each month
- The account was open for more than three years

If the conditions are not met, the associated rule step returns the specified print statement to
the workflow so that the value can be used by the next step in the workflow.

The rule includes a temporary variable, customerAccountBalanceAsOfToday, that is set to the value
of the current account balance.

The rule includes the following properties from the BankAccountUpdate case type:

| Name                  | Type                                                                                      |
|-----------------------|-------------------------------------------------------------------------------------------|
| AccountBalance        | Float                                                                                     |
| isSalaryAccount       | Boolean                                                                                   |
| RelationshipStartDate | Datetime                                                                                  |
| CustomerCategory      | String that is associated with a choice list that has the values GOLD, SILVER, and NORMAL |

The rule also includes the following custom rule parameters that are defined in the rule designer
and whose values can be passed into the rule when it is called.

| Name                           | Type                                                                                                                                          |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| CreditRatingFromExternalAgency | Integer                                                                                                                                       |
| RelationshipDurationInMonths   | Integer. The value of this parameter is derived by using an expression that uses the RelationshipStartDate case property and the system time. |

```
definitions
  set 'customerAccountBalanceAsOfToday' to the AccountBalance of BankAccountUpdate ;

if all of the following conditions are true :
- customerAccountBalanceAsOfToday is more than 1000000
- CreditRatingFromExternalAgency is more than 75
- any of the following conditions is true :
   - BankAccountUpdate is isSalaryAccount
   - RelationshipDurationInMonths is more than 36

then set the CustomerCategory of BankAccountUpdate to GOLD ;

else print "No changes were made to the customer category by the rule: "+ the name of this rule ;
```

```
var theCase = tw.system.currentProcessInstance.parentCase;
var ruleResponse = theCase.executeRule("CheckForExec", null, null);
if (ruleResponse != null) theCase.addCommentToCase(ruleResponse);
```

<!-- image -->

## Determining process routing

The following
sample business rule is used to determine process routing. Based on
whether the account holder is included in a list of defaulters that
is obtained from an external data source, the rule returns a print
statement to the workflow to indicate whether to accept the overdraft
request. The specified print statement can be used by the next step
in the workflow, such as to display the print output on the Case
Details page to advise  the case worker how to proceed.
Alternatively, you can create a step in IBM®
FileNet® Process Designer to automatically trigger
a response that depends on the value of the print output.

The
rule includes the following property from the BankAccountUpdate case
type:

| Name              | Type   |
|-------------------|--------|
| AccountHolderName | String |

| Name             | Type                   |
|------------------|------------------------|
| ListOfDefaulters | String, multiple value |

```
if the AccountHolderName of BankAccountUpdate is one of ListOfDefaulters
then print "REJECT THE OVERDRAFT REQUEST PENDING SUPERVISOR APPROVAL";
else print "SEND THE REQUEST FOR SENIOR MANAGER REVIEW";
```