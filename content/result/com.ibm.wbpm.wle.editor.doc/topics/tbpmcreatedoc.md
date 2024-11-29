# Creating BPM documents

## About this task

You can use the following user interfaces to create BPM
documents:

- One of the BPM documents Coach views: Document
List view (if it has been enabled to allow document creation) or the
Documents view. For more information, see Configuring views for storing and viewing Enterprise Content Management documents.
- The Content Integration node that is available in the human service,
Ajax service, and integration service editors. For more information,
see Building a service that integrates with an ECM system or a BPM store.

If you use the Content Integration node to create a document,
you select the BPM document store as the
target server and select the Create document operation.
The only required value for this operation is the document name. The
object type ID and folder ID are automatically specified because they
are mandatory properties when the BPM document store is specified
as the target server.

Optionally, you can also provide content
and properties:

- To provide content, you can use an ECMContentStream variable.
For an example of how to create a content stream, see Working with document content.
- To provide properties, you can use a list of ECMProperty objects.
All properties are optional and will default to a specific value if
not specified. For more information about default values, see The IBM\_BPM\_Document document type. For information about constructing an
ECMProperty list, see Working with the IBM\_BPM\_Document\_Properties property.

## What to do next