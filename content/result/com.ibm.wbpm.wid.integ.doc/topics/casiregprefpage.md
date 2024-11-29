<!-- image -->

# Application Specific Information (ASI) registry preferences
page

When working with a resource adapter we need to capture the information
required by the adapter to marshal the Enterprise Information Systems
(EIS)-neutral data objects to the native objects used to interact
with the EIS. The information that describes the data conversions
is stored in XML schema files in the form of annotations. The XML
schema provides an appInfo tag for providers to describe application-specific
information. This schema is called the ASI schema.  Application Specific
Information (ASI) is metadata related to data wire formatting and
schema editing that is encapsulated as annotations within a schema.
This information describes a request message to an EIS or a response
message from an EIS.  In general, ASI schemas are provided by a resource
adapter.

The Application Specific Schemas Registry (ASI registry) component
provides a global point of access to the repository of XML Schema
documents (ASI Schemas) that specify application-specific information
used by an application to map a business object into its corresponding
enterprise entity. Ultimately, all XML schemas are stored into an
XML catalog component. Therefore, one of the main functions of the
ASI registry is to create XML catalog entries for ASI Schemas. These
entries are then used by an XML processor when resolving entity references.

To see the available ASI registry entries, from the menu select Window >
Preferences. In the Preferences window,
expand Business Integration and click Application
Specific Schemas Registry.

The preference page is divided into a Registry Entries view
where all registry entries are shown and a Details view
where properties of a selected entry are shown. You can add a new
entry to the User specified entries section using the Add button
or edit an existing user specified entry buy using the Edit button.
You can also remove a user-specified entry using the Delete button.
The Plug-in specified entries and Adapter-specified entries are
treated as system entries and cannot be changed.

- Display name - Contains a short name that identifies the ASI schema
that will be displayed by the IBM Integration
Designer tools.
- Description - Provides the detailed description of the ASI schema.
- XSD file location -URL that specifies the ASI schema unique location.
- Namespace URI - Identifies the namespace of the ASI schema.

You can browse for the ASI schema location in either the workspace
or the file system using the button next to the XSD file location
field. The namespace URI field will be completed automatically after
the ASI schema is specified.