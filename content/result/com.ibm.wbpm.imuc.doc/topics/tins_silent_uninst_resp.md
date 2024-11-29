# Uninstalling IBM Integration
Designer silently
using a response file

## Before you begin

## About this task

## Procedure

To silently uninstall IBM Integration
Designer,
complete the following steps:

1 Create the response files that will uninstall the requiredbase products and Integration Designer . Copyone of the sample response files in the following directory to createyour own response file:
    - To uninstall both Integration Designer and the
test environment: dvd\_root/disk1/responsefiles/responsefile.uninstall.iid.testenv.xml
    - To uninstall Integration Designer alone: dvd\_root/disk1/responsefiles/responsefile.uninstall.iid.xml
2. Modify the parameters as directed
in the text of the response file templates to create your response
files. You can also create response files by recording
your actions in Installation Manager. When you record a response file,
the selections that you make in Installation Manager are stored in
an XML file. When you run Installation Manager in silent mode, Installation
Manager uses the data in the XML response file to perform the installation.
3. Run the following command to uninstall both Integration Designer and the
test environment:IM\_location\tools\imcl.exe input extract\_location\disk1\responsefiles\responsefile.uninstall.iid.testenv.xml
    -log silentuninstall.logIM\_location/tools/imcl input extract\_location/disk1/responsefiles/responsefile.uninstall.iid.testenv.xml
    -log silentuninstall.log
Run the following command
to uninstall Integration Designer alone:IM\_location\tools\imcl.exe input extract\_location\disk1\responsefiles\responsefile.uninstall.iid.xml
    -log silentuninstall.logIM\_location/tools/imcl input extract\_location/disk1/responsefiles/responsefile.uninstall.iid.xml
    -log silentuninstall.log

## Results