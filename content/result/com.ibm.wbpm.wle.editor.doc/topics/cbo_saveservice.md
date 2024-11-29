# Save services for shared business objects

- Validate updated data on the client. The validation can return a validation object.
- Perform calculations that are based on the data that was entered.
- Apply an alternative merge result. If another version of the shared business object is saved
while the save service is running, the merge result is computed again, and then the save service is
started again.

- Service variables
- Save service examples
- Error handling
- Error handling examples

## Service variables

| Variable                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| object (shared business object type)               | The value of the shared business object that is to be saved. You can add logic to the save service to manipulate the value of the variable during the save operation, for example to calculate totals that are based on the updated data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| baseVersion (shared business object type)          | The value of the shared business object before it was changed. This value is null when the first version of the shared business object is saved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| latestVersion (shared business object type)        | The latest value of the shared business object that is saved to the database. If this value is different from the value of the baseVersion variable, the changes were applied to an older version of the shared business object and the system merged its changes with the latest version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| changes (BPMBOPropertyChange business object type) | A list that contains the individual changes that were made to the value of the shared business object. Each item in the list has the following properties: property (String) The changed variable. The format indicates which variable in the shared business object was changed. propertyName: The propertyName variable was changed. boPropertyName.propertyName: The boPropertyName complex type variable of a type that contains a propertyName variable that was changed. listPropertyName[n]: The listPropertyName list variable has a list item that was changed. The number, n, indicates the changed list item. sboPropertyName.@metadata.key: The sboPropertyName complex type variable that references a shared business object type where the value was changed listPropertyName.listLength(): The listPropertyName list variable where the length of the list was changed   oldValue (Any) The previous value of the variable. newValue (Any) The new value of the variable. |

| Variable                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| validationErrors (BPMBOValidationError business object type) | The list of validation errors. If the service    or service flow does not complete the variable or an empty list is returned, the shared business object is considered to be valid and it is saved to the database. However, in certain circumstances, the shared business object might not be valid despite an error not being returned. For more information, see Error handling.If a list of errors is returned, the shared business object is invalid and an error is raised. Each item in the list has the following properties: property (String) The name of the variable that is invalid. Use the same format that is used for the BPMBOPropertyChange business object. errorCode (String) A code that you can use to handle the error programmatically in a BPD or a service. errorText (String) Message text that can be displayed to users if the error occurs at runtime. You can also provide translated versions of the error message. |

## Save service examples

- givenName (String): the customer's given name
- surname (String): the customer's surname
- address (Address): the customer's address
- dateOfBirth (Date): the customer's date of
birth
- status (String): the status of the customer,
for example new, gold, or platinum
- creditScore (Decimal): the customer's credit
score

```
for(var i = 0; i < tw.local.changes.listLength; i ++) {
    var change = tw.local.changes[i];
    if(change.property == "dateOfBirth" && change.oldValue != null) {
        if(tw.local.validationErrors == null) {
            tw.local.validationErrors = new tw.object.listOf.BPMBOValidationError();
        }

        var validationError = new tw.object.BPMBOValidationError();
        validationError.property = change.property;
        validationError.errorText = "The date of birth must not be changed.";
        tw.local.validationErrors[tw.local.validationErrors.listLength] = validationError;
    }
}
```

```
// check if current user is team lead
var teamLeadTeam = tw.system.org.findTeamByName("Team Lead");
var isTeamLead = tw.system.user.isInTeam(teamLeadTeam);

if(!isTeamLead) {
    for(var i = 0; i < tw.local.changes.listLength; i ++) {
        var change = tw.local.changes[i];
        if(change.property == "status" && (change.oldValue != null || change.newValue != "new")) {
            if(tw.local.validationErrors == null) {
                tw.local.validationErrors = new tw.object.listOf.BPMBOValidationError();
            }

            var validationError = new tw.object.BPMBOValidationError();
            validationError.property = change.property;
            validationError.errorText = "The status must only be changed by a team lead.";
            tw.local.validationErrors[tw.local.validationErrors.listLength] = validationError;
        }
    }
}
```

The following
example server script checks whether the baseVersion and latestVersion values
are different. If they differ, updates are merged. The script then
retrieves the different status values from the different versions
of the shared business object. The value of the status variable
is checked to determine whether the value was changed in both versions
and whether the latest status is “platinum”. If so, the
platinum status is enforced to prevent downgrading a customer from
that level.

```
// check if a merge happened because an outdated version was updated
if(tw.local.baseVersion != tw.local.latestVersion) {
    var baseStatus = tw.local.baseVersion.status;
    var latestStatus = tw.local.latestVersion.status;
    var newStatus = tw.local.object.status;

    // check if the status was updated and merged
    if(newStatus != baseStatus && baseStatus != latestStatus) {
        // Make sure a downgrade from platinum does not happen
        if(latestStatus == "platinum") {
            tw.local.object.status = "platinum";
        }
    }
}
```

## Error handling

- For processes, add error intermediate events to the activity or define an error event
subprocess. For more information, see Handling errors in processes.
- For client-side human services, add an error event handler to the service. For more information,
see Handling errors in client-side human services.
- For services other than client-side human services   and service
flows, add an error boundary event to the step where you want to catch the error. For more
information, see Handling errors in services
and Catching errors by using error boundary events.

If the error is not caught on the activity or
the step, it is propagated to the parent instance. If the error is
not caught at all, all the updates are discarded and the instance
is marked as Failed.

Shared business objects that have validation
errors are excluded from automatic synchronization until another change
is made and the user saves the shared business object or it is saved
automatically.

## Error handling examples

```
tw.system.coachValidation.populateFromBPMBOSaveFailedError(tw.local.sharedBOSaveError);
```

<!-- image -->

1. First, the coach validation is done by the script Validate before save. The
script ensures that valid data is passed into the service flow.
2. When Validate before save returns a validation error, the execution goes
directly back to the coach and no save service is invoked.
3. When a user enters data that does not cause any coach validation errors, the run time tries to
save all the data from the user. If the user data includes shared business objects and the
Automatically sync shared business objects option is enabled on the heritage
human service definition, the shared business objects are also saved. Save services are also run as
part of the save. If a save service returns validation errors, the run time throws a
BPMBOSaveFailedError.
4. The BPMBOSaveFailedError is caught as a boundary event on the coach and the
error data is mapped into a local variable sharedBOSaveError.
5. The Populate coach validation errors script in the error path invokes a
system function to transform all validation errors from the BPMBOSaveFailedError
into the coach validation:
tw.system.populateCoachValidationFromBPMBOSaveFailedError(tw.system.coachValidation, tw.local.sharedBOSaveError);
6. The stay-on-page event causes the run time to give control back to the coach, and the user sees
errors.