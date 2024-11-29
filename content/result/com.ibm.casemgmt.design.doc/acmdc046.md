# Include options for assets in FileNet Deployment
Manager

The include options for FileNet Deployment
Manager control
individual assets or objects. The include options that are specified
for an asset are propagated to any related objects that are added
to the export data set as a result of the include options settings
for the original asset. These include options cascade from one object
to the next as the export operation finds associated objects to add
to the export data set based on the specified include options.

When you use FileNet Deployment
Manager to
migrate assets for a solution application, specify include options
that narrowly target the assets to export. This narrow focus is intended
to avoid implicit inclusion of unwanted objects that can be caused
by propagation of the include options. In the Include Options window
in FileNet Deployment
Manager, click None to
clear all the include options that are selected. After you clear the
include options, only the asset that is listed in the export manifest
will be exported and placed into the deploy dataset.

- For associated metadata that was created in the source system
after an add-on was installed, install the same add-on into the target
object store instead of moving the metadata by using FileNet Deployment
Manager.
- To avoid the accidental inclusion of metadata that is created by the workflow deploy solution
process, explicitly include any custom metadata in the export manifest instead of implicitly
including the metadata by using the Data Design include options.

- For more control over the export, add the parent folder explicitly
to the export manifest instead of by using the Include
parent folders option.
- Do not select Include parent folders if you export assets in the case
instance folder hierarchy. The case folder and case instances must be created by the workflow deploy
solution process and workflow server at run time.

For document classes, exclude
any subscriptions and event actions that are associated with the document class definitions. Because
unique IDs are assigned to subscriptions and event actions on each system, duplicate items are
created if you include these items in the export.

Do not use the Data
Design include options for the class definitions themselves. This approach reduces
potential side-effects that can be caused by the export of property templates from add-ons, or by
the export of a case type class definition when an exported object refers to metadata that is
associated with the case type, such as a case property or case activity.

Typically, the
Include modified system classes option is not selected and should be used
with caution.

The General include options can typically
be left with their default values.

For more information about FileNet Deployment
Manager include
options, see the IBM®
FileNet P8 documentation.