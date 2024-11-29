# Work items for a deployed solution whose name exceeds 58 characters do not display in a
personal in-basket

## Symptoms

If your solution name exceeds 58 characters, the work
items do not display in a personal in-basket after the solution is
deployed.

## Causes

## Resolving the problem

1. In IBM
FileNet Process Designer open
the solution.
2. Click View  > Configuration.
3. Right-click the Inbox queue and select Properties.
4. Open the Data Fields tab.
5. Change the length of the SolutionIdentifier data
field to a new value. The new value is calculated by adding the
length of the solution name and six additional characters.
6. Save the solution.

1. In Process Configuration Console, connect to the Content Platform Engine isolated region.
2. Right-click the Inbox queue and select Properties .
3. Open the Data Fields tab.
4. Change the length of the SolutionIdentifier data
field to a new value. The new value is calculated by adding the
length of the solution name and six additional characters.
5. In Process Configuration Console, commit the change.