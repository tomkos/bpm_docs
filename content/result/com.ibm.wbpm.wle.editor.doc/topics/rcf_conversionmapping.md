# Mapping deprecated functions to UI functions

The following sections show the mapping between the deprecated functions, sorted by toolkit, and
their corresponding functions after conversion. Functions that are not deprecated in Business Automation Workflow
24.0.0.0 do not require conversion and are not
included in the tables.

- Mapping deprecated functions in the Responsive Coaches toolkit
- Mapping deprecated functions in the Coaches toolkit
- Mapping deprecated functions in the Content Management toolkit

## Mapping deprecated functions in the Responsive Coaches toolkit

The following table shows the mapping of deprecated coach views in the Responsive Coaches toolkit
to UI views after conversion.

For more information about the UI views, see UI toolkit.

For more information about the deprecated coach views in the Responsive Coaches
toolkit, see Responsive Coaches toolkit.

| Deprecated function in the   Responsive Coaches toolkit   | Function in the  UI toolkit                                        |
|-----------------------------------------------------------|--------------------------------------------------------------------|
| Button                                                    | Button                                                             |
| Check Box                                                 | Check box or  Switch                                               |
| Date Time Picker                                          | Date/time picker                                                   |
| Decimal                                                   | Decimal                                                            |
| Image                                                     | Image                                                              |
| Integer                                                   | Integer                                                            |
| Multiple Select control                                   | Multi select                                                       |
| Output Text                                               | Display text                                                       |
| Radio Button                                              | Radio button group                                                 |
| Section                                                   | Horizontal layout,  Vertical layout,  Panel, or  Collapsible panel |
| Single Select control                                     | Single select                                                      |
| Table                                                     | Table                                                              |
| Tabs                                                      | Tab section                                                        |
| Text                                                      | Plain text or  Type ahead text or  Password                        |
| Text Area                                                 | Text area or  Rich text                                            |

## Mapping deprecated functions in the Coaches toolkit

The following table shows the mapping of deprecated coach views in the Coaches toolkit to UI
views after conversion.

For more information about the UI views, see UI toolkit.

For more information about the deprecated coach views in the Coaches toolkit, see Coaches toolkit.

| Deprecated function in the  Coaches toolkit   | Function in the   UI toolkit                     |
|-----------------------------------------------|--------------------------------------------------|
| Button control                                | Button                                           |
| Checkbox control                              | Check box or  Switch                             |
| Date Time Picker control                      | Date/time picker                                 |
| Decimal control                               | Decimal                                          |
| Horizontal Section control                    | Horizontal layout,  Panel, or  Collapsible panel |
| Image control                                 | Image                                            |
| Integer control                               | Integer                                          |
| Output Text control                           | Display text                                     |
| Radio Buttons control                         | Radio button group                               |
| Select control                                | Single select or  Multi select                   |
| Table control                                 | Table                                            |
| Tabs control                                  | Tab section                                      |
| Text control                                  | Plain text or  Type ahead text                   |
| Text Area control                             | Text area or  Rich text                          |
| Vertical Section control                      | Vertical layout,  Panel, or  Collapsible panel   |

## Mapping deprecated functions in the Content Management toolkit

The table below shows the mapping of deprecated coach views in the Content Management toolkit to
corresponding views in the same Content Management toolkit. The following restrictions exist:

- The conversion does not preserve all of the configuration options and data bindings of the
deprecated Content Management coach views. To ensure that the views work correctly after conversion,
you must review and set their configuration options and bindings again in the Process Designer.
- If converting to ECM Document List, you must set the ECM server configuration
name option based on the name that is used by the search service associated with the
legacy view. If a custom search service was used, the service interface must be updated and the
Search service option must be set to reference it.
- If converting to Document Explorer, any stand-alone File Viewer that was previously configured
will no longer work. The new Document Explorer has a built-in document viewer that can be enabled by
setting the Use document viewer configuration option. The stand-alone File
Viewer can be removed.

For more information about the views in the Content Management toolkit, see Content Management toolkit.

| Deprecated function in the  Content Management toolkit   | Function in the  Content Management toolkit   |
|----------------------------------------------------------|-----------------------------------------------|
| Responsive Document Explorer                             | Document Explorer                             |
| Responsive Document List                                 | BPM Document List or   ECM Document List      |
| Responsive Document Viewer                               | File Viewer                                   |
| Heritage Document Explorer control                       | Document Explorer                             |
| Heritage Document List control                           | BPM Document List or   ECM Document List      |
| Heritage Document Viewer control                         | File Viewer                                   |