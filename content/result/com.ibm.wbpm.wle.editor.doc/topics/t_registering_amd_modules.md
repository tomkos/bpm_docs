# Adding custom AMD modules

## About this task

- Dojo 1.10.4
- Dojo 1.10.5

With this loader, you can package custom AMD modules and then register a dependency on those
modules in your view. Registering a module involves assigning an alias for the module because the
view accesses the module by using its alias.

When you upgrade to Business Automation Workflow V8.5.7 Cumulative Fix
2016.12, your Dojo version is automatically upgraded to Dojo 1.10.5 if your coach or
system toolkit is version 8.5.7. After the upgrade, any custom artifacts that were built using Dojo 1.10.4 must be
verified to ensure that they are working correctly.

## Procedure

1 Prepare your AMD package:
    1. Package your AMD modules in a .zip file such as
myPackage.zip.
    2. Upload that .zip file as a managed web file.
    3. Create a JavaScript file to define the
package map for your AMD modules. For example, create the
myPackageMap.js file and add the following package map code for AMD modules
that are called myModule and myOtherModule:require({
	packages: [
		{name: 'myModule', location: com\_ibm\_bpm\_coach.getManagedAssetUrl('myPackage.zip', 
			com\_ibm\_bpm\_coach.assetType\_WEB, 'PROJECT') + "/path/to/myModule"}
		{name: 'myModule', location: com\_ibm\_bpm\_coach.getManagedAssetUrl('myPackage.zip', 
			com\_ibm\_bpm\_coach.assetType\_WEB, 'PROJECT') + "/path/to/myOtherModule" }
	]
});The PROJECT parameter contains the acronym or short name of the
process application or toolkit
that contains the .zip file. If the module is in the current process application, the
PROJECT parameter is optional. If the module is in a referenced toolkit, you must
include the PROJECT parameter to ensure that the view can use module in the
context of the process application. If the class for the AMD module is at the root of the managed web file, do not
include the /path/to/myModule parameter. The /path/to/myModule
is the path in the .zip file to the AMD module class.
    4. On the Behavior page of your view, add the JavaScript file as an included script.
2 Register each AMD module in your view:

1. On the Behavior page of the view, select AMD
dependencies.
2 Click Add and then specify the following information:
    - In the Module ID column, declare the dependency on the AMD module by
using a path like myPackage/path/to/myModule.
    - In the Alias column, type the alias that you use in the code to refer to
the module.
3. In your view code, use the alias to access the functions of the AMD module.
4. Click Save or Finish Editing.