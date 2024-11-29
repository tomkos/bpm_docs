<!-- image -->

# Testing a human-centric process

## About this task

Before you can begin, you will need to have the
exported process in the form of a project interchange file. This export
must have clearly defined staff information that can be used to populate
the test people directory.

## Procedure

1 To import the project interchange file: The new module will appear in the Physical Resources view.There will be two administrative scripts. One will be to populatethe people directory, and the other will be to clean that registryonce you've completed your testing.
    1. In the Business integration view, click File > Import.
    2. In the Import window, select Other > Project Interchange.
    3. Browse to the project interchange file, select it, and
click OK.
    4. Select all of the projects in the zip, and click Finish.
2 Run the administrative script that populates the test peopledirectory. This will create the test user account(s) and associatedgroup(s). The test user entries are created in the registry. Tosee the user(s) in the Administrative Console, click Users and Groups > Manage Users . Similarly, to see Groups, click Usersand Groups > Manage Groups .

1. In the Physical Resources view, expand the new project
until you see the Administrative scripts. They have a PY extension.
2. Right-click your server, and select Run administrative
script.
3. Browse to the script and click Run.
3 To test the process:

1. In the Assembly diagram, right-click the process and
select Test Component.
2. Launch the Business Process Choreographer explorer,
and log in as a test user. You will note that the user's To-dos list
will be empty.
3. In the Events page, enter some test parameters, and
click the Continue icon, select a deployment
location and click Finish.
4. When the test server is running, return to the Business
Process Choreographer explorer, and check the To-dos list.
You should now have an entry that you can complete as needed to test
the process.
4. When you are done your testing, run the administrative
script that cleans the test people directory.