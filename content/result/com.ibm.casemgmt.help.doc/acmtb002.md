# Solution deployment fails due to a queue table limit

## Symptoms

```
12/6/10 12:35:21 PM PST FNRPA0032E The solution cannot be deployed because 
the Content Platform Engine configuration document could not be found. See the following 
error: Too many user defined fields in queue table (limit of 220?), table 
name=DefaultWPCTable
```

## Causes

The
case management database has a limit of 220 columns per queue, and
there is one queue for each role in-basket. Each property that you
add to a case requires a column in the database. If you deploy multiple
solutions with large numbers of properties to your test environment,
you can exceed the column limit.

Once you reach the limit and
receive the FNRPA0032E error message, you must reset the test environment
to clear the tables. Resetting the test environment removes all of
your deployed solutions and other data from the development target
environment and reinitializes the isolated region.

## Resolving the problem

- In Case Builder, click Actions > Reset Test Environment on the Manage Solutions page.Note: Resetting the test
environment removes all the data from the development target environment, including any FileNet® P8 assets that you copied from your production environment and any
assets you created outside of Case Builder to extend the solution
design, such as search templates or form templates.