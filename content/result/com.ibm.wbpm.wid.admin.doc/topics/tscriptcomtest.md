<!-- image -->

# Using scripts in common testing scenarios

## About this task

Your scripts and the tasks within them will vary based
on you particular situation. For example, if you know your test cases
rarely change then you can create a static set of tasks that do not
require any knowledge of the runtime environment. If your test case changes frequently, then your tasks need to know
something about the environment at run time.

If you are using
a version control system like Concurrent Versions System (CVS) then
your scripts will need to add tasks to get the files from that system
before running the script.

- Creating a script for test cases that rarely change

This section shows you how to create a script for test cases that rarely change.
- Creating a script for test cases that change frequently

Developing scripts for test cases that change frequently is presented in this section.
- Creating a script for test cases stored in a CVS repository

Test cases stored in a CVS repository require some special tasks in your script to extract them from the repository.