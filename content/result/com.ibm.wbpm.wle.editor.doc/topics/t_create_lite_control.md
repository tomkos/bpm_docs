# Example: creating a custom AngularJS progress bar coach view (deprecated)

## About this task

You can build a custom AngularJS control in your own toolkit.
In the following procedure, the custom control is built in a new toolkit,
therefore process applications that use this control must have a dependency
on the Responsive Coaches toolkit. Take note of your toolkit acronym
and use your toolkit acronym in the following examples. The examples
in the steps use a toolkit with an acronym of MYTK. The Responsive Coaches toolkit has the acronym of SYSRC. Also note that the example that uses the <meter> HTML5 tag, which is not supported in Microsoft Internet Explorer; does not work
in Internet Explorer.

## Procedure

1. Create the HTML file for the control.  For example, to create a Progress Bar control, create a file named
						progressBar.html that contains the following
					code:<div class="textLabel ng-cloak" ng-show="showLabel()">
	<label id="progress-label-{{viewid}}" class="text control-label" 
		ng-class="'bpm-label-'+textSize" dir="{{textDirection}}" ng-bind="label"></label>
</div>
<div id="progressBar-{{viewid}}" class="ng-cloak" role="progressbar" aria-valuenow="{{bindingValue}}" aria-valuemin="{{minValue}}" aria-valuemax="{{maxValue}}">
	<meter id="progressBar-progress-{{viewid}}" ng-disabled="disabled"
		aria-labelledby="progress-label-{{viewid}}" value="{{bindingValue}}" min="{{minValue}}" max="{{maxValue}}" style="width:100%" >
	</meter>
</div>In the example, the value for bindingValue comes from the business object to which the
user binds the control. The maxValue and minValue attributes are configuration options that are
defined later in the procedure.
2. Upload the HTML file to your toolkit by creating a web
file and selecting the HTML file.
3 Create two versions of the controller JavaScript file. The firstversion is for debugging purposes and is in a readable format. Thesecond version is for run time and is compressed for improved performance.
    1 Create the debug version of the controller file, andadd JavaScript code toit that does the following things: For example, create a file named progressBar.controller.js and add the following code to it:angular .module("responsive.coaches") .controller("progressBar", ["$scope", "$element", "$timeout","Coach", function ($scope, $element, $timeout, Coach) { "use strict"; angular.extend($scope, new Coach($scope, $element, $timeout)); $scope.watchOption("maxValue", 100); $scope.watchOption("minValue", 0);}]);
        - Loads the required responsive.coaches module
        - Creates a scope.watchOption for each configuration option that the control must
									keep track of

```
angular
	.module("responsive.coaches")
	.controller("progressBar", ["$scope", "$element", "$timeout","Coach", function 
		($scope, $element, $timeout, Coach)
	{
		"use strict";
		angular.extend($scope, new Coach($scope, $element, $timeout));
		$scope.watchOption("maxValue", 100);
		$scope.watchOption("minValue", 0);
}]);
```

2. Create the debug version of the controller by placing
the controller JavaScript file that you have just created into a folder called scripts. Package the scripts folder into a new compressed
file.  For example, create a new .zip file named customControls.debug.zip and add the scripts/progressBar.controller.js to it.
3. To create the non-debug version of the controller, minimize
the content of the controller file into a compressed JavaScript file.  For example, you can use a tool such as https://developers.google.com/closure/compiler/ to minimize the content of
								progressBar.controller.js into a file that is
							called progressBar.controller.min.js. Pasting the
							content of progressBar.controller.js into http://closure-compiler.appspot.com results in the following
							code:angular.module("responsive.coaches").controller("progressBar",["$scope","$element","$timeout","Coach",function(a,b,c,d){angular.extend(a,new
    d(a,b,c));a.watchOption("maxValue",100);a.watchOption("minValue",0)}]);
