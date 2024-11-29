# Configuring production target object store indexes

## About this task

The index contains unique
key values, and the four-part index uses the following format: <case\_folder\_column,
audit\_sequence DESC, object\_class\_id, source\_object\_classid>.

## Procedure

To create the four-part index:

1. If you previously created the two-part index, drop the
index permanently.
2 Use Administration Console for Content PlatformEngine toidentify the database column name of the CmAcmCaseFolder propertyin the Event table. Record the values for the TableDefinitionand ColumnId properties for the CmAcmCaseFolder property in the targetobject store.
    1. Navigate to Target
Object Store > Data Design > Classes > Other Classes > Event.
    2. In the Properties tab, sort on Property Name.
    3. Scroll down to find the property Table Definition and
record the value.
    4. Click Property Value.
Another Administration Console for Content Platform
Engine tab opens.
    5. Open the Column Definition dropdown
list and select column CmAcmCaseFolder.
The Column Definition Properties tab opens.
    6. Record the value of the property Column Name.
3. Use your database tools to create the four-part index with
the following form:  <case\_folder\_column,
audit\_sequence DESC, object\_class\_id, source\_object\_class\_id>.
The audit\_sequence field of the index must be specified as DESCENDING.
4. Repeat this procedure for each target object store in your
production environment that uses IBM Business Automation
Workflow solutions.