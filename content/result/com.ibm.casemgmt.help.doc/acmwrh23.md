# In-baskets widget

You use the In-baskets widget to enable users to view
  and work with work items.

- If you are upgrading from IBM Case Manager, the in-basket is federated and displays work items
for workflow process work items and FileNet® P8 system work items. If you have
any custom request or response filters for in-baskets, you need to make changes as the service
endpoint is different from the federated in-basket.

Alternatively, you can configure the role-based in-basket to
hide the work items. In this configuration, Open Next Work item takes you to
the beginning of the work item list in the in-basket and continues down the list. The
Open Next Work Item in Sequence processes the next sequential work item in
the queue.

The personal in-basket also lists tasks or work items that are
already claimed by the current user or are available to be claimed. These external tasks were
created and started in the IBM Business Automation Workflow 18.0.0.2 release. Earlier workflow
activities that were started from an older Business Automation Workflow release is not
displayed.

- assign a manager team/role to the case role
- add the non-admin user to the manager team/role that is assigned to monitor the work items

- The property values that are in the in-basket are updated only when a case worker completes a
work item. The values are not updated if a case worker merely saves changes to the work item.

- One personal in-basket for a solution
- One in-basket for each role in a solution

- Customize the content that is displayed by specifying the role that is associated with the
widget.
- Configure a menu or toolbar with custom actions.

## Workflow pages that include this widget by default

The In-baskets widget is included on the Work page.

- Configuring content displayed for the in-baskets widget

You can configure the content that is displayed in the role-based in-baskets in the in-basket widget.
- Configuring reassignment items in the In-baskets widget

You can configure the task reassign action to restrict the role members when you are reassigning tasks in the In-basket widget.
- Including work items with existing processes in the in-basket

Use a configuration option to include work items that are configured with existing workflow processes or external processes in the in-basket.
- Filtering and sorting process work items in in-baskets

In workflow process work items, you can retrieve and display the case properties and activity properties value in the in-basket columns. You can filter and sort the case properties and activity properties for process work items in in-baskets.
- In-baskets widget events

The In-baskets widget uses events to display and process lists of the work items that are assigned to a user.