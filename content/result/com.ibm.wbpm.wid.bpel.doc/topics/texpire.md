<!-- image -->

# Defining timer-driven behavior in a BPEL process

## About this task

To set a timer value, proceed as follows:

## Procedure

1. In the Properties area for the activity or element, click
either the Details or the Expiration tab.
2. To create an expiration condition using the process' default
expression language, click Create a New Condition. Otherwise, choose an appropriate language from the drop down menu.
You will have the following choices:

Option
Description

Java™
If you choose this, then you will be able to compose the expiration
expression in the Java programming
language using either the visual snippet editor, or a text editor.
With this option, you will be able to configure either a date or a
duration expression. 

No Expression
This is the default, empty setting.

Same as Process
This is automatically set to be the same as the expression
language that is being used by the BPEL process (it will either be Java or XPath 1.0).

Timeout
If you choose this, then you will be able to simply enter
a duration value, and expiration will occur the moment this period
has passed.

XPath 1.0
Choose this to compose the expressions in the XPath 1.0 programming
language, using either the XPath Expression Builder, or a text editor.
With this option, you will be able to configure either a date or a
duration expression.
3. If you choose Timeout, you will
have the following options to configure the period of time that the
activity should hold.

Option
Description

Simple calendar
This is, as the name suggests, is a simple arithmetic calendar.
Use the Timeout Duration fields to select the
amount of time that this activity should wait for an action to occur
before it expires. How the value of a time duration is consumed
depends on the calendar runtime that you use, which applies for directly
entered values for the simple and business calendars or indirectly
through the user interface. Usually values such as months or longer
are calculated differently for non-Gregorian calendars like the Hijri
calendar.

WebSphere® CRON
calendar
This is a built-in calendar that uses a list of term expressions
representing elements of time to calculate the interval.

User-Defined calendar
Use this option to select a calendar other than those provided.
You can use the fields to name the calendar, and point to a valid Java Naming and Directory Interface
(JNDI) location.

Business calendar
In addition to the three regular options in the Calendar Type field, more options will appear if a business calendar is available. A business calendar can be used
to model duration values for time-sensitive aspects of your BPEL process
in order to account for such variables as regular working hours, weekends,
and holidays. See Using business calendars within a BPEL process for more information.
4. For all other expression language choices, you will be
presented with the following two options:

Option
Description

Date
Choose this when you want the expiration to occur when a specific
time and date has been reached.

Duration
Choose this when you want expiration to occur after a certain
period of time has elapsed.
5. Depending on the expression language that you are using,
you can choose from any of the following expression types:

Option
Description

Visual
Choose this to use the visual snippet editor to graphically
compose Java code.

Java
Choose this to write a Java expression yourself.

Literal
Choose this to enter values directly into customized fields.
Calendar values are represented in Coordinated Universal Time (UTC).

Text
Choose this to compose an XPath expression.

## Results

- Expiration is a BPEL extension, so the tab will not appear in
the Properties area if these capabilities were disabled when the process
was created. See Working with BPEL extensions.
- Timer specifications are ignored for microflows and synchronous
invocations.

- Using business calendars within a BPEL process

When it comes to modeling duration values for time-sensitive aspects of your BPEL process, you can use a business calendar to account for such variables as regular working hours, weekends, and holidays.

## Related tasks

- Configuring the wait activity
- Setting duration values for your human task
- Using business calendars within a BPEL process
- Creating an escalation for your human task
- Selecting a calendar type for your escalation
- Using business calendars within human tasks
- Notifying an event handler of an escalation

## Related reference

- Expiration tab: BPEL process editor
- Details tab: business state machine editor
- Duration tab: Human Task editor