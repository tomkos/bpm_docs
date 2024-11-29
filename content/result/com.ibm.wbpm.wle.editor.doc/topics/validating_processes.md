# Validating process applications and toolkits (projects)

Client-side and server-side validation functions are provided to alert you to issues in your
projects. Validation provides feedback about several types of issues, such as:

- Broken references, such as missing implementations for activities
- Problems with parameter mappings
- Duplicate names and other naming violations
- Problems in scripts
- Critical errors, which are errors that prevent a project from installing or running. In the
Validation pane of the designer, a critical error is flagged with the following
prefix:[Critical]

Client-side JavaScript semantic validation is supported in the process editor, client-side human
service editor, and heritage human service editor. To enable or disable validation or to specify the
delay period before validation starts, you can use the Show JavaScript
warnings and Validation delay (ms) settings in the user
preferences. Information about setting user preferences is found in the topic Setting preferences in Process Designer.

Client-side and server-side validation both include JavaScript syntax
validation in script activities and variable initialization in service flows and processes. This
function validates JavaScript syntax when you modify JavaScript code. The function also
provides server-side validation of JavaScript syntax when you import process applications or
toolkits.

For server-side validation, JavaScript syntax validation verifies changes that occur only after
it is enabled. It doesn't work retroactively, meaning that existing snippets that are unchanged are
not parsed after the function is enabled. For example, if you change some JavaScript code or import
a project, JavaScript syntax validation checks only the changed scripts and imported projects but
not unchanged scripts or projects

Both client-side and server-side JavaScript syntax validation is enabled by default. However,
in case of performance issues, you might choose to disable validation. To disable client-side
validation, clear the Show JavaScript warnings check box in the user
preferences. For information about disabling server-side validation, see the topic Disabling server-side JavaScript syntax validation.

Client-side validation errors and warnings are displayed in the editors in the designer.

- At the snapshot level: In Workflow Center, in the
Process Apps or Toolkits tab, click the process
application or toolkit, and under a snapshot, expand the errors and warnings section.
Click the Open in Designer link to open the artifact with the error. For
more information see Where to edit Process Designer artifacts.
- At the artifact or project level: In the designer footer,
click Validation errors and warnings
.