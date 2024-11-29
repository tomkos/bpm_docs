<!-- image -->

# Adding data pools

## About this task

## Procedure

1 Depending on whether the integration test client is currentlyopen, complete one of the following steps: The New Data Pool wizard opens.
    - In the Events page of the integration test client, click the
down arrow beside the Data Pool icon  and select New.
    - From the workbench menu bar of the Business Integration perspective,
select File > New > Data Pool.
2 Complete one of the following steps:

- If you want the Project field to display
only component test projects, ensure that the Show only
test projects check box is selected. (It is recommended
that you save your data pool file in a component test project because
you may not want your testing artifacts to be deployed to a server
with a module.)
- If you want the Project field to display
all available projects, clear the Show only test projects check
box.
3. In the Project field, select the
project where you want to save your data pool file.
4 If you want to save the data pool file in a different folderthan the default Data folder, clear the Default checkbox and then complete one of the following steps:

- If you want to save the data pool file to an existing folder,
click Browse and then navigate to the folder
and select it.
- If you want to save the data pool file to a new folder,
type the name that you want to assign to the new folder in the Folder field.
5. In the Name field, type the name
that you want to assign to the data pool file.
6. If you want to specify the new data pool as the default
data pool, select the Set this data pool as the workspace
default check box. (Note that this check box is disabled
if there is no default data pool already specified in the Preferences
page for the integration test client. This is because the first data
pool that you create will automatically become the default data pool.
Information about specifying or changing the default data pool is
found in the topic "Specifying a default data pool.")
7. Click Finish. The data pool editor
opens. Information about editing data pools is found in the topics
"Value and data pool editors", "Adding values to data pools" and "Using
values from data pools."