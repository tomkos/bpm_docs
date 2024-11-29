# Updating BPM documents

## About this task

- One of the BPM documents Coach views: Document
List view (if it has been enabled to allow document creation) or the
Documents view. For more information, see Configuring views for storing and viewing Enterprise Content Management documents.
- The Content Integration node that is available in the human service,
Ajax service, and integration service editors. For more information,
see Building a service that integrates with an ECM system or a BPM store.

To use the Content Integration node to update documents, you
must first check out the document. When the content or properties
data is ready to be updated, the document must be checked in. Properties
of a BPM document can be updated only through a check-in operation.
The Update document properties operation, available
for external Enterprise Content Management (ECM) servers, is not available
for the BPM document store.

In
a service flow, a typical update procedure might involve the following
tasks:

## Procedure

1 In the Content Integration node,specify the following options:
    - Server: BPM document
store
    - Operation: Check-out
document.
2. In the Server Script node, populate
the implementation with the code that is required to update the content
or properties.
3 In the Content Integration node,specify the following options:

- Server: BPM document
store
- Operation: Check-in document.
The document ID (private working copy ID) that is returned by the
check-out document operation must be used as input to the check-in
document operation.

## What to do next

For sample code and information about working with BPM
document properties, see Working with the IBM\_BPM\_Document\_Properties property. For
sample code and information on working with content streams, see The IBM\_BPM\_Document document type.