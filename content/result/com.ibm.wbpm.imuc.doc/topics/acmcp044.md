# Exporting business rules to IBM Operational Decision
Manager

## Procedure

To export business rules to IBM Operational Decision
Manager:

1. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. In the navigation tree in the left pane, select a design
object store and click Solutions.
3. On the Solutions page in the right
pane, select the solution with business rules that you want to export.
4. Click Actions > Export > Business Rules and complete the
wizard steps.
5. After the rules are exported, download and save the exported
rules archive file.

## What to do next

The exported archive file contains individual archive
files for each business rule that is associated with the solution.
The individual rule archive files are organized according to the case
type with which they are associated. Extract the exported archive
file, and then import the individual rule archive files into the IBM Operational Decision
Manager Rule Designer or Decision
Center.

If you export rules from solutions that are from a different
persistence locale, you must import the rules into Rule Designer and refactor them to provide a
vocabulary and parameters that can be associated with the persistence locale. After the rules are
refactored, use Rule Designer synchronization commands to publish the project to Decision Center. If
your exported rule projects already support the IBM Operational Decision
Manager
persistence locale, you can import them directly into Decision Center. For more information, see the
IBM Operational Decision Manager documentation.

## Related tasks

- Adding business rules from IBM Operational Decision Manager to a solution