<!-- image -->

# Perspectives and views for team development in Integration Designer

- Business Integration
- Resource
- Team Synchronizing
- CVS Repository Exploring (the name changes
depending on the SCM system being used)

## Business Integration perspective

The Business
Integration perspective is the central work area for Integration Designer, where
you can do artifact design, development, and component integration.
You can also do most team development activities, such as check out,
commit, and update, in this perspective.

As part of the Business
Integration perspective, the Physical Resources view lists the relevant
artifacts and resources for modules and libraries. The Physical Resources
view is similar to the Project Explorer view under the Resource perspective,
except that only Service Component Architecture (SCA) modules are
shown; staging modules are not shown.

The Business Integration
view includes a Show Files option that displays all authored files
for an artifact. For example, a Business Process Execution Language
(BPEL) process saves its process flow logic in a .bpel file, but there
are other backing files-.bpelex and Artifacts.wsdl-that
are needed for the BPEL process to build properly. Right-click any
artifact and select Show Files to open the
view. The Show Files option highlights all the backing files in the
Physical Resources view.

## Physical Resources view

The Physical Resources
view shows all of the file-level resources from the modules and libraries
in their natural form. Related projects that are generated when you
create business integration applications are still hidden in this
view.

The logical contents of the physical file are also displayed
in this view. For example, if you have several business objects in
an XSD file, you will be able to expand the XSD file in this view
and see all the business objects in the file.

If you have an
artifact open in an editor, you can click the opened artifact in the
editor pane (to focus on it) and then click the Link with
Editor button to quickly locate the file in the Business
Integration view.

You can apply filters to exclude all but
the objects that you want from the Physical Resources view. By default,
filters are enabled for XSD files to make it easier to find data types.
You can also apply filters to WSDL files by enabling that function
in Preferences and you can apply a filter to hide secondary artifacts.

The
.settings folder also appears in this view. The .settings folder contains
properties that are used by Integration Designer and should
be shared with each project. For that reason, the .settings folder
should be added to team repositories. See the related links for more
information about the .settings folder.

## Resource perspective

In the Project Explorer
view, which is listed under the Resource perspective, you can see
every module and artifact in the workspace, including all staging
modules.

## Team Synchronizing perspective

In the Synchronize
view within the Team Synchronizing perspective, you can synchronize
the workspace with the remote repository. It displays any relevant
outgoing or incoming changes and can identify merge conflicts.

## CVS Repository Exploring perspective

The
CVS Repository Exploring perspective lists all modules or projects
that are currently managed in CVS. If your project uses a different
SCM provider, then a similar perspective may exist.