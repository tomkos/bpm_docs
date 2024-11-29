# Cannot add a column to display the case type for a work item
in an in-basket

## Symptoms

## Resolving the problem

1. On the Manage Solutions page in Case Builder, click More Actions > Open IBM
FileNet Process Designer for
your solution.
2. In the Case Type Selection window, select
any case type from your solution and click OK.
3. Click View > Configuration.
4. Expand Work Queues, right-click the role
queue for which the in-basket is used, and click Properties.
5 Click the In-baskets tab and add case typesas a column:
    1. Click the Add icon and select CmAcmCaseTypeID
(Guid) in the Available Fields list.
Then, click OK.
    2. Change the label for the column.Important: Do not enable the case type column for sorting. If
you do enable sorting, the results are inconsistent because sorting
is sometimes done in the browser and sometimes on the server. Sorting
on the server uses the internal names of the case types. Sorting in
the browser uses the display names of the case types.
    3. Click OK > File > Solution > Save And Close.
6. In Case Builder, commit
your changes.