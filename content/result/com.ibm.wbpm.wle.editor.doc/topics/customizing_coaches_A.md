# How heritage coaches work (deprecated)

The runtime rendering of a heritage coach involves the following key technologies:

| Technology   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XML          | The design of a heritage coach is described in Extensible Markup Language (XML). As you drag sections and controls to a heritage coach, IBM® BPM automatically generates the XML definition of the heritage coach. You can view the XML while you're building a heritage coach by clicking the Code View icon in the toolbar.                                                                                                                      |
| XSLT         | The Extensible Stylesheet Language Transformation (XSLT) transforms the XML definition to the runtime HTML form. The XLS renders a server-side-scriptlet that is run to generate the HTML.                                                                                                                                                                                                                                                         |
| HTML         | The client (web browser) renders the HTML that the heritage coach generates from its XML definition through XSLT processing.                                                                                                                                                                                                                                                                                                                       |
| CSS          | The Cascading Style Sheet (coach\_designer.css in the following image) instructs the client how to render the HTML output.                                                                                                                                                                                                                                                                                                                          |
| JavaScript   | JavaScript provides the methods and functions that implement runtime heritage coach features, such as dynamically adding rows to a table or governing the visibility of heritage coach controls. JavaScript that is embedded in the XML definition of a heritage coach is evaluated by the runtime engine before it is rendered to HTML by the web browser client. Both client-side and server-side JavaScript is used to render heritage coaches. |

<!-- image -->

If you have the required technical expertise, you can use the following methods to customize
heritage coaches:

- Override and customize Cascading Style Sheets (CSS)
- Edit the XML definition
- Edit the JavaScript files
- Edit the XSL transformation rules

The following topics describe some of the customization options most commonly used for heritage
coaches.