4. Place the minimized JavaScript file into a scripts folder.
Package the scripts folder into a compressed
file.  For example, package scripts/progressBar.controller.min.js into the customControls.min.zip file.
5. Upload both the customControls.debug.zip and the customControls.min.zip compressed files
to your toolkit as web files.
4. To preview the coach view in the coach editor, create a
preview JavaScript file
and add code to it that loads the coachViewHelper module, which loads the AngularJS library and all of the required
dependencies. The coachViewHelper also loads
the controller JavaScript file for the progressBar coach view and calls
the wysiwyg.bootstrap function to compile and
load the controller. Note that coachViewHelper is loaded from the Responsive Coaches toolkit (SYSRC), and the controller is loaded from the coach view's toolkit (MYTK).  For example, create a file named progressBar.preview.js and add the
					following code to
					it:var mixObject = {
	createPreview: function(containingDiv, labelText, callback) {
		var \_this = this; 
		\_this.context.previewDiv = containingDiv;
		window.com\_ibm\_bpm\_coach = this.context;
		var helperPath = this.context.getManagedAssetUrl('coachview.helper.min.zip', 
				com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSRC', false, "/scripts/coachViewHelper.js");
		require({async: false}, [helperPath], function(coachViewHelper) {
		if (coachViewHelper.wysiwyg) {
			coachViewHelper.loadResource('customControls.debug.zip', 'MYTK', '/scripts/progressBar.controller.js');
			coachViewHelper.loadResources();
			coachViewHelper.wysiwyg.bootstrap(\_this.context, containingDiv, callback, "responsive.coaches", "progressBar", {Explorer: 9});
	}
		else {
			setTimeout(function() {
		require({async: false}, [helperPath], function(coachViewHelper) {
			coachViewHelper.loadResource('customControls.debug.zip', 'MYTK', '/scripts/progressBar.controller.js');
			coachViewHelper.loadResources();
			coachViewHelper.wysiwyg.bootstrap(\_this.context, containingDiv, callback, "responsive.coaches", "progressBar", {Explorer: 9});
		});
	}, 250);
	}
		});

	},

	propertyChanged: function(propertyName, propertyValue) {
		var \_this = this;
		var helperPath = this.context.getManagedAssetUrl('coachview.helper.min.zip', 
				com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSRC', false, "/scripts/coachViewHelper.js");
		require({async: false}, [helperPath], function(coachViewHelper) {
			coachViewHelper.wysiwyg.propertyChanged(propertyName, propertyValue, \_this.context);
		});
	},

	destroyPreview: function() {
		var \_this = this;
		var helperPath = this.context.getManagedAssetUrl('coachview.helper.min.zip', com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSRC', false, "/scripts/coachViewHelper.js");
		require({async: false}, [helperPath], function(coachViewHelper) {
			coachViewHelper.wysiwyg.destroyPreview(\_this.context.previewDiv);
		});
	}
};
5. Upload the preview file to the toolkit by creating a Web File and selecting the progressBar.preview.js file.
6. Upload the image files for the control by creating a Web File for each image file and selecting the image
files.  For example, upload the progressBar\_palette.PNG and the progressBar\_preview.jpeg files.
progressBar\_palette.png  
progressBar\_preview.jpeg The following
screen capture shows the files that are created and uploaded to the
toolkit for the Progress Bar control:
7 Create the control as a coach view.

1. Create a coach view.  For example, create
the ProgressBar coach view.
2 In the Overview page of the coachview, set the following properties. For example, the progress bar has the followingvalues in its Overview page: Property Value Palette icon progressBar\_palette.png Layout image progressBar\_preview.jpeg Helper JS file progressBar.preview.js HTML snippet file progressBar.html The following screen capture shows what the Overview page looks like for the example ProgressBar control:
    - In the Preview section, set the Palette icon and Layout image to
the appropriate image files that you uploaded as web files.
    - In the Advanced Preview section, set the Helper JS file to the preview JavaScript file that you uploaded.
    - Set the HTML snippet file to the HTML file
that you uploaded.

| Property          | Value                    |
|-------------------|--------------------------|
| Palette icon      | progressBar\_palette.png  |
| Layout image      | progressBar\_preview.jpeg |
| Helper JS file    | progressBar.preview.js   |
| HTML snippet file | progressBar.html         |

<!-- image -->

3. To provide the location of the coach view helper functions,
in the Inline JavaScript area, paste in the following
code, including the comments: /*
@dojoConfigUpdateStart
dojoConfig.packages.push({
name: 'com.ibm.bpm.coach.angular',
location: com\_ibm\_bpm\_coach.getManagedAssetUrl('coachview.helper.min.zip',
com\_ibm\_bpm\_coach.assetType\_WEB, 'SYSRC')
});
@dojoConfigUpdateEnd
*/
4. Add the following AMD dependency to the progressBar coach view: 
Table 1. 

Module ID
Alias

com.ibm.bpm.coach.angular/scripts/coachViewHelper
coachViewHelper
5. Add necessary code to the appropriate event handlers.
Typically, the code that you put in the load event handler is similar
to the code that you put in the progressBar.preview.js file. Specifically, use the coachViewHelper module
to load the resources (such as the controller file) from your toolkit,
and then call the bootstrap function to compile
and load the coach view. Remember to verify that the toolkit acronym
is correct (in this case, MYTK) and that the controller
name matches the name in the controller file (in this case, progressBar). For example, select the load event handler and add the following code to
							it:
							coachViewHelper.loadResource('customControls.debug.zip', 'MYTK', '/scripts/progressBar.controller.js');
coachViewHelper.bootstrap(this, "responsive.coaches",  "progressBar", {Explorer: 9});Select
							the view event handler, and add the following code to
							it to initialize the coach view:
							coachViewHelper.init();Select the
								change event handler, and add the following code
							to it to notify Angular that it needs to redigest the module:
							coachViewHelper.notify(this, event);
6. In the Variables page, add the
binding type for the control and the configuration options.
 For example, for the Progress Bar coach view, add value(Integer) as business
data, and maxValue(Integer) and minValue(Integer) as configuration options.
7 In the Layout page, add two customHTML items to the canvas:

- Set the HTML property of the first custom HTML item to Managed file, and then select the HTML file of the control.
For example, set the HTML property to progressBar.html for the progress bar control.
- Set the HTML property of the second custom HTML item to Managed file, and then select validationAlert.html in the Responsive Coaches (SYSRC) toolkit.
8. Click Save or Finish Editing.

## Results