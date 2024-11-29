<!-- image -->

# Configuring servers to invoke services synchronously

## Before you begin

## About this task

Figure 1. Invoking a service on a different system

<!-- image -->

## Procedure

1. Install the applications on each server.
2 Create a new namespace binding on the invoking system (System A, in the example) pointing tothe export on the target system. On the Name Space Bindings panel, select a scope of Cell and clickApply . With the changed scope, click New in thedisplay to create the new binding. In the wizard, specify the following (the values are appropriate for the example configuration): Your system displays your new binding.

On the Name Space Bindings panel, select a scope of Cell and click
Apply. With the changed scope, click New in the
display to create the new binding.

    1. Binding type is CORBA
    2 The basic properties are: When finished, click Next and verify the values on theSummary page. After verifying, click Finish .
        - Binding identifier is a unique string, in our example:
sca\_import\_test\_sca\_cross\_simple\_custinfo\_CustomerInfo
        - Name in Name space is the JNDI name of the enterprise Java™
bean (EJB) you are invoking on the target system, for example:
sca/AppB/export/test/sca/cros/simple/custinfo/CustomerInfo This names the
export interface on the target system.
        - Corbaname URL is the IP address and port number of the naming service on the target system:
corbaname:iiop:host:port/NameServiceServerRoot#<package.qualified.interface>

Note: For WebSphere®
Business Process Manager, the port is the BOOTSTRAP\_ADDRESS.

For example:

corbaname:iiop:9.26.237.144:2809/NameServiceServerRoot#sca/
		AppB/export/test/sca/cros/simple/custinfo/CustomerInfo

When finished, click Next and verify the values on the
Summary page. After verifying, click Finish.

3. Save your changes by clicking Save.
4. If your cross cell configuration consists of servers on the same host with the same name and
you encounter JNDI lookup failures with a NameNotFoundException, then you need to
set a system property. 

Follow the directions in the Application access problems under the subheading Two servers with the
same name running on the same host are being used to interoperate.

## What to do next