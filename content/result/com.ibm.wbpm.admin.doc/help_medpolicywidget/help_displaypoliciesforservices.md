<!-- image -->

# Services: Displaying mediation policies for services

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
2. From the Service Browser widget, check that the correct WSRR definition is
displayed. If the correct WSRR definition is not displayed, select the correct WSRR definition. 
If your application server has definitions for more than one instance of WSRR, you can display
the services that are defined on each WSRR. 
When you change the WSRR definition, the list of services is refreshed.
3. Select the level for which you want to display policy attachments. 
Mediation policies can be attached at the level of the service, endpoint, or operation. 
The Mediation Policy Administration widget is refreshed. If there
are existing policy attachments they are displayed.
4. From the Mediation Policy Administration widget, click the
Edit icon of the policy attachment that you want to work with. 
Each policy attachment row has a pencil icon, at the end of the row, that you can click to
view mediation policy information.

## Results

- Assertions: The module properties that the mediation policy can override. In WSRR, the moduleproperties appear as policy assertions.
    - Group Name: The group to which the property belongs. By default, the group name is the name of
the mediation flow component.
    - Property Name: The alias name of the property. The alias name identifies the property in the
mediation flow.
    - Value: The current value in the mediation policy, rather than the current value in the module.
When a mediation policy is available and suitable, the mediation policy value takes precedence.
- Gate Conditions (Optional): Conditions that must be met before the mediation policy can be used.In WSRR, gate conditions are user properties on the policy attachment object.

- Name: The name of a gate condition is always prefixed with the string
medGate\_.
- Value: The value of the gate condition, for example, country = France or
Age > 59.