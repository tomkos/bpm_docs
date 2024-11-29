# Unexpected viewer behavior in Case Client when you open
documents for which the MIME types are not configured

You can open a document for viewing on a page that contains the Viewer widget, such as the
Work Details page. You can then download the document, view the document in the
native application, or cancel the operation. However, because the document tab persists in the
viewer window, you cannot view the document again.

To resolve this problem, close the document tab. You can then view the document again.

To prevent this behavior, configure the Viewer widget to always open documents in a new
window.