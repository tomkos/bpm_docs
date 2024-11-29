# Building a Decision service in the desktop Process Designer  (deprecated)

Business rules are an expression of business policy in a form that
is understandable to business users and that can be run by a rule
engine. Business rules formalize a business policy into a series of
"if-then" statements. In Process Designer, business
rules are included in a business process definition (BPD) by adding
a Decision service to the process. Add a Decision service to a Process
Application when the actions that should take place in your process
depend upon one or more conditions. For example, if an employee holds
the position of Director and submits a meal expense for more than
$250, then you can create a rule and set a variable in the rule, such
as approvalRequired, to route the process sequence
flow into a specific approval activity.

- Build your rule hierarchy so that rule conditions are ordered
from most complex to least complex.
- Create a final condition that is a catch-all rule. This rule is
necessary if you cannot guarantee that the variable that you want
to modify in the rule will be set before running the process that
triggers the Decision service.
- Consider encapsulating your rules in a single-function Decision
service, which allows the service to be available to any other part
of the process application that needs the same rule logic.

The following topics describe how to author, implement and manage
business rules in Process Designer.

- Scenario: Creating a Decision service in a Personalized Notification process (deprecated)

 Traditional: 
This scenario shows you how to create, configure and test Business Action Language (BAL) rules in a Decision service. The scenario presents a sample business process that is used by a bank to notify a customer when a payment is made from a specific account.
- Adding a Decision service to a process (deprecated)

 Traditional: 
You can add a Decision service to a business process definition (BPD). Use a Decision service when you want a decision or condition to determine which process implementation is invoked. For example, when a certain condition evaluates to true, IBM Process Designer implements the associated activity or action.
- Implementing an activity using a Decision service (deprecated)

 Traditional: 
You can implement an activity using a Decision service.
- Attaching a Decision service to a decision gateway (deprecated)

 Traditional: 
You can use a decision gateway in your business process definition (BPD) when you need to model a point in the process execution where only one of several paths can be followed, depending on a condition. You can also attach a Decision service to a decision gateway.
- Adding a BAL Rule component to a service (deprecated)

 Traditional: 
The Business Action Language (BAL) Rule component provides a rule editor that allows rule designers to author business rules using natural language technology. Using natural language, instead of JavaScript, to author rules means that no programming expertise is required to create business rules, and the rules are easier for people to read and understand.
- Adding and modifying Decision service variables (deprecated)

 Traditional: 
Each IBM Business Automation Workflow Decision service has a set of input, output, and private variables that are declared for that service. The business terms and phrases that you define as variables are available for you to use when you are writing rules. For example, the variable appear in the Content Assist menu in the rule editor.
- Testing a Decision service (deprecated)

 Traditional: 
When you have finished creating a Decision service and authoring rules in a rule component, such as a BAL Rule component, you can test the Decision service to determine if the rules are being applied as you intended. If an error or exception occurs within a rule, you will see messages about the error during testing, and you can debug the specific rule component or rule that caused the error.
- Scenario: Exporting rules to Rule Execution Server (deprecated)

 Traditional: 
This scenario shows you how to export, migrate, and connect BAL rules to Rule Execution Server. You can migrate the rules that you created in Process Designer to a business rules management system (BRMS) such as IBM Operational Decision Manager, and then continue to use the rules in a business process definition.
- Exporting rules for use in Rule Designer (deprecated)

 Traditional: 
You can export a set of rules to create a project file that you can then import and work on in IBM Operational Decision Manager Rule Designer.
- Adding an IBM ODM Decision Service component to a service (deprecated)

 Traditional: 
When building a Decision service in Process Designer, you can include decision services available on an instance of IBM Operational Decision Manager Rule Execution Server in your implementation.
- Adding a Decision Table component to a service (deprecated)

 Traditional: 
You can add a Decision Table component to a service.
- BAL reference (deprecated)

 Traditional: 
A reference guide to the Business Action Language (BAL), which is used to author rules in IBM Business Automation Workflow, is available in the IBM Operational Decision Manager documentation.
- Decision service limitations (deprecated)

 Traditional: 
Some functions and variables are not supported in a Decision service.