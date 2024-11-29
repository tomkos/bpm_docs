<!-- image -->

# Editing WS-Security properties

## About this task

- Specifying the request generator properties for the import.
- Specifying the request consumer properties for the export.
- Specifying the response generator properties for the export.
- Specifying the response consumer properties for the import.

These tasks are described in the following steps:

## Procedure

1 Specify the request generator properties for the import:
    1. In the Business Integration view,
right-click the module that contains your import and select Open Deployment Editor. The module deployment editor
opens.
    2. Select the Design tab.
    3. Select the Web Services Imports node.
    4. Click Add and select Web Services Client Security Extensions, then click OK. The Web Services Client Security Extensions node
is added under Web Services Imports and the Component Scoped Reference
node is added under the Web Services Client Security Extensions node.
    5. Select the Component Scoped Reference node.
    6. Click Add and select Service Reference, then click OK. The Select a Web Service Import window appears.
    7. In the window, select your web service import and click OK.
    8. Select the Port Qualified Name Binding node.
    9. Click Add and select Client Service Configuration, then click OK.
    10. Select the Client Service Configuration node.
    11. Click Add and select Request Generator Configuration, then click OK.
    12. Add nodes to the Request Generator Configuration node to specify properties for the security mechanism that you are
implementing, such as security token, integrity, confidentiality,
and timestamp.
    13. Select the Web Services Imports node.
    14. Click Add and select Web Services Client Binding Configurations, then click OK. The Web Services Client Binding Configurations node
is added under Web Services Imports and the Component Scoped Reference
node is added under the Web Services Client Binding Configurations
node.
    15. Select the Component Scoped Reference node.
    16. Click Add and select Service Reference, then click OK. The Select a Web Service Import window appears.
    17. In the window, select the import that you want to use
and click OK.
    18. Select the Port Qualified Name Binding node.
    19. Click Add and select Security Request Generator Binding Configuration, then
click OK.
    20. Add nodes to the Security Request Generator Binding
Configuration node to specify properties that correspond to the extension
properties that you specified under Request Generator Configuration,
such as token generator, signing information, and encryption information.
    21. Press Ctrl-S to save your changes
to the deployment side file ibm-deploy.scaj2ee in the Physical Resources
view.
2 Specify the request consumer properties for the export:

1. In the Business Integration view,
right-click the module that contains your export and select Open Deployment Editor. The module deployment editor
opens.
2. Select the Design tab.
3. Select the Web Services Exports node.
4. Click Add and select Web Services Security Extensions, then click OK.
5. Select the Web Services Security Extensions node.
6. Click Add and select Web Service Description Extension, then click OK. The Select a Web Service Export window appears.
7. In the window, select the export that you want to use
and click OK.
8. Select the Port Component Binding node.
9. Click Add and select Server Service Configuration, then click OK.
10. Select the Server Service Configuration node.
11. Click Add and select Request Consumer Service Configuration Details, then
click OK.
12. Add nodes to the Request Consumer Service Configuration
Details node to specify properties that correspond to the extension
properties that you specified for the import, such as required security
token, required integrity, required confidentiality, and timestamp.
13. Select the Web Services Exports node.
14. Click Add and select Web Services Binding Configurations, then click OK.
15. Select the Web Services Binding Configurations node.
16. Click Add and select Web Service Description Binding, then click OK. The Select a Web Service Export window appears.
17. In the window, select the export that you want to use
and click OK.
18. Select the Port Component Binding node.
19. Click Add and select Request Consumer Binding Configuration Details, then
click OK.
20. Add nodes to the Request Consumer Binding Configuration
Details node to specify properties that correspond to the properties
that you specified under Request Consumer Service Configuration Details,
such as token consumer, signing information, and encryption information.
21. Press Ctrl-S to save your changes
to the deployment side file ibm-deploy.scaj2ee in the Physical Resources
view.
3 Specify the response generator properties for the export:

