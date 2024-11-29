<!-- image -->

# Retrieving a Cognos report

Invoking a get function to retrieve a Cognos report could
fail due to a time out condition at run time. Therefore look at the
session value, which is enumerated so you can evaluate the valid values,
to determine if you should try invoking again in a while loop construct.
The session needs to be mapped from the response to the request of
the next invocation.

<!-- image -->

The Java code
snippet in the while loop is as follows:

```
if (GetCognosReportResponse != null) {
	if (GetCognosReportResponse.getDataObject("session") != null) {
		return !GetCognosReportResponse.getDataObject("session").getString("status").equals("complete");
	}
}

return true;
```

Mapping the response to the request
is shown in the ResetSession assign activity as follows:

<!-- image -->

Add
the cleanHeader method at the end of your process,
as discussed earlier in the sections on the handlers, as it frees
up thread storage and allows a thread to be reused. Select a Java
snippet activity from the palette and add it to the end of the business
process. Select the Properties view for the
Java snippet and then the Details tab. Add
the code to the pane provided.

<!-- image -->