<!-- image -->

# Endpoint updates in a web services binding

## Endpoint updates in a unit test environment

During
the development and testing of a web service, you can update an endpoint
address in either the properties view of the web services binding
or in the WSDL editor.

To update an endpoint from the binding
properties view, select the import or export in the assembly editor
and open the Properties view. Select the Bindings tab.
The endpoint can be viewed and updated from the Address field.

To
update an endpoint from the WSDL editor properties view for a web
services import binding, click the canvas and open the Properties view.
Select the General tab. The endpoint can be
viewed and updated from the Address field.

You cannot update the endpoint value in the Address field
of a web services export binding.

## Endpoint updates in a production environment

After
you have deployed a service to a server in a production environment,
you can still change an endpoint by using the Process Admin Console.

To
change the endpoint on a production server, see Administering bindings.
Each binding has a section on viewing and updating the binding information
including the endpoint URL.