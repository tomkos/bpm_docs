# Designing your case management solution and application

One approach to designing a solution is to first identify the types of documents that people in
your organization need to complete for some activity. For example, to resolve a credit card dispute
claim, you might need a dispute form and customer to complete the form and a service representative
to review that form. Next, you might need to initiate a fraud investigation if circumstances warrant
such an activity. In that case, you might need a fraud investigator to review the claim.

- Dispute form
- Fraud investigation form

- Customer
- Customer service representative
- Fraud investigator

The following diagram shows the steps you might take when you try
to identify the artifacts that you will need for a solution.

You can use Case Builder to help you think through the
various document classes, roles, case types, activities, and so on that you need for a specific
solution.

<!-- image -->

A solution is a set of related business problems (or case types).
For example, if you are designing a solution for the bank industry
for a credit card dispute claim, you might first decide what case
types are needed. An example of a credit card dispute case type is
a processing a claim. For this case type, a customer claim for a credit
card dispute is reported and processed.

For every business problem that you are trying to solve (case type), you have physical assets or
documents (document classes) that you work with to complete the case, people who work those
documents (roles), and activities that need to be completed to close the case. Properties help to
define the details of the case types, document classes, roles, and activities.

A process describes how case workers must complete an activity, but an activity describes what
needs to be done and why. For every activity, steps can be completed by the system or by the case
worker. Activities can be run in parallel, they can be chained together, or they can even be
skipped.

You can create a workflow process for an activity in Case Builder. You can also define an
activity process map or a process definition by using Step Designer in Case Builder or by using IBM®
FileNet® Process Designer, which is integrated into
Case Builder at both the solution
and activity level. You can modify workflow processes that are created for an activity in the
Case Builder Step Designer in the
IBM
FileNet Process Designer. External process
activities are created as reused activities in the Case Builder and should be implemented by
using IBM Business Automation
Workflow
Process Designer or
IBM
FileNet Process Designer

Activities can be required or optional, and you can set the activities to start automatically or
manually by a case worker. A case is completed when all required and currently running activities
are completed. In addition, you can group activities so that they are mutually exclusive and only
one activity in the group can be completed or all-inclusive and all activities in that group must be
completed. You can also group activities inside of a container activity.

You can also associate business rules with your solution. Organizations might have rules for
business operations, such as for pricing calculations, eligibility checks, validations,
underwriting, and fraud detection. In your solution, you can create business rules that determine
process routing or update case properties. In conjunction with other case management  capabilities,
business rules can be used in the following ways:

- Intelligently assign priority to cases or assign case workers to activities
- Automatically create and assign activities
- Trigger fully automated actions that are based on external events, completion of other case
activities, or expiration of activity deadlines
- Apply rules to the key facts and information, and guide the responses
that are based on that information
- Simplify certain activities by automating the decision logic
- Increase consistency by using decision rules across similar cases

- Decide what the case worker needs to do to complete his or her
job and what fields are needed in the Case Client.
- Evaluate the use case flow and extract the solution assets from
it.

As you become familiar with designing solutions, you can identify the roles, document classes,
and properties that can be used in more than one case type.

When you design and create a solution, you must decide what the solution locale
is. The solution locale refers to the locale of display names, such as case properties, case types,
activities, and other solution artifacts that you create with Case Builder. When you deploy the solution to a target environment
for the first time, you must deploy the solution under the same locale to ensure that the display
names are preserved.

- Preparing the design environment

To prepare your design environment, you can import metadata from the production environment in which you plan to deploy the solution. You can also import a solution template so that you can quickly design a new solution that is based on the template.
- Identifying your solution artifacts

When you design your solution, identify the document classes that are needed for the cases. Then, decide which people must be involved and what they will work on.
- Adding and deploying a case management solution

You can use Workflow Center or Case Builder to add a solution that case workers will access from the Case Client. A solution is a set of web pages, content, and process definitions that provide a framework so that you can manage cases.
- Sample business rules

Business rules can include user-defined case properties and case system properties. Business rules can also include custom rule parameters if you want the rule to refer to data that is external to the case.
- Configuring auditing

You can configure auditing for use with the analytics tools that supports Case Analyzer. You can also configure auditing to track the history of cases by using the timeline visualizer widget. You can configure auditing for a deployed solution in a development environment, or in a production environment.
- Validating preconditions

Using commands, you can run the precondition checker utility to validate preconditions after changing property preconditions for an existing activity. The precondition checker looks for activities that were created before the precondition changed and evaluates the updated activity. If the new precondition is met, the activity status changes to working status.
- Resetting the test environment

You can use the Reset Test Environment feature to remove the deployed solutions and other data from the development environment project area.
- Managing case solutions

In various ways, you can manage your case solutions.
- Creating and distributing solution templates

In addition to creating case solutions for deployment in the same domain that hosts your Case Builder instance, you can create solution templates that can be distributed to a separate domain or at another site. After you design and create a case solution, you can create a template from that solution to use as a base for other solutions.
- Unlocking solution assets

If a solution asset is locked by a user and the user cannot unlock it, for example the user is on vacation or left the company, you can unlock the asset by using the  Case administration client.
- Translating case management applications

You can translate the user interface elements that make up your case management application. For example, your users can then open the case management application and view it in Chinese or French by setting their browser locale to Chinese or French, or by setting the application language to Chinese or French in the Change Language and Locale Settings window.
- Adding workflow processes to existing solutions

If your in-basket doesn't include the necessary actions to work with workflow process tasks, you must add the actions manually to your in-basket menu, toolbar, or both by editing the In-basket widget in Case Builder.