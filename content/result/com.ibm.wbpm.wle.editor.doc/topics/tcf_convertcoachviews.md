# Converting deprecated coach views into UI views

## Before you begin

<!-- image -->

To convert the
deprecated coach views into UI views, you must add a dependency on the System Data 24.0.0.0 toolkit or a toolkit
or process application that has a theme. The UI views require theme definitions. The
Carbon theme in the System Data toolkit provides these theme definitions and it
is the default theme for new process applications.

## About this task

Start the conversion process at the application or toolkit level. During the conversion, you
replace all the deprecated coach views with UI views. Deprecated coach
views from the Content Management toolkit are converted into corresponding views from the same
Content Management toolkit. For the mapping between the deprecated functions to their
equivalent UI functions after conversion, see Mapping deprecated functions to UI functions.

For more information about the conversion and how
it works, see Converting deprecated functions.

## Procedure

To convert the deprecated coach views in the selected artifacts into UI views, complete
the following steps:Important:  Complete the following procedure in the Process Designer.

1. Open the appropriate process application or toolkit in
the Designer view.
2. In the Toolkits view, check whether the process application or toolkit
depends on the deprecated Coaches or Responsive Coaches toolkits.
If a dependency on a deprecated toolkit exists, the Conversion UI tab
becomes available in the Process App Settings page. The Conversion
UI tab is always available if there is a dependency on the Content Management
toolkit.
3. Switch to Conversion UI.
4. Optional: 
If you're using an earlier version of the System Data toolkit, upgrade to the latest toolkit
version to be able to access the theme definitions that are required by the UI views.
5 Under Toolkit Dependencies , openthe first toolkit dependency and complete the following steps:
    1. If the toolkit has more dependencies, drill through
its hierarchy of dependencies to the last toolkit that does not have
non-system toolkit dependencies and start the conversion from there.
    2. Check whether a converted version of a dependency toolkit
exists.  If a converted version of the dependency exists,
skip the substeps c - g and update the version of your toolkit to
the converted version. If a converted version does not exist, complete
the following substeps.
    3. Under Artifacts Using Deprecated Coach Views, select all the artifacts
that have deprecated coach views to be converted into UI views, and click
Convert.
    4. When the conversion is complete, test the results in the artifacts and make adjustments where
necessary.
For example, you can test whether each artifact runs successfully and its layout is correct,
update the custom JavaScript and CSS, or customize the UI views as needed. Retest the artifacts to
ensure that they work as you expected.
    5. Optional: Click Refresh () to make sure that
there are no artifacts or dependencies left to convert for this toolkit.
    6. Take a snapshot of the toolkit.
    7. Move up one level and change the toolkit version to
the snapshot version. Updating the version removes the
dependency from the list of dependencies for its parent.
6. Repeat step 5 with all its substeps for all the toolkit dependencies in the hierarchy, one
dependency at a time, until both the artifacts and toolkit dependencies lists for each toolkit are
empty.
7. In the Conversion UI tab for your application, select all the artifacts
whose deprecated coach views you want to convert, and convert them into UI views.
The list can include artifacts such as views that have dependencies on other deprecated coach
views, heritage human services, and client-side human services earlier than 24.0.0.0.
8. After the conversion completes, review the artifacts that contain converted views to verify the
results of the conversion.
You can also make adjustments where necessary (see step 5d).
9. Optional: Click Refresh to make sure that the list of artifacts contains no more dependencies.
All the artifacts in the process application or toolkit are
now mobile-ready and suitable for use on multiple device types.
10. (For the Coaches toolkit only) From the library, under Toolkits, remove the dependency on the Coaches toolkit. 
The dependency on the Content Management toolkit is automatically
upgraded.