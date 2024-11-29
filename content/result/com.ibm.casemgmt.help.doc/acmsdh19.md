# Adding and modifying case types

## About this task

Case types identify the activities, content, processes, and views that are required to manage the
case. For example, a solution for a human resources department might include a case type for new
hires, a case type for retirement, and a case type for resource actions. Each case type can have one
or more activities that must be completed to process and close the case, such as reviewing a claim
application or distributing a check for an approved claim. Activities include steps that are
displayed as work items in case worker in-baskets. You can create business rules to implement
business policies and practices, such as determine process routing or update case properties if
particular conditions are met. You design views to control what information case workers see when
they work on a case.

## Procedure

To add or modify a case type from the solution home page:

1. Click the Case Types tab and add
a case type, or select an existing case type to modify.
2. Enter a name and description for the case type.
If you are adding a case type, the Case type unique identifier value is
updated as you enter the name to create a unique identifier for the case type.
3. Optional: 
Set the Case Identifier Prefix setting to a value that you would like to
see as the prefix of the Case Identifier in runtime. Case Identifier acts as the default title of
the case instances that you view in Case Client.
4. Optional: 
Select the starting document class that triggers a new case. 
For example, when a new claim form document is added to the system, a new case starts to
process the claim.

To copy matching document properties to case type properties, select Map document
class properties. For example, if a new claim form document includes the policy number,
that policy number can be copied into the policy number property for the new case.
5. Optional: 
If you want users to be able to create quick tasks for a case, select Enable case
workers to create quick tasks.
6. Optional: 
If you want users to be able to create custom activities for a case, select Enable
case workers to create custom activities.
7. Optional: 
If you want users to be able to add documents or attachments from external repositories,
     select Allow documents and attachments from repositories other than the case
      management object stores.
If you plan to include content from an external repository, configure a connection to the
     repository in IBM Content
Navigator before you deploy the
     solution.
8. Optional: 
Select the Case Client pages
or client-side human service views that you want to display when a user adds a case or views a case.
You can also select the Case Client page that you want to display when a user splits a case, but there is no client-side human
service view for a split case.
When you create a solution, you can choose to include default pages or client-side human
service views.
9. Optional: 
If you want a different Case Details page or client-side human service view to display in
Case Client for a specific role,
click Add Role to add the role, and then select the page or client-side human
service view that you want to associate with the role.
When you create a solution, the only available options are Default Case Details
page or a client-side human service view.
10. Add properties, views, case folders, business rules, and activities to the case type. For more
information, see Adding and reusing properties.
11. Click Save.
Case Builder does not save
your edits automatically as you work. When you click OK to close a dialog box
or an editor view, your selections are stored in memory. Click Save to store
your changes to the solution definition file. If you do not save your changes, you can save or
discard the changes before you close the solution.
12. On the Overview tab, click the three vertically aligned dots and select
Validate.
The case type design is validated and a message is displayed in the status
bar.
13. Click the Commit icon.
Committing your changes makes the solution assets available for further editing or
deployment.

- Case types

Case types define the activities, document classes to support the activities, activity steps, and roles that must complete the steps to solve a business problem.