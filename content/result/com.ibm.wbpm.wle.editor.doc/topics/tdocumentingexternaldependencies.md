# Linking to external information (deprecated)

Traditional: 
To include a
link to an external source, paste a link into the Description field of the process application or
toolkit, or the Documentation field of an artifact in IBM® Process
Designer.

When
you work with process applications or toolkits, you might need to
link to related information that is outside of the IBM Business Automation
Workflow environment.
For example, you might want to link to a website or a wiki page. You
can also reference a change request stored in a change management
system or a test case in a quality management system. These kinds
of links can be used to achieve traceability or provide details about
the fixes and features that went into a new process application snapshot.

## Adding a link

### Before you begin

### Procedure

To add a link to an external source, complete the following
steps:

1. Log in to Workflow Center or Process Designer and
select a process application or toolkit.
2 Do either of the following steps:
    1. In Workflow Center, click
 the Manage tab. The
    2. In Process Designer, select
the artifact in the process application or toolkit for which you want
to add a link to an external resource and click the Overview tab,
or open the Properties editor.
3 Do either of the following steps: In Workflow Center , theinline editor displays showing you a standard formatting toolbar.In Process Designer ,a rich text editor window opens that shows a standard formatting toolbar.

- In Workflow Center,
click inside the Description field.
- In Process Designer,
click the Documentation Edit link in the Common
Section of the Overview, or in the Properties editor.

In Workflow Center, the
inline editor displays showing you a standard formatting toolbar.
In Process Designer,
a rich text editor window opens that shows a standard formatting toolbar.

4 To add a link, click the Insert Link icon on the toolbarand complete the fields in the Add Link window. When you access a specific content source, you might be prompted to log in to the source. Youmust log in with a user ID and password that provides access to that content source. The link sourcemust be registered as a remote content source with Workflow Center using the Create Registration option.Note: InWorkflow Center , the attachment link type isavailable only when you create a new snapshot, or edit an existing snapshot. When you create a newsnapshot, you can create the attachment link either to an existing design file, or to a new file.When you edit an existing snapshot, you can create the attachment link only to an existing designfile. Also, when you create an attachment link to a new file:

- The files that you add must be 100 MB or less.
- The name of the file that you add must be less than 64 alphanumeric characters.
- The accumulated total file size for a process application must be less than 600 megabytes.
5. Optional: You can specify the relationship type of the
link and the asset type that the link is associated to. The asset
types are determined by the type of content source that you are using
 in your project. When you select a link type, it can be modified
by any asset type that you select. For example, if you select Implements as
the relationship type and Defect as the asset
type, the description of the artifact is modified with an option that
defines the link as implementing a defect. The link displays as a
defect. The following table identifies the default link
and asset types.
Table 1. Link options

Type
Description

Relationship Type
 

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

### Before you begin

### Procedure

To edit an existing link, complete the following steps:

1. Log in to Workflow Center or Process Designer and
select a process application or toolkit.
2 Do either of the following steps:
    - In Workflow Center,
click  the Manage tab.
    - In Process Designer,
select the artifact in the process application or toolkit for which
you want to add a link to an external resource and click the Overview
tab, or open the Properties editor.
3 Do either of the following steps: In Workflow Center , theinline editor displays showing you a standard formatting toolbar.In Process Designer ,a rich text editor window opens that shows a standard formatting toolbar.

- In Workflow Center,
click inside the Description field.
- In Process Designer,
click Edit in the Overview tab
or the Properties editor.

In Workflow Center, the
inline editor displays showing you a standard formatting toolbar.
In Process Designer,
a rich text editor window opens that shows a standard formatting toolbar.

4. Place the cursor on the link and click the link text.
The Edit Link window opens. You can
now edit the link or the link name.