1. In the Business Integration view,
right-click the module that contains your export and select Open Deployment Editor. The module deployment editor
opens.
2. Select the Design tab.
3. Select the Web Services Exports node. (If you followed the instructions in step 2 and
you are now working with the same export, you can simply expand all
levels of the Web Services Exports node and
skip to step j below.)
4. Click Add and select Web Services Security Extensions, then click OK.
5. Select the Web Services Security Extensions node.
6. Click Add and select Web Service Description Extension, then click OK. The Select a Web Service Export window appears.
7. In the window, select the export that you want to use
and click OK.
8. Select the Port Component Binding node.
9. Click Add and select Server Service Configuration, then click OK.
10. Select the Server Service Configuration node.
11. Click Add and select Response Generator Service Configuration Details, then
click OK.
12. Add nodes to the Response Generator Service Configuration
Details node to specify properties for the security mechanism that
you are implementing, such as security token, integrity, confidentiality,
and timestamp.
13. Select the Web Services Exports node.  If you followed the instructions in step 2 and
you are now working with the same export, expand all
levels of the Web Services Exports node and
skip to step r below.
14. Click Add and select Web Services Binding Configurations, then click OK.
15. Select the Web Services Binding Configurations node.
16. Click Add and select Web Service Description Binding, then click OK. The Select a Web Service Export window appears.
17. In the window, select the export that you want to use
and click OK.
18. Select the Port Component Binding node.
19. Click the Add button and select Response Generator Binding Configuration Details, then
click OK.
20. Add nodes to the Response Generator Binding Configuration
Details node to specify properties that correspond to the properties
that you specified under Response Generator Service Configuration
Details, such as token generator, signing information, and encryption
information.
21. Press Ctrl-S to save your changes
to the deployment side file ibm-deploy.scaj2ee in the Physical Resources view.
4 Specify the response consumer properties for the import:

1. In the Business Integration view,
right-click the module that contains your import and select Open Deployment Editor. The module deployment editor
opens.
2. Select the Design tab.
3. Select the Web Services Imports node. (If you followed the instructions in step 1 and
you are now working with the same import, you can simply expand all
levels of the Web Services Imports node and
skip to step j below.)
4. Click Add and select Web Services Client Security Extensions, then click OK. The Web Services Client Security Extensions node
is added under Web Services Imports and the Component Scoped Reference
node is added under the Web Services Client Security Extensions node.
5. Select the Component Scoped Reference node.
6. Click Add and select Service Reference, then click OK. The Select a Web Service Import window appears.
7. In the window, select your web service import and click OK.
8. Select the Port Qualified Name Binding node.
9. Click Add and select Client Service Configuration, then click OK.
10. Select the Client Service Configuration node.
11. Click Add band select Response Consumer Configuration, then click OK.
12. Add nodes to the Response Consumer Configuration node
to specify properties that correspond to the extension properties
that you specified for the export, such as required security token,
required integrity, required confidentiality, and timestamp.
13. Select the Web Services Imports node. (If you followed the instructions in step 1 and
you are now working with the same import, you can simply expand all
levels of the Web Services Imports node and
skip to step r below.)
14. Click Add and select Web Services Client Binding Configurations, then click OK. The Web Services Client Binding Configurations node
is added under Web Services Imports and the Component Scoped Reference
node is added under the Web Services Client Binding Configurations
node.
15. Select the Component Scoped Reference node.
16. Click Add and select Service Reference, then click OK. The Select a Web Service Import window appears.
17. In the window, select the import that you want to use
and click OK.
18. Select the Port Qualified Name Binding node.
19. Click Add and select Security Response Consumer Binding Configuration, then
click OK.
20. Add nodes to the Security Response Consumer Binding
Configuration node to specify properties that correspond to the extension
properties that you specified under Response Consumer Configuration,
such as token consumer, signing information, and encryption information.
21. Press Ctrl-S to save your changes
to the deployment side file ibm-deploy.scaj2ee in the Physical Resources view.

## Example

1. Close the module deployment editor.
2. In the Physical Resources view, right-click
the deployment side file ibm-deploy.scaj2ee and select Delete.
3. In the Physical Resources view or the Business Integration view, click your module to select
it.
4. From the Project menu, select Clean. The Clean? window opens.
5. Select Clean selected projects and then
click OK. When the module has finished rebuilding,
you can open the module deployment editor as usual.

## What to do next