<!-- image -->

# Limitations of the module deployment editor

A known limitation is:

- Deployment side file must be manually updated after any binding
changes

This limitation is discussed in the following section.

## Deployment side file must be manually updated after
any binding changes

In this release of IBM® Integration
Designer, the module deployment editor enables a user to configure WS-Security
deployment options on web service exports and imports. The data associated
with the configured deployment options is stored in a deployment side
file named ibm-deploy.scaj2ee, which is located in the root of the
SCA module in the Physical Resources view of the Business Integration
perspective. For example, MyModule/ibm-deploy.scaj2ee. The
deployment side file can contain binding information, such as the
port name and address of web service imports and the port name and
service name of web service exports.

If the binding information
of a web service import or export is changed, then the copy of this
binding data in the deployment side file will be invalidated. For
example, if you manually change the address of a web service import
in the assembly diagram of the associated module, the binding data
in the deployment side file will not reflect the new address of the
web service import.

To ensure that the deployment side file
reflects any binding changes to your web service imports or exports,
you must open the deployment side file in a text editor and then manually
update the deployment information to reflect the changes to the binding
information.