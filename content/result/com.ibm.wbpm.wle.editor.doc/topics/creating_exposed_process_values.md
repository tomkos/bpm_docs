# Creating exposed process values (EPVs)

## About this task

- If Use New Values is set, the tw.epv API returns the
EPV that has an Effective On date that is in the past and is closest to the
current time.
- If Use New Values is unset, the tw.epv API uses the
time that the task instance started, which means that it finds the EPV that has an
Effective On date in the past and is closest to the time that the task
instance started.

- Check your settings to make sure the behavior is what you expect.
- Set a default value for your EPV.

## Procedure

To create an EPV:

1. Open the designer.
2. Expand Data and select Exposed Process
Value. The New Exposed Process Value window
opens.
3. In the Name field, type a name for the value and click
Finish. The EPV configuration view
opens.
4 Configure the EPV:
    1. In the Documentation field, enter a description of the EPV for
the developers.
    2. To allow users to send feedback about this EPV, type an email address in the
Feedback E-mail Contact field.

The Manage Exposed Process Values page in the Process Admin Console includes
a feedback link that uses this email address.
    3. In the External Description field, enter a description of the
EPV for the users. The description that you provide here is displayed in the Manage
Exposed Process Values page in the Process Admin Console.
5 Add one or several variables to the EPV by applying the following steps:

1. In the Exposed Process Value Variables section, click
+ to add a variable to this EPV.

For example, if you want to enable users to adjust the dollar amounts that correspond with
various levels of approvers for an expense reimbursement process, add a variable for each available
level.
2. In the Variable Details section, in the External
Name field, type the name of the variable for the users. This name
appears in the Variable List for this EPV in the Process Admin Console.
3. In the Variable Name field, type the name of the variable for
internal processing. 
Note: Variable names should start with a lowercase letter, with subsequent words capitalized like
so: myVar. Do not use spaces in variable names. Variable names are case
sensitive.
4. In the External Description field, type the text to describe
this variable to users. This description appears in the Variable List for this EPV
in the Process Admin Console.
5. Optional: In the Default Value text box, type a
valid default for this variable.
6. To enable in-progress tasks to use the updated value of this variable when users edits its
value, select the Use New Values check box.
7. To select a variable type, click Select... and select a
business object or click New to create a new custom business object (variable
type).

Note: You should exercise caution when using a non-string type for EPV variables. The use of
non-string types is not recommended and it can result in problems with JavaScript type conversion.
If you must use a non-string type for EPV variables, see the "Example" section below.
6. In the Exposing section, click Select to choose
the team whose members can manage this EPV and adjust its variable values.

By default, an EPV is not exposed to any team. You must expose an EPV by selecting a team in
order to edit the values of the EPV. The EPV can only be edited by the team that is selected in the
Process Admin Console. Administrators cannot edit the EPV. After the EPV is exposed to a specific
team, you can change the content of the team at runtime using the regular team modification methods.
For more information about EPVs, see the topic Managing exposed process values (EPVs).
7. Click Save or Finish Editing.

## Results

The EPV is created, you can link it to a process, service, or report.

You can refer to the name of the EPV and its variables like so:
tw.epv.[epv\_name].[epv\_variable\_name].

You can use the EPV in a decision gateway to control the flow of a process. You can also refer to
the EPV from any JavaScript code in a linked process, such as the code within a server script
service component.

## Example

To use an integer or decimal type for an EPV variable (rather than the recommended string type),
you should consider creating a corresponding local variable of the integer or decimal type. The
operation should be performed on the local variable instead, for example

```
tw.local.number = tw.epv.myepvs.number; tw.local.number = tw.local.number + 1;
```

Alternatively, to use EPV variables in JavaScript code, you need to use type cast, for
example

```
var mynumber = parseFloat(tw.epv.myepvs.number);
```

You can also use a complex variable by casting the EPV variable to the type you are using. For
example

```
// for a string use the following:
 tw.local.myString = String(tw.epv.kbexample.myString);
 // for an integer use:
 tw.local.myInt = Number(tw.epv.kbexample.myInt);
 //for a boolean use:
 tw.local.myBoolean = String(tw.epv.kbexample.myBoolean);
```

## What to do next

After you create an EPV, you can link it to a process or a service by selecting it from the list
of exposed process variables in the Variables tab.

- Adding an exposed process value to a report (deprecated)

When you create an exposed process value (EPV), you can link it in a report.