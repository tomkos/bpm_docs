# Adding a case solution

## About this task

Use the wizard to add a new case solution either from scratch, without using a template, or from
a template that is based on a snapshot of an existing case solution. Choose to use a base template when you want to quickly
create a new solutions that is based on the same design.

- Without using a template, you create an empty solution to which you then add and configure
assets in Case Builder.
- When you use a template, you start the design of your new solution from a point-in-time snapshot of a base case solution.

Multiple templates can be created for the same case solution, from snapshots that are captured at different points in the
solution lifecycle.

The template provider might choose to prevent you from changing or deleting assets, such as
properties, document classes, or case types. Check with the template provider for specific
restrictions.

- Adding a case solution
- Adding a legacy case solution

For more information on how to add and configure assets to complete and deploy the solution, see
Adding and deploying a case management solution.

- Adding and managing properties

Properties such as names or dates are defined at the solution level. These properties can be reused in any case type, document class, task, or step within that solution.
- Adding and selecting roles

A role defines and groups caseworkers by the type of work that they do. You can associate roles with steps in the tasks of a solution.
- Adding and modifying document classes

Document classes organize and classify the documents that belong to a case. For example, you can create a document class for case correspondence and another document class for photographs and images. You assign document classes at the solution level. You can assign a document class to start a new case or as a precondition for a task.
- Adding and modifying business objects

A case can contain multiple instances of a solution entity that is best represented by a collection of properties. In this scenario, you can define a business object that is a structured data type that contains a collection of properties. You define a case property in your solution that uses this business object as the data type.
- Adding and modifying case types

A solution can have one or more case types. You can add case types to a new solution by using the wizard or from a solution home page. You can modify existing case types from the solution home page.
- Creating and configuring stages for a case type

You define stages for a case type to represent the lifecycle of a case. The first stage starts automatically when the case is started. When one stage completes, the next stage automatically begins. For example, for a loan case type, you might have an initial review stage that starts when a client submits a loan application. When the initial review verifies that all the necessary information is submitted, the case moves on to the credit check stage.
- Defining case type views

The Views section for a case type enables you to customize the user interfaces that a case worker uses to find, identify, and work with cases and the information they contain.
- Business rules

Business rules determine the actions to take if particular conditions are met. After you create business rules for your case type, you can use the business rules in an activity to determine process routing or to update case properties.
- Adding activities

A case activity is a automated set of actions that are performed on a case instance to help drive it to a successful outcome. These activities are orchestrated by the case or case worker in the Case Client and can perform various functions depending on its type, including launching a process, adding a to-do list to a case at the appropriate time, and acting as a container for other activities to control when they are available.
- Multiple user editing of solutions

Multiple users can edit a single solution at the same time. Opening an asset for editing locks the asset so that only the user who is editing can change it. In addition, editing certain assets locks all associated assets.
- Designing the case management client application

The client application consists of a set of pages that are displayed in Case Client for your solution. Each page provides the layout that is required to perform a specific action or task. You can start with a set of default pages that you can customize to meet the requirements of specific roles, case types, or work items in your solution. Alternatively, you can create custom pages to use in place of the default pages.
- Testing your solution

Before you deploy your solution into production, you can test it to verify that the solution components are working correctly by deploying it into a development environment.

## Adding a case solution

In Workflow Center,
you can add a new case solution either without using a template or from a base solution template.
Each user who might add a solution must use their own user ID. If you edit the same solution in more
than one browser session, changes might be lost.

### Before you begin

### Procedure

To add a case solution:

1. In Workflow Center,
in the navigation tree, click Case solutions, then click
Create.
2. In the Create a case solution modal, enter a name and an optional
description for the new solution. If you want to use a base template, select the template, too, and
then click Create. Note that the base template option is not
offered if no templates exist.

### Results

## Adding a legacy case solution

### About this task

When you create a solution from a template, you can select an option to use existing unique
identifiers. The default setting is the option that is set in the template. The new solution is
created in the same object store as the template, and you can select the project area to which to
assign the solution.

### Procedure

To add a solution in Case Builder:

1 On the Manage Solutions page, select the method that you want to use toadd a solution: Without a template Copy an existing solution From a template
    1. Select a template from the menu and click Add Solution, then select
No template to create a solution without using a template.
    1. Select an existing solution and click Copy. Tip: If you do
not find an existing solution that you wanted to copy on the Manage Solutions
page, the solution might be assigned to a different project area. Check with your system
administrator.
    2. Enter a name and solution prefix. The solution prefix is a 2-5 character prefix that is
prepended to all case types, document classes, properties, and task unique identifier names that are
created for the solution. The solution prefix must be unique across all solutions. However, if you
create a solution from a template, reused properties that are part of the template retain the prefix
that is assigned by the template supplier. Restriction: You cannot modify the solution
name or prefix after you create the solution.
    3. Add a solution description and icon. If you copied a solution, you can
change the icon after you create the solution. You can modify the solution description by clicking
the Edit solution description icon in the solution summary on the solution
home page. Solution icons are a predefined set of icons.
    1. In the navigation tree, select an object store and click Solution
Templates.
    2. On the Solution Templates page in the right pane, select a template.
    3. Click Actions > Create
Solution and complete the wizard steps.
2. Add roles, case types, and properties, then add document classes and set the in-basket views to
complete the case solution.

### Results

### What to do next

If the solution is associated with a process application, complete the steps in the topic Copying case solutions that are associated with process applications.