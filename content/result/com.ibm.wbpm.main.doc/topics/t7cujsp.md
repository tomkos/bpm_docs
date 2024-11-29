<!-- image -->

# Developing JSP pages for task and process messages

## About this task

To include user-defined JavaServer Pages (JSP) pages in
the web client, you must specify them when you model a human task
in IBM® Integration
Designer.
For example, you can provide JSP pages for a specific task and its
input and output messages, and for a specific user role or all user
roles. At run time, the user-defined JSP pages are included in the
user interface to display output data and collect input data.

The
customized forms are not self-contained web pages; they are HTML fragments
that Business Process Choreographer Explorer imbeds in an HTML form,
for example, fragments for all of the labels and input fields of a
message.

When a button is clicked on the page that contains
the customized forms, the input is submitted and validated in Business
Process Choreographer Explorer. The validation is based on the type
of the properties provided and the locale used in the browser. If
the input cannot be validated, the same page is shown again and information
about the validation errors is provided in the messageValidationErrors request
attribute. The information is provided as a map that maps the
XML Path Expression (XPath) of the properties that are not valid to
the validation exceptions that occurred.

To add customized
forms to Business Process Choreographer Explorer, complete the following
steps using Integration Designer.

## Procedure

1. Create the customized forms. The user-defined
JSP pages for the input and output forms used in the web interface
need access to the message data. Use Java™ snippets
in a JSP or the JSP execution language to access the message data.
Data in the forms is available through the request context.
2. Assign the JSP pages to a task. Open the
human task in the human task editor. In the client settings, specify
the location of the user-defined JSP pages and the role to which the
customized form applies, for example, administrator. The client settings
for Business Process Choreographer Explorer are stored in the task
template. At run time these settings are retrieved with the task template.
3. Package the user-defined JSP pages in a web archive (WAR
file).  You can either include the WAR file in the enterprise
archive with the module that contains the tasks or deploy the WAR
file separately. If the JSPs are deployed separately, make the
JSPs available on the server where the Business Process Choreographer
Explorer or the custom client is deployed. 
If you are
using custom JSPs for the process and task messages, you must map
the web modules that are used to deploy the JSPs to the same servers
that the custom JSF client is mapped to.

## Results

The customized forms are rendered in Business Process Choreographer
Explorer at run time.

- User-defined JSP fragments

The user-defined JavaServer Pages (JSP) fragments are imbedded in an HTML form tag. At run time, Business Process Choreographer Explorer includes these fragments in the rendered page.