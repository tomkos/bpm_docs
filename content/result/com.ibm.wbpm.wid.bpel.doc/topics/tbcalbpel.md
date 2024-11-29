<!-- image -->

# Using business calendars within a BPEL process

## About this task

To use a business calendar in a BPEL process, proceed as follows:

## Procedure

1. If you have not already done so, create a business calendar
or import one from WebSphere® Modeler. For detailed instructions on how to do this,
refer to Business calendars.
2 Drop an activity with a time-sensitive aspect onto thecanvas. Possible activities include:
    - wait,
    - invoke,
    - human Task,
    - Timeout element in an eventHandler
3. Select the activity on the canvas, and click the appropriate
tab in the Properties area. For
a wait and invoke activities as well as the timeout element, this
would be the Details tab, and for the invoke
and human task activities, this would be the Expiration tab.
4. From the Expression language list,
select Timeout.
5. From the Calendar Type list, select
the business calendar that you created or imported in Step 1.
6. Using the Timeout Duration fields,
select the amount of time that this activity should wait for an action,
knowing that the business calendar will compensate for all non-contiguous
aspects of the interval of time.

## Related tasks

- Defining timer-driven behavior in a BPEL process
- Setting duration values for your human task
- Configuring the wait activity

## Related reference

- Expiration tab: BPEL process editor