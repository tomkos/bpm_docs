# Configuring the file size of uploaded content management documents

## About this task

For more information about the 100Custom.xml configuration
file, see Creating a 100Custom.xml configuration file.

## Procedure

To limit the file size of the uploaded content management
documents, complete the following steps.

1. Stop the server for Workflow Server or Workflow Center.
2. Locate and open the appropriate 100Custom.xml configuration
file in a text editor. See The 100Custom.xml file and configuration.
3. Edit the 100Custom.xml file as follows,
and update the specified file size in bytes as required. As an example, the following code snippet limits the file size of the uploads to 1 megabyte
(MB).<properties>
    <server>
        <document-attachment-max-file-size-upload merge="replace">1048576</document-attachment-max-file-size-upload>
    </server>
</properties>
4. Save your changes to the 100Custom.xml file.
5 Start the server for Workflow Server or Workflow Center . Alternatively, if you wanted to impose a system-wide restriction to prevent users from uploadingdocuments for any application, you could choose either one of the following options.
    - Exclude any document upload control widgets from coaches.
    - Restrict the ACTION\_ADD\_DOCUMENT,
ACTION\_UPDATE\_DOCUMENT, and ACTION\_DELETE\_DOCUMENT
properties by using the wsadmin commands. See Configuration properties for action policies.