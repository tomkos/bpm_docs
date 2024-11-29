# Importing case assets by using a solution package

## Procedure

To import a solution package for case solutions that haven't been promoted, complete
the following steps:

1. Copy the compressed file that contains the exported solution package to a location that is
accessible by the Case administration client .
2. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM® Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
3. In the navigation pane, select the design or staging object store to which you want to import
the solution and click Solutions.
4 On the Solutions page, clickImport > Import Solution > FromSolution Package and complete the wizard steps. Tip: By default, the Import Solution wizard is configured to display the targetprincipal mapping step to users. You can hide the target principal mapping from users by clearingEnable target principal mapping when assets are imported in the Case Manageradministration plug-in, which is located in the Admin desktop of IBM ContentNavigator . This hides thetarget principal mapping for the entire environment rather than just for the import process of aspecific solution.
    1. Map object stores: Object store mapping appears when you have object store references in FileNet
Process Engine workflow definitions. The mapping enables you to update the object store references
in the workflow definitions.
    2. Map service data: Service data mapping appears when you have case solution pages with website
URL specified, including adapter pages for client-side human services. The mapping panel also
appears if you have any external WSDL URL or Partner links specified in any FileNet Process Engine
workflow definitions.

## What to do next

- Reimporting assets with content that contains environment-specific references

When a solution is reimported to the same object store, environment-specific changes to the assets of that solution might not show up in the reimported version.