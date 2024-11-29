# Working with document content

- Check in document
- Create document
- Get document content
- Set document content

Information about these operations is found in the topic Data mapping in Enterprise Content Management operations.

The properties for the ECMContentStream
data type are described in the following table:

| Property name   | Description                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| contentLength   | The length of the original (non-encoded) content length in bytes. If the property is set, the length must be a positive number. If the length is unknown, the property must not be set.                |
| mimeType        | The MIME media type of the content stream. For the primary content of a document, the MIME media type should match the value of the property cmis:contentStreamMimeType. For example, application/pdf. |
| fileName        | The file name of the content stream. For the primary content of a document, the file name should match the value of the property cmis:contentStreamFileName.                                           |
| content         | The value of the document. It must be of type String Base64 and encoded in UTF-8.                                                                                                                      |

The samples would work only on traditional IBM Business Automation Workflow systems and not on
containerized Workflow systems. See the deprecated feature link: https://www.ibm.com/docs/baw/22.x?topic=examples-calling-java-through-javascript-deprecated

```
// Script sample code to set and encode the document content
var value = "abc";
var bytesValue = new Packages.java.lang.String(value).getBytes("UTF-8");
tw.local.contentStream = new tw.object.ECMContentStream();
tw.local.contentStream.contentLength = bytesValue.length;
tw.local.contentStream.mimeType = "text/plain";
tw.local.contentStream.content = Packages.javax.xml.bind.DatatypeConverter.printBase64Binary(bytesValue);
```

```
// Script sample code to get and decode the document content
var bytesValue = Packages.javax.xml.bind.DatatypeConverter.parseBase64Binary(tw.local.contentStream.content);
var value = new Packages.java.lang.String(bytesValue, "UTF-8");
```

```
// Script sample code to set and encode the document content from a file
var file = new Packages.java.io.File(tw.local.fileName);
var bytesValue = Packages.org.apache.commons.io.FileUtils.readFileToByteArray(file);

tw.local.contentStream = new tw.object.ECMContentStream();
tw.local.contentStream.contentLength = file.length();
tw.local.contentStream.fileName = file.getName();
tw.local.contentStream.mimeType = "text/plain"; // provide your designated mime type here
tw.local.contentStream.content = Packages.javax.xml.bind.DatatypeConverter.printBase64Binary(bytesValue);
```

```
// Script sample code to decode the document content and write it to a file
var bytesValue = Packages.javax.xml.bind.DatatypeConverter.parseBase64Binary(tw.local.contentStream.content);
var file = new Packages.java.io.File(tw.local.outputDirectory, tw.local.contentStream.fileName);
Packages.org.apache.commons.io.FileUtils.writeByteArrayToFile(file, bytesValue);
```