<!-- image -->

# Changing URLs for web service exports

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services export.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4 Change the context root by completing the following steps:
    1. Select the Application Project node.
    2. Click Add and select Context Root. The Context Root node is added under Application
Project.
    3. In the Context root field, replace
the existing context root with a new context root. For example, NewContextRoot.
5 Create a URL mapping for the web services export by completingthe following steps:

1. Select the Web Services Exports node.
2. Click Add and select Web Service Export. A Web Service Export node is added
under Web Services Exports.
3. In the Name field, select your
web service export. For example, receiveWebServiceCallFromClient.
4. Click Add and select URL Mapping. A URL Mapping node is added under Web Service
Export.
5. In the URL pattern field, type
the name of the new URL pattern. For example, /NewURLPattern.
6 Remove the default URL mapping for the web services exportby completing the following steps:

1. Select the Web Services Exports node.
2. Click Add and select URL Mapping (Default). The URL Mapping (Default) node
is added beneath Web Service Export.
3. Disable the Include default mapping check box.
7. Press Ctrl-S to save your changes
and close the module deployment editor.
8. If your server is already running in the Servers view,
click the Build Activities tab to open the
Build Activities view and then click Update Running Servers.