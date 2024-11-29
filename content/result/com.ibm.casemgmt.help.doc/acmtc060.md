# Case packaging action is not displayed on Case Details or Cases page for existing
solutions

## Symptoms

## Resolving the problem

For solutions that are created in version 5.2.1 Fix Pack 4 or later, the case packaging action is
displayed by default on the Case Details and Cases pages. For solutions that were created before Fix
Pack 4, the case packaging action must be manually added by editing the solution in Case Builder.

To add the case packaging action to a solution that was created prior to version 5.2.1 Fix Pack
4:

1. Open the solution in Case Builder.
2 Add the Create Package button to the Case Toolbar widget on theCase Details page.
    1. On the Pages tab, open the Case Details page.
    2. In Page Designer, click the Edit Settings icon for the Case Toolbar
widget.
    3. On the Toolbar tab, select the Editing a case
toolbar.
    4. Click the Add Button icon and select the Create
Package action.
3 Add the Create Package menu action to the Case List widget on theCases page.

1. On the Pages tab, open the Cases page.
2. In Page Designer, click the Edit Settings icon for the Case List
widget.
3. On the Menu tab, click the Add Menu Item icon and
select the Create Package action.
4. Save and redeploy the solution.

To add support for non-English locales, see the last section in createCasePackage operation.