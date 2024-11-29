<!-- image -->

# Limitations for the integration debugger

Some of the more common limitations encountered when using the
integration debugger are:

- A business process running in the debugger is not picking up your changes
- Old breakpoints are causing problems or confusion

These limitations are discussed in the following sections.

## A business process running in the debugger is
not picking up your changes

If you are debugging a business process
in the Debug perspective and you find that you need to edit the process, it
is recommended that you first run the process to completion by repeatedly
clicking the Resume button until the process exits.
When you have finished running the process to completion, you can then edit
the process. If you edit the process while the server is running, it is generally
recommended that you right-click your server in the Servers view and select Publish.
Although some changes to business processes will automatically be picked up
by a running process instance, selecting Publish will
ensure that all of your changes will be picked up.

## Old breakpoints are causing problems or confusion

When
debugging business processes, there are some situations where you should manually
remove your old breakpoints to avoid encountering problems or confusion in
your debugging tasks.

For example, if you have set breakpoints in a
condition that you built using the visual snippet editor and you then decide
to further develop the condition by editing the Java™ code directly, you should remove the
old breakpoints that you added in the visual snippet editor. Similarly, if
you have set breakpoints in a condition that you built by editing the Java code
directly and you then decide to further develop the condition by editing the
condition in the visual snippet editor, you should remove the old breakpoints
that you added by editing the Java code directly.

Another situation
where you may need to remove old breakpoints is when you are working with
a business process expiration condition (for a Staff or Invoke activity) or
a time-related condition (such as a Wait activity or onAlarm activity). For
example, if you switch from the Duration setting to the Date setting,
any breakpoint that was set in the Duration setting is not properly
removed and you must manually remove it. Similarly, if you switch from the Date setting
to the Duration setting, any breakpoint that was set in the Date setting
is not properly removed and it must be manually removed.