# Working with BPM documents

## About this task

The following topics provide additional information about working with BPM documents:

- The BPM document store

The BPM document store is a CMIS-enabled embedded document repository that is used to store documents locally. The BPM document store supports most Content Management Interoperability Services (CMIS) operations and a number of inbound events and you can use either coaches or heritage coaches to work with documents in the BPM document store.
- Inbound events for the BPM document store

The BPM document store supports a subset of the inbound content event types that are supported by external ECM systems. Event subscriptions for the BPM document store can only be created using the IBM\_BPM\_Document type.
- Inbound events for the BPM content store (deprecated)

The BPM content store supports a subset of the inbound content event types that are supported by external Enterprise Content Manager systems. Event subscriptions for the BPM content store can be created only by using the IBM\_BPM\_Document type.
- The IBM\_BPM\_Document document type

In the BPM content store, BPM documents are represented by instances of the predefined document type IBM\_BPM\_Document.
- Creating BPM documents

You can create BPM documents by using one of the BPM documents Coach views and by using content integration in a service.
- Updating BPM documents

You can update BPM documents by using one of the BPM documents Coach views and by using the Content Integration node in a service.
- Working with the IBM\_BPM\_Document\_Properties property

Working with documents through the Content Integration node usually requires the manipulation of document properties.
- Working with BPM documents in the BPM Document List coach view

The BPM Document List coach view works with BPM documents. The BPM Document List builds a CMIS default query, but the query can be modified by specifying additional configuration options.
- Limitations in working with BPM documents

There are some limitations in working with BPM documents. In most situations, you can successfully work around these limitations.