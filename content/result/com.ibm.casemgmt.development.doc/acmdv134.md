# Creating custom property editors and controllers

## About this task

## Procedure

To create an extensions package for a custom property
editor and controller:

1. Create a web project that contains the following folders
for your extensions package:

Folder
Content

ProjectName/ProjectNamePlugin
Contains the files that are used to create the
JAR file for the IBM® Content
Navigator plug-in.

ProjectName/ProjectNamePlugin/src/PackageName
Contains the files that are used to create the
JAR file for the IBM Content
Navigator plug-in.

ProjectName/ProjectNamePlugin/src/PackageName/WebContent
Contains the main JavaScript plug-in file and the root folder
of your custom editors and controller code. It can have subfolder
structures to organize the code packages. 

ProjectName/ICMRegistry
Contains the Extension.json file that is used to register
the extensions package and optionally the translated Extension.json in the
nls subfolder.Note: In the Extension.json file, replace
the relative path with the Content Navigator absolute path.
2 Create the registry files and place them in the ICMRegistry folder:
    1. Create a file called Extension.json.
This JSON-format file indicates the ID, title, description,
type, packages, CSS, and a bootstrap class of the extensions.
    2. Optional: 
For a different locale, you can
create the translated Extension.json files, and
put them in the corresponding language folders under the nls subfolder.
For example, create ICMRegistry/nls/fr/Extension.json for
a French locale.
3 Create a standard Content Navigator plug-in in theProjectName/ProjectNamePlugin folder to hold the source code for your customeditors and controllers. Create the following items in the WebContent folder of theplug-in:

1. Create a self-contained Dojo widget to represent the customer editor that you want to use in
the properties view.
2. Create a registry file to describe the custom editor, and specify the types of the properties
that are suitable to use with the editor in the registry. 
This registry file is used to register the editor into Properties View
Designer.
3. Optional: 
If you want to interact with custom data types, you can create a custom controller to use with
the editor and the custom data type. 
You must also create a custom integration configuration file to load the custom controller in
the integration configuration.
4. Create a bootstrap class to register the custom editor and custom controllers.
4 Create an extensions package that contains the custom plug-in and registration file:

1 Create a build.xml script that builds the following components:
    - The ICMRegistry folder that includes the extension definitions.
    - A JAR file that contains the IBM Content
Navigator plug-in.
5. In the Extension.json file, update the relative path with the Content
Navigator absolute path.
6. In the Case configuration tool, run
the Deploy and Register Extensions Package task to register and deploy your extensions package. For
this, manually place the reference to a CORS filter servlet in web.xml in the
external Navigator, and set the Access-Control-Allow-Origin: <baw-hostName>
header in the CORS filter. For more information about configuring the web.xml
file, see Upgrading your IBM Case Manager system using an external IBM Content Navigator 
Important: If you run this task in a cluster
environment, you must ensure that the plug-in is loaded on each node of the cluster. Either restart
the cluster to force the plug-in to be loaded on all nodes or manually load the plug-in on each node
by using the IBM Content
Navigator administration
client.
7. In Case Builder,
use Properties View Designer to choose the custom properties editor
for a property in a properties view.
8. Deploy and test your solution.