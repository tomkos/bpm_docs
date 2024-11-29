<!-- image -->

# Generating reports

You can generate documentation reports for the artifacts
in your modules, mediation modules, and libraries.

## Procedure

To generate documentation, complete the
follow actions:

1. In the Business Integration view, select the project or
artifact that you want to document.
2. Click the Generate Documentation button  in the toolbar, or right-click an
artifact to select Generate Documentation in
the context menu. The Documentation Generation wizard
opens.
3. In the Documentation Generation wizard, specify Author name, Documentation title and a Location for the PDF file that will
be generated. The default file name is reportFile.pdf and the default location is in your workspace. In any of the fields
for this wizard, press F1 (Ctrl+F1 for Linux®) to get help for that field. Use the Tab key to move the focus to
the next field.
4 You can accept the defaults and click Finish to generate the documentation. However, if you want to select additionalresources to be included in the output or change the layout of thedocumentation, click Next . Note: If the Finish button is not enabled, you haveselected a resource that the documentation generator does not support.You must click Next to create a new masterfile. Then, later, you will be able to select a resource that thedocumentation generator does support. See "Documentation of resources"under related concepts for additional information about the documentationfunctions.
    1 In the Select Content page, you specify if you wantto further customize the content of the generated output. See "Documentation of resources" for additional information onmaster files. Click Next .
        - Select Generate documentation from the selected resource if you do not want to add or remove resources for the documentation
generation.
        - Select Generate documentation from an existing master
file and a master file to rerun a previously saved resource
profile.
        - Select Create a new master file to add
or remove resources for this documentation generation.
2. In the Documentation Resource Selection page, you can
add and remove resources for your documentation. Select a resource
and click > to add it to the Document
input resources table. You can also select items in the
table and click < to remove content from
the documentation to be generated. Select the Include referenced
files  check box to also generate information for artifacts
that are referenced by the selected resources. See "Documentation
of resources" under related concepts for additional information on
referenced files.  The Save As button saves the new master file so that you can regenerate the
same report using the master file. Click Next.
3. In the Layout Settings page, select the documentation
layout that you require and click Finish to
generate the documentation. Note: If you change the layout
and style settings, they are saved for all subsequent documentation
generations, until they are changed again. 
(To add new fonts
to use in the documentation, see the instructions below.)
5. Optional: If you are generating a long report, you can
click the Run in Background button on the status
window to clear it from your screen.
6. When the document generation is complete, a window will
prompt you to open the PDF report. Restriction: The PDF files that are generated
by this product cannot be searched. If the PDF is generated in a non-English
character set, it might not be possible to copy the content into other
software products.