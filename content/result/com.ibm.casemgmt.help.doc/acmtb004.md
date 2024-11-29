# Troubleshooting Case Builder

```
http://localhost:9080/CaseBuilder?debug=true
```

- Changing the screen display resolution for Case Client and Case Builder

The default screen size for Case Client and Case Builder can be too large for small computer monitors with low resolution (for example, 768x1080).
- Solution deployment fails due to a queue table limit

Deploying a solution from Case Builder to the development target object store fails due to a database limitation.
- Solution deployment fails if a value is not found for a required property

Deploying a solution from Case Builder to the development target object store fails if no default value is found for a property that is required in the case type.
- Deploying case solution fails with NullPointerException

Case solution snapshot deployment using REST API fails because a user that is assigned to case membership no longer exists in LDAP. You need to delete the case membership permissions of the deleted user from the assignment table of Content Platform Engine using ACCE.
- Responding to validation errors in the Step Designer

If you receive a validation error message when you validate a task in the Case Builder Step Designer, you must confirm that roles and properties that are referenced in the Step Designer are valid for the solution and confirm that your routes meet the validation guidelines. You might also see errors when you open a Task in the Step Designer.
- Reviewing log entries in Case Builder

Case Builder displays error messages and status messages in the status pane at the bottom of the window when the error or status update occurs. You also can view the entire contents of the log file in the status pane, or you can view only the errors from the log.
- Cannot edit locked solution assets

A solution asset is locked when another user opens the asset for editing and does not commit the solution properly, or a session times out, which can prevent other users from editing the asset.
- Case type validation errors

If you receive an error message when you validate a case type in the Case Builder, you must ensure that you saved the solution first.
- Cannot reset the test environment because target object server does not exist

Resetting the test environment fails because the target object server does not exist.
- Deploy dataset not found when the test environment is reset

You cannot reset the test environment because the FileNet® Deployment Manager deploy dataset is not found.
- Document opens in another window even when the Viewer widget is present

A default setting in Case Builder can cause unexpected   behavior when you view documents or attachments on the Case Details   page.
- Toolbar buttons on Rules and Activities pages are not displayed in Internet Explorer

When you view Case Builder in Internet Explorer 8, you cannot see the toolbar buttons on the Rules and Activities pages.
- Cannot add a column to display the case type for a work item in an in-basket

You cannot add case type as a property in an in-basket in Case Builder. You must use IBM® FileNet Process Designer to configure an in-basket to display case types.
- Columns overlap when sizes are set too large in the page designer

When designing a page, the columns may overlap if the settings for the width or height exceed the page design area.
- Troubleshooting overlap and gap warnings in table-based rules

When you edit table-based business rules, you might receive overlap and gap warnings.
- Cannot view values when you edit cells in table-based rules

When you type values in the cells of a table-based business rule, you cannot see the values until you press Enter.
- Comments in scripts cause a validation error

If you enter a comment in the script for a script action or in the Script Adapter widget, Case Builder might return a validation error.
- Workgroups are not marked as required fields in the Properties widget

Workgroups are not automatically marked as required fields if you are using the system-generated view for the Properties widget.
- Event actions cannot have duplicate labels

An event action that is added to a toolbar or menu is overridden if another event action is added with the same label.
- Cannot validate the case types or deploy a solution after the data type or cardinality of a solution-level property is changed

If you change the data type or cardinality of a solution-level property, you cannot validate the case types that reuse the property and cannot deploy the updated solution.
- Problems occur in Case Client if widgets are configured incorrectly

If certain widgets are not configured correctly for the page on which they are used, the widgets do not work correctly in Case Client.
- Workflow artifacts are not added to the Content Platform Engine configuration file when the file is locked

If you insert a workflow into a case type or collection when the Content Platform Engine configuration file is locked, the workflow artifacts are not added to the file.
- Unexpected behavior when you use choice lists that have duplicate values with unique display names

You might see unexpected behavior when you use duplicate values in choice   lists.
- Unexpected results when you use different default values for the same property

Users can experience unpredictable behavior when you configure different default values for separate instances of the same property.
- Bi-directional step names do not display in the Step Designer swimlane

Using the Chrome browser in a bi-directional locale can cause display issues in Step   Designer.
- Fields in the Settings pane of the Properties View Designer lose focus in Internet Explorer

If you are working in Internet Explorer, the Name field for workflow fields and the Collection ID and Property ID fields for external properties lose focus each time that you type a character.
- Focus is lost when some settings in Properties View Designer are changed

When you specify some settings in Properties View Designer by selecting an option from a list, the focus is lost and you must manually restore the focus.
- The test solution link in Case Builder can redirect to the SiteMinder login page

In a SiteMinder SSO environment, when you click Test to preview your solution for the first time, you might be redirected to the SiteMinder login page.
- Changing the type of a property that is used in in-baskets, in-basket filters, or activities

Before you change the data type of a property that is used in in-baskets, in-baskets, filters, or activities, you must remove the property from in-baskets, filters, and activities.
- If you change an activity start from discretionary to manual or automated, Case Builder does not clear the response from the launch step

When you start a discretionary activity, you can assign a response for the launch step in the Step Designer. Later, if you change the activity to start manually or automatically, the response is not cleared from the launch step.
- Percent signs (%) and underscores (\_) do not work in case property filters

If you include a percent sign (%) or an underscore (\_) in a filter value, the filter does not work as expected.
- Adding many properties might cause a script warning message

If you add many properties at a time in Case Builder, you might receive a warning message that a script is taking too long.
- Inconsistent behavior when adding the same property in multiple in-baskets in the same queue with different object types

If you try to update the object type of a property that is used in multiple in-baskets in the same queue without first saving and closing the solution, the object type might not be set correctly.
- Activities cannot be assigned to new sets before you save and close the solution

If you create a set in Case Builder and then try to assign an existing activity to that set, the activity is not successfully assigned to the set.
- Unexpected results when you use a number spinner editor with a property of type float

In Case Builder, you configure a float property to use a number spinner editor and you select the Round automatically option. In Case Client, the value of that property is unpredictable if the user clicks the arrows in the number spinner multiple times.
- Preventing users from having to select a folder when they add documents

You can configure a case type setting in Case Builder that allows users to add documents from non-case management repositories. However, with this setting, users might be required to select a folder when they add a document.
- Earlier minor versions of Internet Explorer 10 or 11 can cause issues with workflow applications

If your browser is an older, minor version of Internet Explorer 10 or 11, you might experience unexpected behavior in Case Builder and Case Client.
- Certain property templates cannot be used in IBM Business Automation Workflow

Certain property templates cannot be used in IBM Business Automation Workflow properties.
- Case and attachment documents with non-English-language titles are added to email with incorrect titles

When you use the Case Information widget or the Attachment widget, case documents and attachment documents that have a non-English-language title are added to email with the incorrect title.
- Cannot open IBM Process Designer from Case Builder

If the URL to the workflow server host is not configured correctly, you cannot open Process Designer from Case Builder.
- Queue changes might not take effect after a solution is deployed

When you edit a solution workflow collection by using the Process Configuration console that is launched from IBM FileNet Process Designer, changes to queue security and component queue properties might not take effect after the solution is deployed.