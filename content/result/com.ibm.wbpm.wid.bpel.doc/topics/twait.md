<!-- image -->

# Configuring the wait activity

## About this task

Your BPEL process might reach a point where it is necessary
to pause before continuing. An example would be a process which needs
a part to be delivered by a third-party before any further action
can be taken. In such a scenario you can use a wait activity to pause
the process for a set period of time, or until a certain date and
time.

To create and configure a wait activity, proceed as follows:

## Procedure

1. Drop a wait activity from the palette on to the canvas.
2. In the Properties area, click the Details tab.
3. To create an expiration condition using the process' default
expression language, click Create a New Condition.
Otherwise, choose an appropriate language from the drop down menu.
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
This is automatically set to be the same as the programming
language that is being used by the BPEL process. 

Timeout
If you choose this, then you will be able to simply enter
a duration value, and expiration will occur the moment this period
has passed.

XPath 1.0
Choose this to compose the expressions in the XPath 1.0 programming
language, using either the XPath Expression Builder, or a text editor.
With this option, you will be able to configure either a date or a
duration expression.
4. If you choose Timeout, you will
have the following options to configure the period of time that the
activity should hold.

Option
Description

Simple
This is, as the name suggests, a simple arithmetic calendar.
Use the Timeout Duration fields to select the
amount of time that this activity should wait for an action to occur
before it expires. 

WebSphere® CRON
This is a built-in calendar that uses a list of term expressions
representing elements of time to calculate the interval. Examples
of this type of calendar can be found in the Related Information section
below.

User-defined
Use this option to select a calendar other than those provided.
You can use the fields to name the calendar, and point to a valid Java Naming and Directory Interface
(JNDI) location.

New Business Calendar
There will be more than three options in the Calendar
Type field if a business calendar is available.
A business calendar can be used to model duration values for time-sensitive
aspects of your BPEL process in order to account for such variables
as regular working hours, weekends, and holidays. See Using business calendars within a BPEL process for more information.
5. For all other expression language choices, you will be
presented with the following two options:

Option
Description

Date
Choose this when you want the expiration to occur when a specific
time and date has been reached.

Duration
Choose this when you want expiration to occur after a certain
period of time has elapsed.
6. Depending on the expression language that you are using,
you can choose from any of the following expression types:

Option
Description

Visual
Choose this to use the visual snippet editor to graphically
compose Java code.

Java
Choose this to write a Java expression
yourself.

Literal
Choose this to enter the required values directly into customized
fields. Calendar values are represented in Coordinated Universal Time
(UTC).

Text
Choose this to compose an XPath expression.

## Related tasks

- Defining timer-driven behavior in a BPEL process
- Setting duration values for your human task
- Using business calendars within a BPEL process

## Related reference

- Expiration tab: BPEL process editor