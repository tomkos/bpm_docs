# Converting heritage services

## About this task

- Converting a service creates the equivalent service flow in the
Service Flow editor. This editor can add other services, events, and
gateways to your service flow. In other words, your original service
becomes the starting point for a more sophisticated service flow.
The Service Flow editor is only available in the Process Designer.
See Creating a service flow.
- Conversion is simple, as shown in the following steps.

- Conversion is one way. After a heritage service is converted,
you cannot undo the operation, so make sure you take a snapshot before
you convert the service.
- Through conversion, artifacts in the heritage service are replacedwith their equivalent in the Service Flow editor. For example, a scriptnode and an error end event in a general system service are convertedinto a script activity and an error end event in the resulting serviceflow.Important: After conversion, test the service flowto ensure that all artifacts are present, the logic is correct, andthe service flow works as expected. Depending on the complexity ofthe heritage service submitted for conversion and on the availablesupport, you can expect one of the following outcomes:
    - If the heritage service includes only artifacts that have a direct
equivalent in the Service Flow editor, the conversion completes successfully
and the service flow preserves the logic of the initial heritage service.
    - If there are artifacts for which there is no equivalent in the
Service Flow editor, the conversion replaces the unsupported artifacts
with placeholder Service Task activities. Edit the service flow in
the Process Designer as
needed to make sure it implements the logic of the initial service
correctly.
    - If the logic of the heritage service is not supported by the service
flow, unsupported artifacts might be lost during conversion. In some
rare cases, conversion might not occur.
- Conversion of a heritage service is done at the process application
or toolkit level. Artifacts in dependent toolkits are not converted
automatically. You must open the dependent toolkit and convert the
artifacts manually, or you can use the Toolkit Dependencies section
in the Service Conversion page. A dependent toolkit
with converted services can be easily added to your process application.
In the Toolkits library navigation, find the
toolkit and select the option to upgrade the dependency. Tip:  Services that are included in system toolkits have a dual nature, which allows
them to behave as both their traditional flow types (integration, general system, decision) and as
service flows. For example, you can open an integration service in the System Data toolkit either as
its traditional integration flow in the desktop Process Designer or as a service flow in the web Process Designer.

## Procedure

1. Open the process application or toolkit.
2. Open the Process App Settings or Toolkit
Settings editor.
3. In the Service Conversion tab, select
the services that you want to convert and click Convert. 
To ensure that a snapshot is created
before conversion, Create a snapshot before converting is
selected by default in the Convert Heritage Services dialog.
 You are reminded that editing your converted service flow is done in the Process Designer.Important: Only services that
can be converted are listed for selection. Some services that have been created in earlier products
such as Teamworks or WebSphere® Lombardi
Edition cannot be
converted into service flows, and  are therefore not displayed. In the desktop Process Designer, these services are listed in the
category User Interface under Services and they are
displayed with the icon of a general system service. If you have such a service, you can use the
desktop Process Designer to convert it to either a
heritage human service (if it contains coaches), otherwise convert it to a general system service.
Alternatively, you could consider rewriting your legacy services to take advantage of newer features
such as client-side human services and coach views using the BPM UI toolkit.
4. Click Finish.  A message
states the number of converted services, confirms that the pre-conversion
snapshot was created, and suggests you check your converted services
in the Service Flow editor.  If you see references
in toolkits, convert the references, as discussed in Converting deprecated functions.
5. After conversion, test the service flows, make all the
necessary edits in the Process Designer,
and re-test to ensure that the service flows work correctly.
6. Click Services in the library to
see your converted services.

## Results

Since a converted service is a service flow, all your former services regardless of type are
listed as service flows. Suppose that you converted a general system service that is called Tax
Bracket Rules and an Integration service called Corporate Tax Regulations. You would then have two
service flows: Tax Bracket Rules and Corporate Tax Regulations.

- Converting Business Process Definitions (BPDs) to processes: To
continue developing your BPDs with the  Process Designer,
which includes features that are not found in the desktop editor,
you must convert your BPDs. To convert your BPDs, see Converting BPDs to processes.
- Converting deprecated functions: The Process Designer extends
your processes to run on mobile devices such as tablets and cell phones.
Your older and deprecated functions must be converted to work with
these newer devices. To convert your deprecated functions, see Converting deprecated functions.

- Mapping heritage service artifacts to service flow artifacts

Learn about the artifacts that are created when you convert a heritage service that was built in the desktop Process Designer so that you can use it in the Process Designer.
- Converting integration services with web service integrations

In previous releases, web service integrations were created by using integration services in the desktop Process Designer. Convert these integration services and their web service integrations so that you can use them in the web-based Process Designer.
- Migrating heritage services that can be started by using a REST API

If you used the system-wide configuration property <startservice-valid-services> from previous releases, you might need to perform additional steps listed below to get your scenario running again.