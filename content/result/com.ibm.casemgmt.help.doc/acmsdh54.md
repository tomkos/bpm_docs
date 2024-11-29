# Multiple user editing of solutions

Some solution assets are associated with specific configuration
files. If any one of these assets is being edited, the other assets
that are associated with the same file are unavailable for editing.
When multiple users are editing a solution, the behavior for the various
solution assets is as follows:

| Asset                                                                                                                                                                                      | Availability                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pages                                                                                                                                                                                      | A page can be modified by only one user at a time. If a page is being edited, it is locked until the page is saved and committed. Users can create or edit other pages while a page is being edited.                                              |
| Business rules                                                                                                                                                                             | A business rule can be modified by only one user at a time. If a business rule is being edited, it is locked until the business rule is saved and committed. Users can create or edit other business rules while a business rule is being edited. |
| Views                                                                                                                                                                                      | A view can be modified by only one user at a time. If a view is being edited, it is locked until the view is saved and committed. Users can create or edit other views while a view is being edited.                                              |
| Content Platform Engine configuration file assets:  in-baskets or roles                                                                                                                    | If any asset that is associated with the Content Platform Engine configuration file is being edited, all similar assets are locked. Only one user can edit assets from Content Platform Engine at one time.                                       |
| Solution definition file (SDF) assets: properties, document classes, case types, case folders, case summary view, case search view, choice lists, solution descriptions, or solution icons | If any asset that is associated with the SDF is being edited, all similar assets are locked. Only one user can edit any SDF assets at one time. When another user is editing an SDF asset, some SDF assets might be available for viewing only.   |
| Solution workflow definition file assets: activities                                                                                                                                       | If any activities that are associated with the solution workflow definition file are being edited, all similar assets are locked. Only one user can edit an activity at one time.                                                                 |

When you save changes to an asset, those changes are saved as drafts
until you commit the changes. If you deploy the solution before the
changes are committed, the draft changes are not included in the deployment.
When lists of available items are displayed in Case Builder, such as attachments
and predefined workgroups, the lists include committed items only.

- If you want the list of available items to include an item that you created in another activity
but did not yet commit, first open the activity with which the item is associated. For example, you
previously added an attachment to activity A but did not yet commit the changes. If you want to add
that attachment to activity B, ensure that you first open activity A before you open activity
B.
- Before you commit your solution, you can click Validate onthe solution home page to ensure that none of the following assetswere deleted by another user while you were editing the solution:
    - Properties, roles, or step pages that are used in a workflow
    - Properties that are used in an in-basket
    - Activities or case pages in a case type

For assets that are associated with a configuration file, the file
is locked when an asset is created in the file. For example, if you
are creating a new property or editing an existing one, the file is
not locked until you click OK.