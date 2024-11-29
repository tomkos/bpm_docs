# Setting the order of the dashboards in Process Portal for
a user group

## About this task

Users
can reorder dashboards in Process Portal, and
the order is saved when they log out. However, someone with administrative
privileges might need to apply an order for all users in a group so
that all users see the dashboards and saved searches in the same order.
To apply the order from one user to all users in a selected user group,
copy the attribute value from the user and paste it in as the value
for a user group.

## Procedure

1. In the Server Admin area of the Process Admin Console,
click User Management > Bulk
User Attribute Assignment.
2. Click View by User.
3. Copy the order from a user by selecting the user ID and
copying the value for the user's Portal Dashboard Display
Order attribute.  For example, if you decide
that your dashboard order should be applied to all users in a group,
select your user ID and copy the attribute value.
4 Apply the order to all users in a group.
    1. Click View by Attribute, and
then select the Portal Dashboard Display Order attribute.
    2. Select the name of the user group.
    3. In the Specify a Value and Assign it to the
Selected Users section, delete any existing entry, and
paste the entry that you copied in step 3 into the attribute value
for the tab order.
    4. Click Assign.
5. Process Portal only. In the administrative
console, configure the com.ibm.bpm.portal.defaultDashboardDisplayOrder mashups
property with the value from step 3: 
For more information, see Configuring custom properties.

## Results

The next time that users in the user group log in to Process Portal, the
dashboards in the navigation pane are displayed in the new order.
Users in the group can reorder dashboards as they like, but the default
order is what you specified.