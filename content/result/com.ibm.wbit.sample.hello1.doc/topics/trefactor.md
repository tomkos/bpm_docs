<!-- image -->

# Copy the web service file

## About this task

To copy the web service file into the library:

## Procedure

1. In the Business Integration view, expand the HelloService project,
and then the Web Service Ports category.
2. Right-click HelloService\_HelloServiceHttpPort  and
select Show Files. This action opens the Physical
Resources view. This view shows the underlying files in your projects. 
For more information about the content and structure of projects
in both the Project Resources view and the Business Integration view,
see Business integration projects and the topics linked
from there.
3. Return to the Business Integration view. Right-click the
file HelloService\_HelloServiceHttpPort and
select Copy. When the Multiple Artifact Copy
window opens, click OK. This action places
the WSDL file in the clipboard.
4. Right-click HelloWorldLibrary and
select Paste. This copies the WSDL file into
your library project.
5. Collapse the HelloService project
because you do not need to see it anymore, and expand the HelloWorldLibrary project.
Then expand its Interfaces and Web
Service Ports categories to see what has been copied in
from that WSDL file, as shown here:     Note: When
you have your own existing web service, you can similarly copy it
to a library or module project by using the clipboard or by dragging
and dropping it from the Windows file system, or by using File
> Import > Business Integration > WSDL and XSD. The latter
option is suggested for more complicated WSDL files that include references
to other files.
Note: You might be wondering what the annotation
is on the upper right of the icons for the interface and port. This
annotation indicates that the interface and port are part of a WSDL
file that contains multiple objects that can be extracted by right-clicking
and selecting Refactor or Analyze Impact > Extract WSDL
Components. However, you do not need to perform that task
in this sample.