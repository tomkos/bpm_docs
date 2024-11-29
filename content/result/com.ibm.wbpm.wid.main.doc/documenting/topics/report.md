<!-- image -->

# Generated reports for artifacts

In addition to viewing resources, you might want to document
the applications that you are building. IBM® Integration
Designer provides a tool to generate documentation for the artifacts in your
modules, mediation modules, and libraries.

Initiate the documentation generation by invoking a wizard.
You can customize the contents of the documentation by selecting multiple
resources from one or more modules and libraries so that all the information
will be written to a single report, which is a PDF file. You can also
specify the layout and fonts for the output. See "Generating documentation"
in the related tasks for detailed instructions on how to create documentation.

- Details of the generated documentation
- Referenced files
- Documentation structure
- Documentation layout and style
- Master files to save settings
- Register new fonts

## Details of the generated documentation

The documentation generator produces the following information
for these resources:

| Resource                   | Generated documentation                                                                                                                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assembly diagram           | Overview picture of the assembly diagram in the Editor view Components Properties of the assembly and its components List of the all the qualifiers in an assembly, where they are set, and their definitions |
| Library                    | List of all the resources in the library                                                                                                                                                                      |
| Module or mediation module | List of all the resources in the module                                                                                                                                                                       |
| Business object            | Overview picture of the business object in the Editor view Properties of the business object                                                                                                                  |
| Business object map        | Overview picture of the business object map in the Editor view Properties of the business object map Transformation objects and their properties Transforms and their properties                              |
| BPEL Process               | Overview picture of the process in the Editor view Properties of the process Partners and their properties   Activities and their properties                                                                  |
| Human task                 | Overview picture of the human task in the Editor view Properties of the human task, including email support                                                                                                   |
| Interface                  | Overview picture of the interface in the Editor view Properties of the interface                                                                                                                              |
| Java™ object               | Details from the .java file                                                                                                                                                                                   |
| Mediation flow             | Overview picture of participating interfaces and their connections Source interfaces and their properties References and their properties Mediation flows and their properties                                |
| Relationship               | Overview picture of the relationship in the Editor view Properties of the relationship                                                                                                                        |
| Business rule              | Overview picture of the business rule in the Editor view Properties of the business rule Rules and their properties                                                                                           |
| Rule group                 | Overview picture of the business rule group in the Editor view Properties of the business rule group Added interfaces and their properties Added partner references and their properties                      |
| Selector                   | Overview picture of the selector from the Editor view Properties of the Selector Added interfaces and their properties                                                                                        |

Other resources are not documented by the documentation
generator.

## Referenced files

The documentation
generator can also produce documentation for the selected resources and the resources that they reference. For example, in the Documentation
Generation wizard, you can select the business process and the Include referenced files option. As a result, the generated
PDF report will also have information for the resources (such as interfaces
invoked by its activities) that the process references.

## Documentation structure

The generated PDF report has the following structure:

- Title pageHas the report title, author name, and report date.
- Table of contentsLists the sections and page numbers in the
report.
- Resource documentation sectionsLists the properties of the
resources. Except for the module and library, all resources also have
pictures of the resources opened in the Editor view.
- Cross referenceLists for each documented resource, which resource
uses it (Providers list), and where it is used (Receiver list).
- Appendix: Documentation generation settingsLists the documentation
generation settings that were specified in the Documentation Generation
wizard and used for the PDF report.

## Documentation layout and style

The layout and the style of the generated PDF report can be customized
with the Documentation Generation Wizard.  If you change the layout
and style settings, they are saved for all subsequent documentation
generations, until they are changed again.

The following layout
settings can be modified:

Default
value: Letter

Default value: 7

- Plain text

Plain text

    - Used for the description and documentation of different artifacts.
The font family of plain text is also used for the title page, the
header, and the footer.
    - Default font family: Helvetica
    - Default font size: 10
    - Default font style: regular
- Chapter title

Chapter title

- Used for the numbered headings, the header of table of contents,
and the header of the appendix
- Default font family: Helvetica
- Default font size: 14
- Default font style: bold
- Source code text

Source code text

- Used for the documentation of source code such as Java
- Default font family: Courier
- Default font size: 10
- Default font style: regular
- Caption text

Caption text

- Used for the captions of images
- Default font family: Helvetica
- Default font size: 10
- Default font style: bold
- Definition text

Definition text

- Used for the documentation of key-value pairs
- Default font family: Helvetica
- Default font size: 10
- Default font style: regular
- Header text

Header text

- Used for the unnumbered headings
- Default font family: Helvetica
- Default font size: 11
- Default font style: bold
- Table of contents

Table of contents

- Used for the table of contents
- Default font family: Helvetica
- Default font size: 9
- Default font style: regular

## Master files to save settings

A master file is a resource profile defining the contents (not the
font styles) to be included in the generated documentation. When using
the Documentation Generation wizard, create a master file to save
your resource selections and the next time you use the wizard to update
the same report, just select the existing master file.

## Register new fonts

The documentation
generator provides three default fonts that can be used in the documentation.
These fonts are Helvetica, Courier, and Times with the font styles:
regular, italic, bold, and bold italic.

You can add a new font,
which is either a true type font file (.ttf) or true type collection
file (.ttc) by registering it. Font registration is done from the
Documentation Generation wizard. Once a font is registered, it can
be used for all reports until it is removed. Default fonts cannot
be removed. See "Generating documentation" under related tasks for
instructions on how to work with the Documentation Generation wizard.

- Generating reports

You can generate documentation reports for the artifacts in your modules, mediation modules, and libraries.
- Changing fonts

Default fonts are specified for you, but if you want to customize the appearance of your reports, you can change the fonts used for various text entities. If you want to change the fonts that are used in the generated documentation, launch the Documentation Generation wizard and click Next until you have the Layout Settings page.
- Capturing images

You can export artifacts from your workspace as images and save them in the file system.