<!-- image -->

# Defining user interfaces for a human task

## Procedure

1. Open your human task in the editor.
2. Under User interface settings, choose
the type of client.
3 In the Properties page, configure the client as follows: Option Description HTML-Dojo client for Heritage Process Portal spaces Use the Context root and HTMLFile fields to specify the location of the HTML file thatcontains the visualization of the user interface. These fields areused to compose the URL from which your HTML file is uploaded usingthe following format: http://localhost/contextroot /pathAndFile Ifno HTML file exists, you can click New to createone. In the New HTML file window, you can choosean existing web project for the new HTML file, or click NewWeb Project to create one. Tip: Modify theHTML file by using a text or HTML editor. Business Process Choreographer Explorer With this option, the task is delivered to the staff membervia an HTML-based web page. In the JSP definition table, specify theinput and output JSPs. If no JSPs are specified, the standard client is used. External Implementation (for use in Process Portal ) Specify the URL for the external user interface that is calledwhen a user opens the task in Process Portal . Usereplacement variables to include runtime information, for example,the task instance ID: %htm:task.property.ExternalRoot%/task?id=%htm:task.instanceID% . Process Portal automaticallyappends the REST URL to the restUrlPrefix parameterto indicate where task related operations can be performed. For moreinformation, see Replacement variables in human tasks . The JSF custom client is not included in this list becausethe client generator does not require any properties to be configuredin order to generate the client.If you are using Business ProcessChoreographer Explorer, you do not need to generate a client, as astandard client is provided for it.

| Option                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HTML-Dojo client for Heritage Process Portal spaces | Use the Context root and HTML File fields to specify the location of the HTML file that contains the visualization of the user interface. These fields are used to compose the URL from which your HTML file is uploaded using the following format: http://localhost/contextroot/pathAndFileIf no HTML file exists, you can click New to create one. In the New HTML file window, you can choose an existing web project for the new HTML file, or click New Web Project to create one. Tip: Modify the HTML file by using a text or HTML editor.                                                                        |
| Business Process Choreographer Explorer             | With this option, the task is delivered to the staff member via an HTML-based web page. In the JSP definition table, specify the input and output JSPs.  Click Add. On the JSP definition page, select the JSP type.  In the Apply to field, select the role that sees the JSP. You can then create a JSP, or browse to an existing one, and use the Context root field to define the runtime path to the JSP. If you have WSDL faults defined in your interface, you can select a Fault message JSP as the JSP type, and then select the fault that triggers it.  If no JSPs are specified, the standard client is used. |
| External Implementation (for use in Process Portal) | Specify the URL for the external user interface that is called when a user opens the task in Process Portal. Use replacement variables to include runtime information, for example, the task instance ID:  %htm:task.property.ExternalRoot%/task?id=%htm:task.instanceID%. Process Portal automatically appends the REST URL to the restUrlPrefix parameter to indicate where task related operations can be performed. For more information, see Replacement variables in human tasks.                                                                                                                                   |

If you are using Business Process
Choreographer Explorer, you do not need to generate a client, as a
standard client is provided for it.

## What to do next

## Related concepts

- Before you begin: Client types and prerequisites

## Related tasks

- Generating HTML-Dojo pages for Heritage Process Portal spaces (deprecated)
- Integrating JavaScript in HTML-Dojo pages
- Preparing to extend generated JSF code
- Customizing clients
- Deploying a generated client to an external runtime environment

## Related reference

- Design considerations for user interface generation