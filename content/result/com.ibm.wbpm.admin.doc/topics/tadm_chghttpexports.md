<!-- image -->

# Viewing and updating HTTP export bindings

## About this task

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Exports.
    2. Expand the export, and then
expand Binding.
    3. Click the binding to view
information about its properties.
3 Select the scope for thechanges you want to make. When both configurations exist, the method scope configurationtakes precedence over the binding scope configuration.

- To change the configuration on the binding scope, click the Binding
Scope tab.
- To change the configuration at the method scope, click the Method
Scope tab.

When both configurations exist, the method scope configuration
takes precedence over the binding scope configuration.

4 Make changes to one or more of the following properties:

- Select method (Method scope only)Choose the method that you want
to review or configure. Click the arrow in the Select method field to see the
list of methods that can be configured.
- HTTP Methods Lists the methods and the current configuration forthe methods. You can set whether the method is pingable and the return code for the method.
    - MethodThe name of the method. The methods are GET, POST, PUT, DELETE,
TRACE, OPTIONS, and HEAD.
    - PingableWhether or not an HTTP client can ping the method. When
selected, you must specify the return code the binding returns to the client. The default for this
is unchecked.
    - Return codeAn integer returned when an HTTP client pings the
method.
- Transfer EncodingSpecifies how information is transferred between
the endpoints. Choices are chunked or identity.

The chunked encoding modifies the body of a message in order to transfer it as a series of
chunks, each with its own size. This allows dynamically produced content to be transferred along
with the information necessary for the recipient to verify that it has received the full message.
Important: If you set this parameter to chunked, Content Encoding
is set to identity and you will be unable to change Content
Encoding.
- Content EncodingSpecifies how the content that traverses the
binding is encoded. Choose either gzip, x-gzip,
deflate, or identity.
5. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.