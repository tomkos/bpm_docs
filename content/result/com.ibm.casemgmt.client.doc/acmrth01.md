# In-baskets

You use an in-basket to view, open, and work with work items assigned to you or
others.

- If you are upgrading from IBM® Case
Manager, the in-basket is
different in IBM Business Automation
Workflow. The workflow in-basket is federated,
and displays work items for process work items and FileNet® P8 system work items. If you have
any custom request or response filters for in-baskets, you need to make changes as the service
endpoint is different from the federated in-basket.

Typically, the in-basket widget contains separate tabs for your personal in-basket and for each
in-basket that is associated with a role.

The personal in-basket displays the work items that are assigned directly to you.
You can select any work item in your in-basket, open it to complete the item, reassign it to someone
else, or view its attachments or data fields. The person who designed the application can prevent
users from reassigning work items.

The personal in-basket also lists work items that are already claimed by the current user or are
available to be claimed. Workflow work items that were associated with a process external to a case
solution are no longer displayed in the in-basket. For more information on how to enable viewing
work items in the in-basket, see Including work items with existing processes in the in-basket.

A role in-basket provides access to work items that are assigned to a group of
people who share a role. The role in-basket can be configured to display a list of work items from
which anyone in that role can select the next item to work on. Alternatively, the role in-basket can
be configured to work on one item at a time. For more information, see In-baskets widget.

You can move a work item from the role in-basket to your personal in-basket for processing,
or you can also process the item from the role in-basket. Because access to a role in-basket is
determined by the person who designed the application that you are using, you might not be able to
see a specific role in-basket. Additionally, you might not be able to reassign work items or move
them to your personal in-basket.

The all assigned work in-basket lists all the open work items that are assigned to or claimed by
users. Work items that are assigned to roles are not listed. You can filter the list to display only
the work that is assigned to a specified user. Only users in specific roles can access this
in-basket. Access is determined by the person who designed the application that you are using. For
workflow process work items, only a user who is a member of the tw\_admins group can
see all of the claimed work items that are associated with all users.

- By default, the property values for FileNet Process Engine work items that are displayed in the
In-basket are updated even if you merely save changes to a work item. This can be disabled if a
business analyst updates the Event Update flag for properties to
FALSE in FileNet Process
Designer.

- The conditions are case-sensitive.
- If you exceed the maximum length of a string data field, you get a message that the In-basket
widget cannot get the queue elements. Character limits might vary depending on your
language.
- The number of displayed items reflects the total number of filtered work items that are in the
in-basket. Because many work items cannot be retrieved in a single query to the server, a pagination
filter breaks down the large number into smaller batches. The default pagination configuration
enables the retrieval and display of up to 50 work items per scrolled page. The paging size is
configurable, and you can change the default value by using the Number of work items in
In-basket page option in the IBM Business Automation
Workflow client plug-in.
- To include special characters in a filter entry, use the '\' character before the special
character. Example, for nov\_2014, enter nov\_2014. The filter values
eventually pass down to the database and depending on the database, escaping single or double
quotation marks are done differently: To escape a single or a double quotation mark for Db2 and
MSSQL databases, you need to type the character twice. Example, for George's, enter
George''s and for Top"Hat enter Top""Hat.

- Scroll bar for the In-basket widget remains in the same position while moving through pages. For
example, if on page 1, the scroll bar is at the bottom of the page, moving to another page, the
scroll bar remains at the bottom.
- Filter case sensitivity - For case sensitivity to work accurately with FileNet P8 work item filtering, you need
to ensure proper settings in the database and set in the target object store of the Content Platform Engine.
- To filter and sort the case properties and activity properties for process work items in
in-baskets, see Filtering and sorting process work items in in-baskets.

- View information about the work item and information about the associated case.
- Edit work item data, including case properties.
- View, check out or check in, and edit the properties of documents that are attached to the work
item. You can check out, check in, cancel checkout, or view properties for documents that are stored
only in the content repository. For FileNet P8 documents, you can select the
version of the document that you want to work with.
- Add a comment to the work item for others to read.
- Attach another document to the work item by clicking Add.Restriction: You can attach any document, including system files such as workflows and entry
templates, only if they are stored in the content repository.
- Dispatch the work item to the next step by clicking Complete or one of
the response buttons that are configured for the work item.

- If the number of listed items is equal to or smaller than the default number of items per page,
the sorting and filtering of the list are optimal. The list displays the expected mix of FileNet P8 and workflow items, which are
sorted and filtered based on the specified criteria. The default page size is 50.
- If the number of items is larger than the default page size, the sorting of the work items is
different, namely FileNet P8
items are displayed first, followed by the workflow items. Legacy FileNet P8 work items are listed at the
end.
- To prevent inefficient filtering when using query filters, where rules are defined as filtering
criteria, avoid the like operator in the rules.
- For troubleshooting known functional gaps when using process work items with case in-baskets,
see here.