# Inserting logic to transform or validate event data

## Procedure

To insert logic into event communication on a page:

1. In Case Builder,
add the Script Adapter widget to the page.
2. Add a wire to the Script Adapter widget from the source
widget that will publish the event whose payload is to be transformed
or validated.
3. Add a wire from the Script Adapter widget to the target
widget that is to receive the transformed or validated payload.
4. Click the Display menu icon for the Script Adapter widget
and then click Edit Settings.
5. In the JavaScript field, type the
code that you want to use to transform or validate the event data.
End the script with a Return statement.

The script you
enter is limited to basic JavaScript and should be viewed as the body
of one single function. You cannot use Dojo commands such as console.debug();
you must use the alert() statement to display information about the
values in the script.
Tip: You can use the Script Adapter
widget to debug your code while you are developing the script. When
it is acting as a debugger, the Script Adapter displays the source
event payload so that you can see the data that the script needs to
transform.
6. Optional: 
Hide the Script Adapter widget so
that it is not visible to the user.
7. Click OK.

## Example

1. Open the Cases page for the solution in Page
Designer.
2. Drag the Script Adapter widget onto the Cases page.
3 From the Case Search widget menu, select Edit Wiring towire the Case Search widget to the Script Adapter widget..
    1. In the Script Adapter Incoming Events section,
select Case Search from the Source
widget list.
    2. Select Search cases from the Outgoing
event list.
    3. Select Receive event payload from the Incoming
event list.
    4. Click Add Wire and then click OK.
4. From the Script Adapter widget menu, select Edit Settings and
then enter the following script in the JavaScript field:payload.CaseType=\"Homeowner Policy\"; 
alert(\"Updated Case Type to - \" + payload.CaseType); 
return payload;This script updates the CaseType property
in the payload from the Case Search event.
5. Save the settings and then save and close the page.
6. Deploy the solution.

In Case Client,
a search will return only cases of the Homeowner Policy case type.