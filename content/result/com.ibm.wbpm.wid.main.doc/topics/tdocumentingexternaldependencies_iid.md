<!-- image -->

# Linking to external information in IBM Integration Designer

You can include a link to an external source
by pasting the link into the Description field of a business object.

When you work with a business object, you might need to provide
a link to related information that is outside of the IBM® Integration
Designer environment.
For example, you might want to link to a website or a wiki page. You
can also refer to a change request stored in a change management system
or a test case in a quality management system. These kinds of links
can be used to achieve traceability or provide details about the fixes
and features that went into a new process application snapshot.

## Adding a link

### Procedure

To add a link to an external source, complete the following
steps:

1. Log in to IBM Integration
Designer 
and then select a data (XSL) or interface (WSDL) file.
2. Select the artifact for which you want to add a link to
an external resource and click the Overview tab, or open the Properties editor.
3. Click the Documentation Edit link.
4 To add a link, click the Insert Link icon on the toolbar and complete the fields in theAdd Link window. When you access a specific content source, you might be prompted to log in to the source. Youmust log in with a user ID and password that provides access to that content source. The link sourcemust be registered as a remote content source with Process Center using the Create Registrationoption.Note: In Process Center, the attachment link type is available only when you create a newsnapshot, or edit an existing snapshot. When you create a new snapshot, you can create theattachment link either to an existing design file, or to a new file. When you edit an existingsnapshot, you can create the attachment link only to an existing design file. Also, when you createan attachment link to a new file:
    - The files that you add must be 100 MB or less.
    - The name of the file that you add must be less than 64 alphanumeric characters.
    - The accumulated total file size for a process application must be less than 600 megabytes.
5. Optional: You can specify the relationship type of the
link and the asset type that the link is associated to. The asset
types are determined by the type of content source that you are using
 in your project. When you select a link type, it can be modified
by any asset type that you select. For example, if you select Implements as the relationship type and Defect as the asset type, the description of the artifact is modified with
an option that defines the link as implementing a defect. The link
displays as a defect. The following table identifies the
default link and asset types.
Table 1. Link options

Type
Description

Link Type
 

Unspecified
No specific link type is specified

Affected by
Defines the link target as affected what is
defined by the selected asset type

Implements
Defines the link target as implementing what
is defined by the selected asset type

Related to
Defines the link target as associated to what
is defined by the selected asset type

Resolves
Defines the link target as resolving what is
defined by the selected asset type

Tested by
Defines the link target as tested by what is
defined by the selected asset type

Uses
Defines the link target as using what is defined
by the selected asset type

Asset Type
 

Unspecified
No specific asset type is specified

Change Request
Defines the asset type as a change request

Defect
Defines the asset type as a defect

Requirement
Defines the asset types a project requirement

Service
Defines the asset type as a service that can
be implemented

Test
Defines the asset type as a test

## Editing an existing link

### Procedure

To edit an existing link, complete the following steps:

1. Log in to IBM Integration
Designer and select a data (XSL) or interface (WSDL) file.
2. Select the artifact for which you want to edit a link to
an external resource and then click the Overview tab, or open the
Properties editor.
3. Click Edit in the Overview tab or the Properties editor.
4. Place the cursor on the link and click the link text.
You can now edit the link or the link name in the Edit Link window.