# Improving view performance

## About this task

With the Dojo build system, your view can include the modules that it depends on in one file or
small set of files. These files, each one a layer, reduce the number of HTTP requests that are
needed by the process application
that contains the view. You can use the layers to improve performance by optimizing the loading of
the modules without sacrificing modular development. These layers can be custom code or be
third-party Dojo layers. The layer files must be built with the Dojo version that is compatible with
the Dojo version that your view uses.

Two modes are available for you to use: debug and non-debug. The isDebug
configuration setting in the administrative console determines which mode is in effect. You can
specify different layers for each mode.

The build layer definitions must be in a specific format at the start of the inline JavaScript for the view. The designer uses this format to
generate the appropriate code in the HTML for the coaches that contain the view.

## Procedure

1. If you have custom code, transform it into a Dojo build layer. For information
about Dojo build layers and how to create them by using a transform, see The Dojo Build
System.
2 Prepare your custom JavaScript:
    1. Package your Dojo build layer in a .zip file, such as
myLayer.zip.
    2. Upload that .zip file as a managed web file.
3 On the Behavior page, add a specific comment block at the beginning of theinline JavaScript. The comment block consists of two sets of tag blocks: Tip: If you have multiple views that are adding the same layers, copy the commentblock into these views. If the layer content is the same, Process Designer combines it so thatthe generated page contains only one copy of the layer code. The followingexample shows the comment block for adding Dojo build layers. For your implementation, replace thename and location values in the Dojo configuration section and replace the names in the layer section./* 1 @dojoConfigUpdateStart 2 if (dojoConfig.isDebug) { dojoConfig.packages.push({ name: 'com.mycompany.dashboards ', 3 location: com\_ibm\_bpm\_coach.getManagedAssetUrl('myLayer\_debug.zip ', com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSD') + "/com/mycompany/dashboards " 4 }); } else { dojoConfig.packages.push({ name: 'com.mycompany.dashboards ', location: com\_ibm\_bpm\_coach.getManagedAssetUrl('myLayer.zip ', com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSD') + "/com/mycompany/dashboards " }); }@dojoConfigUpdateEnd @layerRequiredStart 5 { "nonDebug":["com.mycompany.dashboards/dashboards ", "com.mycompany.dashboards/dashboardsMore "], 6 "debug":["com.mycompany.dashboards/dashboardsDebug "] }@layerRequiredEnd* / For more examples of how to add layers, see many of the views in theDashboards toolkit.

- @dojoConfigUpdateStart and @dojoConfigUpdateEnd contain normal
JavaScript code that updates the global
dojoConfig variable before the system loads the Dojo AMD loader.
- @layerRequiredStart and @layerRequiredEnd contain a JSON
structure with two optional properties (debug and non-debug). Each property is a JavaScript array type that contains the full name of the layers for each
mode. The full name is the package name and the layer file name.

```
/*  1 
@dojoConfigUpdateStart  2 
	if (dojoConfig.isDebug) {
		dojoConfig.packages.push({
			name: 'com.mycompany.dashboards',  3 
				location: com\_ibm\_bpm\_coach.getManagedAssetUrl('myLayer\_debug.zip', 
				com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSD') + "/com/mycompany/dashboards"  4 
		});
		} else {
			dojoConfig.packages.push({
				name: 'com.mycompany.dashboards',
					location: com\_ibm\_bpm\_coach.getManagedAssetUrl('myLayer.zip', 
					com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSD') + "/com/mycompany/dashboards"
		}); 
	}
@dojoConfigUpdateEnd 
@layerRequiredStart  5 
	{
		"nonDebug":["com.mycompany.dashboards/dashboards",
			"com.mycompany.dashboards/dashboardsMore"],  6 
		"debug":["com.mycompany.dashboards/dashboardsDebug"]
	}
@layerRequiredEnd
* /
```

- 1  Using a comment prevents the comment’s contents from being
run as actual inline JavaScript of the view.
- 2  The start of the Dojo configuration section
- 3  The namespace for the package
- 4  The location of the managed file that contains the package
- 5  The start of the layer section
- 6  The name of the package and module within that package for the
layer to use in this mode. In this example, the non-debug mode loads two layers and the debug mode
loads one layer.
4. Click Save or Finish Editing.