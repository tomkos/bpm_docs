<!-- image -->

# Exporting modules and libraries as serviceDeploy files

## Procedure

1. From the File menu, select Export.
The Select page of the Export wizard opens.
2. In the Select page, expand Business Integration and
select Integration modules and libraries.
3. Click Next. The Export Integration
Modules and Libraries page opens.
4. The intended usage of the exported content determines the
export format. Select the Command line service deployment to
export the content as compressed files.
5. In the Select projects to export list box, select the name of each
project that you want to export and click Next.
6. In the Target file field, specify
a path name for the exported .zip file. Alternatively, you can click Browse to
navigate the file system and select a target file.
7. If you have changed any of your generated Java 2 Platform
Enterprise Edition projects, select the Include generated
Java 2 Platform Enterprise Edition projects from workspace check
box. The names of the Java 2 Platform Enterprise Edition projects
will be displayed in the Additional projects list
box. By default, all dependencies are automatically included in the
serviceDeploy .zip file. These dependencies are required to successfully
build an EAR file from the .zip file and deploy it using the serviceDeploy
command-line tool.
8. If there are global shared libraries that the exported
content depends on, these libraries are listed. These libraries must
be deployed to the runtime environment according to these instructions:
http://www-01.ibm.com/support/docview.wss?rs=2307&uid=swg21322617
9. Click Finish to export the selected
modules and libraries in a compressed file for command-line service
deployment.