<!-- image -->

# Examining the files in Java EE
view

## About this task

## Procedure

1. Switch to the Java EE
view by selecting Window > Open
Perspective > Other > Java
EE.
2 Double-click the service name (for example, ConvPB) andselect gen/src > com.ibm.ims.mfs.emd.databinding .
    - The data binding Java files
are location in this folder. These files are based on the SCA framework.
    - The XSD files are what define the business objects in the business
integration perspective.
    - The import file is a file that has information about EIS system
(such as IMS) and connection
information. This file contains the resource adapter name and the
connection information. The resource adapter name must match the name
of the IMS TM
resource adapter that
is installed through the IBM® Process
Server administrative
console.<esbBinding xsi:type="EIS:EISImportBinding" dataBindingType="com.ibm.ims.mfs.emd.databinding.generator.MFSDataBindingGenerator">
 1    <resourceAdapter name="IMS TM Resource Adapter" type="com.ibm.connector2.ims.ico.IMSResourceAdapter" version="11.3.0">
      <properties/>
    </resourceAdapter>
 2    <connection target="<JNDI lookup>" type="com.ibm.connector2.ims.ico.IMSManagedConnectionFactory" interactionType="com.ibm.connector2.ims.ico.IMSInteractionSpec">
      <properties/>
    </connection>