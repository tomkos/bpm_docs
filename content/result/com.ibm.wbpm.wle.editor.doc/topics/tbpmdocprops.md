# Working with the IBM\_BPM\_Document\_Properties property

## About this task

Information about the document type IBM\_BPM\_Document and all of its available properties is found
in the topic "The IBM\_BPM\_Document document type."

Information about working with the document
property IBM\_BPM\_Document\_Properties is found in the following topics:

- Writing to the IBM\_BPM\_Document\_Properties property

Properties can be written into a document when it is created or updated. In both cases, you can optionally provide the operation with a list of ECMProperty objects.
- Reading from the IBM\_BPM\_Document\_Properties property

The get document operation returns an ECMDocument object. This object contains the properties that are associated with the document.
- Updating the IBM\_BPM\_Document\_Properties property

In an update scenario, only the properties that are passed into the check-in operation are updated in the document. BPM document properties are stored in the single CMIS property object IBM\_BPM\_Document\_Properties. When a value is passed to the property object, the existing value for the property is overwritten. Be careful to ensure that when updating the property, only the intended updates are sent to the server.
- Specifying search criteria for the IBM\_BPM\_Document\_Properties property

After the "Document List" Coach View is configured to work with BPM documents, it automatically generates the CMIS query to pass to the search service. The query includes any required search conditions from the BPM document options that are specified for the view. However, if you intend to write your own CMIS query, or configure the Content Integration node for a search operation, then you must manually specify the format of the search condition.