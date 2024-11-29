<!-- image -->

# Services: Deleting mediation policies for services

## Before you begin

1. Use IBM Integration Designer to create a module containing a Policy Resolution mediation
primitive.
2. Deploy the module to Process Server.
3. Ensure that Process Server has a definition for the WSRR that you want to use.
4. In WSRR, load the enterprise archive (EAR) file containing your module. Also, load the WSDL
documents for the services that you want to attach mediation policies to.
5. Create a business space that contains the administration widgets you need, including the
Service Browser and Mediation Policy Administration
widgets.

## About this task

You can control service requests dynamically by using mediation policies to override module
properties at run time. Such mediation policies are stored in WSRR. You can define one or more
mediation policies for services used by your module, and each mediation policy can override one or
more module properties. Optionally, you can create one or more gate conditions on each policy
attachment. When service requests are processed, gate conditions are compared to the condition
values in the message. All the gate conditions must be met before an associated mediation policy can
be used.

## Procedure

1. Log in to your business space and navigate to the space that you created for administering
services.
2. From the Service Browser widget, if the correct WSRR definition is not
displayed select the correct WSRR definition. 
If your application server has definitions for more than one instance of WSRR, you can display
the services that are defined on each WSRR. 
 The list of services is refreshed.
3 Select the level at which you want to delete a policy attachment and associated mediationpolicies. You can attach a mediation policy at the level of the service, endpoint, or operation. The Mediation Policy Administration widget is refreshed. Thefollowing information is displayed:
    - The name of the service, endpoint, or operation that you selected.
    - The WSRR definition that you selected.
    - Any policy attachments that exist for the service, endpoint, or operation that you selected.
4. Click the delete icon of the policy attachment that you want to delete.
 Each policy attachment row has a cross icon, at the end of the row, that you can click to
delete the policy attachment.
You are asked if you want to delete the policy attachment.
5. Click OK.

## Results

In WSRR, the policy attachment is deleted. Any associated mediation policies are also deleted,
unless they are being used by another policy attachment.