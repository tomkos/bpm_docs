# Business Process Choreographer Archive database upgrade troubleshooting

```
ALTER TABLE bpcarchive.PROCESS\_TEMPLATE\_B\_T ADD CUSTOM\_TEXT8  VARCHAR(64)     
DB21034E  The command was processed as an SQL statement because it was not a valid Command Line Processor command.  During SQL processing it returned:SQL0670N  The row length of the table exceeded a limit of "4005" bytes. (Table space "CEI\_TS\_BASE4K\_PATH".)  SQLSTATE=54010
```

1. Export the data from the table.
2. Create a new table space at least 8K in size.
3. Drop all indexes created on the table.
4. Drop the table.
5. Re-create the table and its indexes.
6. Import the data into the table.