# Wiring Viewer widgets to display documents from different widgets

## Procedure

In the following steps, assume that a page contains a
Content List widget and a Case Information widget with the Documents
tab enabled. To display the documents from each widget in a different
instance of the Viewer widget, follow these steps:

1. Open the page that contains the Content List widget and
Case Information widget in Page Designer.
2. Drag two Viewer widgets onto the page.

Tip: There is no label to distinguish the Viewer widgets in Case Client. Therefore, place each
Viewer widget on the page to emphasize its relationship to the Content
List widget or Case Information widget.
3 Wire the Content List widget to the first Viewer widgeton the page:
    1. Click the Edit Wiring icon for
the Content List widget.
    2. In the Content List Outgoing Events area,
select Document opened from the Outgoing
event list.
    3. Select the first instance of Viewer from
the Target widget list.
    4. Select Open document from the Incoming
event list.
    5. Click Add Wire.
    6. On the Event Broadcasting tab,
clear the Enabled check box for the Document
opened event.
Disabling event broadcasting
prevents the Document opened event from being broadcast automatically
to the other widgets on the page.
4 Wire the Case Information widget to the second Viewer widgeton the page:

1. Click Edit Wiring icon for the
Case Information widget menu.
2. In the Content List Outgoing Events area,
select Document opened from the Outgoing
event list.
3. Select the second instance of Viewer from
the Target widget list.
4. Select Open document from the Incoming
event list.
5. Click Add Wire.
6. On the Event Broadcasting tab,
clear the Enabled check box for the Document
opened event.
Disabling event broadcasting
prevents the Document opened event from being broadcast automatically
to the other widgets on the page.
5. Save and deploy the solution.