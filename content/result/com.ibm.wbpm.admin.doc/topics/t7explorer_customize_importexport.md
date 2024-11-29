<!-- image -->

# Reusing Business Process Choreographer Explorer or Business
Process Archive Explorer views

## About this task

Often the same views are needed in both Business Process
Choreographer Explorer and Business Process Archive Explorer. To transfer
these views from one client instance to the other, you can export
the views from Business Process Choreographer Explorer and then import
them in to Business Process Archive Explorer.

You also might
want to ensure that the views you have defined for an instance of
Business Process Choreographer Explorer running in a test environment
are also available to the clients running in the production environment
after successful completion of the tests. To avoid redefining these
views manually, you can export the views from the client in the test
environment and then import them to client instances in the production
environment.

If you have the system administrator role, you
can import and export views by completing the following steps.

## Procedure

1. Click Manage Views in the taskbar.
2 Export views from a client instance. In the Manage Views page, complete the following steps: The views are saved as an XML file. Tip: Ifyou cannot save the exported view, check the security settings ofyour browser.
    1. Expand the Export and Delete Views section.
    2. Select the view type. If you want to export
a view that belongs to a specific user, enter the user ID for the
user. Click Refresh.
    3 In the list of views, select one or more views, andclick Export . Restriction: If the view contains any of the following columns, you can only exportthe view to a Version 7.5 client instance.
        - Process App Acronym
        - Process App Name
        - Snapshot ID
        - Snapshot Name
        - Toolkit Acronym
        - Toolkit Name
        - Top-Level Toolkit Acronym
        - Top-Level Toolkit Name
        - Workspace Name
3 Import views in to a client instance. In the Manage Views page, complete the following steps: Imported views appear in your navigation pane. Users seethese views when they next log in to this instance of the client.Imported personalized views appear in the navigation pane of the ownerof the views the next time they log in to the client instance.

1. Expand the Import Views section.
2. Click Browse to find the XML
file that contains the views that you exported from another client
instance, and click Import. Tip: If you cannot import a view, check the security settings
of your browser.

<!-- image -->