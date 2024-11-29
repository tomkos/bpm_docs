# Assigning work

## About this task

- View work that is assigned to individual users and reassign multiple
work items to other users in one action.
- Verify that users in certain user roles cannot assign work to
others.
- Complete work assignments by user role and from the LDAP directory.

You can restrict the users when you are reassigning work items for the targeted users. You can
filter the search for users, who are assigned to specific solution roles instead of searching from
the entire LDAP directory by default.

- What user to log in as to be able to assign work items.
- The work items that you want to reassign. Case Client shows all in-baskets that are
associated with a role, and these in-baskets contain the work items. If the application was designed
to include the All Assigned Work Items in-basket, then you also see an
in-basket that contains all work that is assigned to users.
- The user that you want to reassign work items to. You can use one of the following methods findsand select users, depending on the application design: Restriction: When you assign work by selecting a role, you see all users in a roleand you can filter the list of users. However, you cannot search for users across roles.
    - Search in the directory service provider by selecting the Search All
Users option.
    - Select a role, and then select a user that is assigned to a specific role. If you have
permissions to modify role membership, the list of roles includes all roles. If you do not have
modify permissions, then the list includes roles that you belong to.
- Whether to assign one or more work items from one user to another. You can select a list of work
items in any in-basket for the Reassign, Move item to Personal
In-basket or Return Item actions. These actions are shown only if
you have a role that has the appropriate permissions to do these actions.
- The case folder security in the target object store controls the access to a work item that is
associated with a case. When you (as user) open a work item for a particular case type, security is
validated on the case to determine whether to display the work item to you as a user. See how the
case teams are implemented in Managing access to cases. The case team membership is validated
before the case or the work item is displayed to you.  Note: Roles do not control security on the
cases or work items that is mainly a way to organize users and groups. You (as admin) can assign
work items to users in a different role. Similarly, a link (for example, email notification) to a
particular work item can be sent or accessed by a user that does not belong to the same role. The
user can open and process the work item, if the user has access to the case or is part of a case
team, and has access to the roster and queue where the work item resides. To prevent a user from
opening a case-related work item, you must secure the case by applying security on the case folder
and its related content objects.

## Procedure

To assign work items:

1. Log in to Case Client as
a user with a role to reassign work items, such as the Supervisor
role.
2. From the In-basket page, determine
which work items you want to reassign. Find the in-basket that contains
the work items.
3. Select the work items and click Reassign.
4 Select a user in a specific role or search for a username. Option Description To assign the item to a user in a specific role. Select a role from the Roles section of the Reassignitems dialog box, and select a user from the list of users in that role. To search for a username.

| Option                                           | Description                                                                                                                   |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| To assign the item to a user in a specific role. | Select a role from the Roles section of the Reassign items dialog box, and select a user from the list of users in that role. |
| To search for a username.                        | Click Search for a user. Enter the search criteria for the username. Click Search. Select a user from the results list.       |

5. Click OK.
Multiple
work items are reassigned to the specified user.
6. Refresh the in-basket of the selected user to see the new
work items.