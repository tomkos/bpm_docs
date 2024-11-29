# ECM File Properties

## Configuration properties

<!-- image -->

The
content management advanced configuration properties for the ECM File Properties view are shown in
the following table:

| Content management advanced property   | Description                                                                                                                                                                                                                                                              | Data type                  |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| ECM server configuration name          | The ECM server to be used.                                                                                                                                                                                                                                               | String                     |
| Default document type                  | The document type for the first use. The default document type is cmis:document.                                                                                                                                                                                         | String                     |
| Default document properties            | Select the variable to use for the default properties of the ECM document. When an ECM document is created, the document list contains the default values for the document properties. The values might be read-only or hidden from users when they create the document. | List of ECMDefaultProperty |

## Events

- On load: Activated when the view loads. For
example:me.getDocumentId()
- On error: Activated when an error is in the view. For
example:alert("There has been an error with the control")
- On document type changed: Activated when the document type changes. For
example:console.log("Document type is changed: "+docType)

Depending
on the specific event, you can use JavaScript logic to modify the effects of the view. You can find
more information about using events with views in User-defined events.

## Methods

For detailed information on the available methods for ECM File Properties, see the ECM File Properties JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.