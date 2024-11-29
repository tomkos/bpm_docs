<!-- image -->

# Configuring properties for EJB imports

The properties of an EJB import can be edited as required
from the assembly editor using the Properties view.

## Before you begin

You should know how to create an EJB import.

## About this task

- JNDI name - The JNDI Name is the logical name that an EJB import
would use to look up the EJB instance. For more information, see the
topic Administering EJB bindings in the IBM® Business Automation
Workflow information
center.
- Data Handler - The data handler provides transformation function
for transforming from one form to another. The transformation may
map into a provided target or into a new instance of a specified target.
- Fault Selector - The fault selector generates a fault identifier
that can be matched with one of the faults associated with the specific
outbound operation.
- Function Selector - The function selector is an artifact that
allows an EJB import to determine which EJB method should be invoked
for a given WSDL method on the EJB import. EJB import function
selector is the default value and it uses JAX-WS mapping to determine
the EJB method. For more information, see the IBM Business Automation
Workflow information
center.
- Faults configuration - The configuration of the fault handler
is optional. By default, JAX-WS data handler configured at the EJB
import level is used for all of the faults.

## Procedure

1. From the assembly editor, select the EJB import in the
assembly diagram.
2. Select the Properties tab to view the properties for the
EJB import and edit the values for them as required.
3. Save the changes.