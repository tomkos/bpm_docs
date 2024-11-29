# Business rules

You can include user-defined case properties and case system properties
in your rules. If you want the rule to refer to data that is external
to the case, such as the credit rating of a loan applicant, you can
define custom rule parameters and then include them in the rule.

To use the business rule in your workflow, call the rule
from a process activity by using the executeRule JavaScript API in the
currentProcessInstance.parentCase class. For an example, see Sample business rules. For more information, see JavaScript API in processes, cases, and service flows.

## Text-based business rules

A text-based business
rule consists of the following elements:

- Case Identifier
- Creator
- Date Created
- Date Last Modified
- Last Modifier
- Case State

For example, for a loan case type, you can define
a rule to set the value of the Interest\_Rate case property to 3.5%
if the credit rating of the applicant is higher than 700. In the following
examples, Credit\_Rating is a custom rule parameter. (The following
examples are written in the English locale.)

```
if Credit\_Rating is more than 700 
then set the Interest\_Rate of LoanCaseType to 3.5;
```

## Table-based business rules

A table-based
rule, also known as a decision table, consists of condition and action
columns. Each condition column specifies the circumstance for which
particular actions are to be carried out. Each action column specifies
the actions to take if the conditions are true. Each row in the table
represents a separate rule. If the conditions of a row are met, the
actions in that row are taken.

For example, you want to create
a group of rules that sets the value of the Interest\_Rate case property
for different ranges of credit rating values. You first define a condition
column that represents the value of the Credit\_Rating custom rule
parameter for a loan applicant.

```
Credit\_Rating is <a number>
```

Next,
you define an action column that represents the interest rate to offer:

```
set the Interest\_Rate of LoanCaseType to <a number>
```

Then,
in each row, you specify a particular credit rating and the corresponding
interest rate:

|   Credit rating |   Interest rate |
|-----------------|-----------------|
|             500 |             5.2 |
|             600 |             4.3 |
|             700 |             3.5 |

As you specify values in each row, checks are run by default to ensure that the values that you
enter for a given condition do not overlap or are not identical. For example, consider a column for
the age of the customer:

- Row 1: age is between 17 and 30
- Row 2: age is between 29 and 40

In this example, customers that are 29 years old satisfy the condition of both rows. The rule
editor reports this as an overlap warning.

By default, the rule editor also checks that the cells in a condition column consider all
possible cases, which helps you ensure that there are no gaps in your table. For example, consider a
column for the age of the customer:

- Row 1: age is between 17 and 30
- Row 2: age is between 32 and 40

In this example, customers that are 31 years old are not taken into account, which is reported as
a gap warning.

## Defining preconditions in table-based rules

For table-based rules, you can use preconditions to check incoming data to determine
				whether the table-based rule can process the information. You can also use
				preconditions to define variables that can be used in the rule. The scope of these
				variables is limited to the specific rule in which the variables are defined.

## Checking for null values

To
avoid receiving possible errors during run time, use defensive programming
techniques to ensure that values are populated for all case properties
whose values are retrieved in a business rule.

Use the definitions section
in a rule to declare variables for all case properties whose values
are retrieved. If a case property is not initialized, its variable
is not initialized and the rule is not run.

```
definitions
 set balanceAmount to the Opening\_Balance of Account\_Request;

if balanceAmount is more than 10000 
then set the Interest\_Rate of Account\_Request to 0.55;
```

## Defining temporary variables

You can define
temporary variable in the definitions section to
calculate intermediary values that can be used in a rule. For example,
you define a business rule to set the value of the ProfitAfterTax
case property. Because no case property corresponds to the profits
before tax, you define an intermediary ProfitBeforeTax variable to
calculate the profits before tax according to the values of the Assets
and Liabilities case properties. To determine the correct tax rate,
you add a condition in the rule to use a higher tax rate if the profits
are more than 1 million dollars.

```
definitions  
	set ProfitBeforeTax to 
	(the Assets of TaxCasetype - the Liabilities of TaxCasetype);
	set Tax to .07;
	set SurchargeForHigherIncome to .005;

if ProfitBeforeTax is more than 1000000 
then set the ProfitAfterTax of TaxCaseType to 
	(ProfitBeforeTax - ProfitBeforeTax *(Tax+SurchargeForHigherIncome)) ;
else set the ProfitAfterTax of TaxCaseType to 
	(ProfitBeforeTax -ProfitBeforeTax*Tax);
```

## Using Boolean properties in business rules

The
following examples show how you include Boolean properties in a rule.

- If the value of a Boolean property is true, set the value of another
Boolean property to false:if CaseTypeName is BooleanProperty1
then make it false that CaseTypeName is BooleanProperty2
- If the value of a Boolean property is false, set the value of
another Boolean property to true: if it is not true thatCaseTypeName is BooleanProperty1
then make it true that CaseTypeName is BooleanProperty2

- Setting completion menu options

You can set options for the way the rule editor presents terms and phrases in the completion menu, and for the way rules are parsed.