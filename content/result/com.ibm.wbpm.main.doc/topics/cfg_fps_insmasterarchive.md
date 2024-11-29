# Installing a master archive of an IBM® Process Federation
Server configuration on another federated
system

## Before you begin

## Procedure

1. Transfer the master archive file to the new system.
2. Extract the contents of the archive file and run the following command.
java -jar package\_file\_name [Options] install\_locationWhere:
package\_file\_name.zip
The name of the file that you are extracting.
Options

--acceptLicense
Automatically indicate acceptance of license terms and conditions.

For a list of all the options, see Archive file extraction options.
install\_location
The path to the directory where you want to install the products. If you do not specify an
installation location, the directory that contains the archive file is used.Restriction: Ensure that the directory names in the path contain only the following characters: 0-9 A-Z a-z
(space) & ( ) + - . \_
3. Remove duplicated code. If the installation
of the master Process Federation Server configuration
was not done in the pfs\_install\_root directory,
you will have two copies of the bpmFederatedProcessServer directory
on the new system after you install the master archive. During installation
of the archive, the ibmProcessFederationServer directory
is copied to the pfs\_install\_root directory
on the new system. However, the archive still contains a copy of the pfs\_install\_root/ibmProcessFederationServer directory.
You can delete the pfs\_install\_root/ibmProcessFederationServer from
the archive on the new system.