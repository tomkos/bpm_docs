<!-- image -->

# Modules: Deleting mediation policies for modules

## Before you begin

1. Use IBM Integration Designer to create a module containing a Policy Resolution mediation
primitive.
2. Deploy the module to Process Server.
3. Ensure that Process Server has a definition for the WSRR that you want to use.
4. Load the enterprise archive (EAR) file, containing your module, into WSRR.
5. Create a business space that contains the Module Browser widget and the
Mediation Policy Administration widget.

## About this task

You can control service requests dynamically by using mediation policies to override module
properties at run time. Such mediation policies are stored in WSRR. You can define one or more
mediation policies for your module, and each mediation policy can override one or more module
properties. Optionally, you can create one or more gate conditions on each policy attachment. When
service requests are processed, gate conditions are compared to the condition values in the message.
All the gate conditions must be met before an associated mediation policy can be used.

## Procedure

1. Log in to your business space and navigate to the space that you created for administering
mediation policies associated with modules.
2. From the Module Browser widget, select Mediation
Policies.
The Mediation Policy Administration widget is refreshed. If there
are existing policy attachments they are displayed.
3. If you have more than one WSRR definition, then select the definition used by your
module.
If you change the WSRR definition, the list of policy attachments changes.
4. Click the Delete icon of the policy attachment that you want to
delete.
 Each policy attachment row has a cross icon, at the end of the row, that you can click to
delete the policy attachment.
You are asked if you want to delete the policy attachment.
5. Click OK.

## Results

In WSRR, the policy attachment is deleted. Any associated mediation policies are also deleted,
unless they are being used by another policy attachment.