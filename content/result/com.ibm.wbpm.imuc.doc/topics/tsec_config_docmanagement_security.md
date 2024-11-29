# Configuring document management security

The following MIME types are part of the allowlist by
default:

- <mime-type>text/plain</mime-type>
- <mime-type>text/calendar</mime-type>
- <mime-type>text/css</mime-type>
- <mime-type>text/csv</mime-type>
- <mime-type>text/rtf</mime-type>
- <mime-type>text/html</mime-type>
- <mime-type>text/xml</mime-type>
- <mime-type>img/png</mime-type>
- <mime-type>img/jpg</mime-type>
- <mime-type>img/jpeg</mime-type>
- <mime-type>img/gif</mime-type>
- <mime-type>application/xml</mime-type>
- <mime-type>application/xml-dtd</mime-type>
- <mime-type>application/pdf</mime-type>
- <mime-type>application/zip</mime-type>
- <mime-type>application/x-zip-compressed</mime-type>
- <mime-type>application/x-tar</mime-type>

If you are unable to upload a document because its MIME type is not in the default allowlist,
it can be added to the allowlist through the 100Custom.xml file. Java JDK
libraries determine the MIME type value of an uploaded document. For some document types such as
Microsoft documents or Open Office documents, the JDK libraries return the MIME type as null.
IBM Business Automation
Workflow handles
such document types internally and maps the appropriate MIME type to the corresponding document
extension through an internal list of file extensions.

More MIME types can be added to the
allowlist of MIME types, in the server-side configuration option
document-attachment-accepted-mime-types. When
<allow-null-mime-type> is set to true, files without extensions (file name only)
can be uploaded. Files where the <mime-type> value is determined to be null can
also be uploaded. Due to the implementation of the Java SDK, the MIME type is determined as null for
many file extensions. Therefore, if <allow-null-mime-type> is set to true, it is
possible to upload files of MIME types that are not part of the allowlist, which can cause
unexpected behavior.

- Malicious files such as viruses, are uploaded and shared among users.
- To display a document, a user might upload JavaScript files and run them in another user's
browser. Browsers attempt to render or even run files of specific MIME types automatically.

- document-attachment-accepted-mime-typesWith this configuration
parameter, you can specify an allowlist of MIME types that can be uploaded. MIME types that are not
included on the allowlist are blocked from being uploaded.

- document-attachment-download-mime-types With this configurationparameter, you can specify a blocklist of MIME type mappings. Each MIME type mapping allows for aconversion to be made from a specific MIME type to another during a download. The default<mime-type> values are:

With this configuration
parameter, you can specify a blocklist of MIME type mappings. Each MIME type mapping allows for a
conversion to be made from a specific MIME type to another during a download.

The default
<mime-type> values are:

    - <mime-type>text/plain</mime-type>
    - <mime-type>img/png</mime-type>
    - <mime-type>application/zip</mime-type>

```
<server merge="mergeChildren">       
  <!-- mime type allowed list which specifies mime types accepted for --> 
  <!-- upload to document list or document attachment --> 
  <document-attachment-accepted-mime-types merge="replace"> 
    <!-- specifies whether to allow a null mime type for upload --> 
    <allow-null-mime-type>false</allow-null-mime-type> 
    <!-- lists the mime types allowed for upload --> 
    <mime-type>text/plain</mime-type> 
    <mime-type>img/png</mime-type> 
    <mime-type>application/vnd.ms-excel</mime-type>
    <mime-type>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet</mime-type>
    <mime-type>application/vnd.ms-powerpoint</mime-type>
    <mime-type>application/vnd.openxmlformats-officedocument.presentationml.presentation</mime-type>
    <mime-type>application/msword</mime-type>
    <mime-type>application/vnd.openxmlformats-officedocument.wordprocessingml.document</mime-type> 
  </document-attachment-accepted-mime-types> 
    
  <!-- mime type blocked list which specifies mappings from unacceptable --> 
  <!-- mime types to acceptable mime types for download from --> 
  <!-- document list or document attachment --> 
  <document-attachment-download-mime-types merge="replace"> 
    <!-- will map text/html mime type to text/plain mime type --> 
    <mime-type-map> 
      <from>text/html</from> 
      <to>text/plain</to> 
    </mime-type-map> 
    <!-- missing <to> element implies mapping to content/octet-stream --> 
    <mime-type-map> 
      <from>application/pdf</from> 
      </mime-type-map> 
  </document-attachment-download-mime-types> 
</server>
```

- You can extend the settings by adding more mime-type.
- Providing a configuration in the 100Custom.xml file overrides the default
configuration. As a result, for text or html to remain on the blocklist, you must add it explicitly
to the 100Custom.xml file.

## Restricting file uploads and downloads

To specify server-side configuration options in the 100Custom.xml file to
restrict file uploads and downloads by MIME type in a document list coach view.

1 Determine your document attachment's security requirements by evaluating any additional wantedrestrictions on MIME types for upload or download.
    - For example, you might want to rewrite several MIME types, such as those used for PDF files, to
application/octet-stream.
2 Add the default configuration in the example to your 100Custom.xml file,and augment this configuration with your additional settings.

- Refer to The 99Local.xml and 100Custom.xml
configuration files.
3. Restart your environment and test.

## Disabling document upload security

To disable the security of document upload by MIME type, configure the
<disable-document-attachment-accepted-mime-types> parameter in the
100Custom.xml file:

```
<server merge="mergeChildren"> 
<document-attachment-accepted-mime-types merge="replace"> 
<disable-document-attachment-accepted-mime-types>true</disable-document-attachment-accepted-mime-types> 
</document-attachment-accepted-mime-types> 
</server>
```