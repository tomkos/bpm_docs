# Configuring content displayed for the in-baskets widget

## Procedure

To configure the in-baskets widget:

1. Click the Edit Settings icon.
2. To configure the in-baskets for a specific role, select the role from the
Role list.
If you do not select a role, the changes apply to all roles that use this
Work page.
3. Set the following configuration options: 

Property
Description

Show work item counts for all in-baskets
Displays the work item count for all in-baskets that are associated with the role at the
first rendering of the in-basket widget.

Hide the tab if there is only one in-basket for the role
Hides the tab if only one in-basket is displayed for the selected role or roles.

Do not populate the in-basket until the dynamic filter is received 
Prevents the work items from being displayed in the in-basket until the filter is
received.

Only include a user's assigned tasks in the personal in-basket
To show only workflow process claimed work items in the personal in-basket.Note: When the
check-box is selected, "All users" team-assigned work items are not shown in
any in-basket. If the workflow process work item is external or was configured with existing
workflow and does not have any equivalent role in-basket, the work item is not displayed in any of
the in-baskets.
4. Select one of the following work modes:

Work Mode
Description

Show work items in role in-baskets
To enable the user to view and open work items in the role in-baskets. This mode gives a
user the ability to choose, which item to work on next.

Hide work items in role in-baskets
To prevent the user from choosing the item to work on next. Instead, an action toolbar is
added to the in-basket widget. The user clicks Open Next Work Item in
Sequence on this toolbar to open the next item in the queue. The Open Next
Work item takes you to the beginning of the work item list in the in-basket and
continues down the list. The item is opened in the Work Details page.
5 If you selected the Show work items in role in-baskets work mode,configure the following properties: The following table describes the results of the different combinations of setting the twoproperties that are related to locked items. Select the locked items to be displayed Allow user to show or hide work items that are locked by other users Result Work items locked by any user Selected The in-basket widget shows all work items, including work items that arelocked by other users. The user can hide or show the work items that are locked by otherusers. Work items locked by any user Cleared The in-basket widget shows all work items, including work items that arelocked by other users.The user cannot hide the work items that are locked by otherusers. Only work items locked by current user Selected The in-basket widget shows only work items that are not locked or that arelocked by the current user.The user can hide or show the work items that are locked by otherusers. Only work items locked by current user Cleared The in-basket widget shows only work items that are locked or not locked bythe current user.The user cannot show the work items that are locked by other users. Note: If you are working with work items in a random order from the in-basket list, then oncompleting a work item, you get a message about the other work items in your list.
    1. Indicate whether the in-basket shows work items that are locked by other users by selecting a
value from the Select the locked items to be displayed list.
    2. Indicate whether Case Client
users can override the display settings. This is to show or hide work items that are locked by other
users using the Allow user to show or hide work items locked by other users
check-box.
    3. If you want to prevent users from filtering the work items in the in-basket, select the
Hide the in-basket filter check-box.

| Select the locked items to be displayed   | Allow user to show or hide work items that are locked by other users   | Result                                                                                                                                                                         |
|-------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Work items locked by any user             | Selected                                                               | The in-basket widget shows all work items, including work items that are locked by other users. The user can hide or show the work items that are locked by other users.       |
| Work items locked by any user             | Cleared                                                                | The in-basket widget shows all work items, including work items that are locked by other users.The user cannot hide the work items that are locked by other users.             |
| Only work items locked by current user    | Selected                                                               | The in-basket widget shows only work items that are not locked or that are locked by the current user.The user can hide or show the work items that are locked by other users. |
| Only work items locked by current user    | Cleared                                                                | The in-basket widget shows only work items that are locked or not locked by the current user.The user cannot show the work items that are locked by other users.               |

6. Optional: 
If you selected the Hide work items in role in-baskets work mode,
provide instructions that tell the user how to open and process the next work item.