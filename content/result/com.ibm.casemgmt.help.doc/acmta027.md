# Solution deployment fails with a Content Platform Engine views error

## Symptoms

You receive the following error message: ERROR
FNRPA0032E The solution cannot be deployed because the Process Engine
configuration document could not be imported. See the following error:
Cannot create new views; old views deleted. Run transfer or re-create
views. The old database views for queues, rosters, and event logs
have been deleted, but the new views could not be successfully created.
The transfer or view creation option must be done again to properly
create the views, after whatever problem that caused view creation
to fail has been fixed. See the chained exception for the problem
that caused the view creation to fail. java.lang.Exception: ORA-00972:
identifier is too long

## Causes

One or all of the following solution elements is too
long: solution name, role name, case type name, or field name.  Process
Engine generates the database view names for the event log that maps
to the case type unique name, the queue that maps to the role unique
name, the roster that maps to the solution name, and field name. If
the view name is too long, Content Platform Engine automatically
truncates the view name to be within 30 characters.

However,
even with automatic truncation, the database view names might still
exceed 30 bytes, the restriction set by the Oracle database,  if a
character is more than 1 byte.

## Resolving the problem

Use Case Builder to
assign a shorter name for the solution, role, case type, or field
name. The name limits are documented in the FileNet® P8 product documentation.
After you shorten the names and save the solution, redeploy the solution.