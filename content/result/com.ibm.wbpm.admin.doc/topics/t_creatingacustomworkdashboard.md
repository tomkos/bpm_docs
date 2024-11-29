# Creating a custom dashboard

## About this task

## Procedure

1. Add a dependency on the Dashboard toolkit and other toolkits
that contain resources that your dashboard uses. For information,
see Managing toolkit dependencies. The Dashboard toolkit
contains coach views and other resources that you can use to create
a dashboard.
2. Create the human service that users monitor and interact
with through a dashboard. For information, see Building a heritage human service.
3. In the Overview page of the human
service, set the Expose To field to a team
whose members can view and use the dashboard. Set the Exposed
As field to Dashboard. For
information, see Exposing heritage human services.
4. Optional: Set the label that Process PortalProcess Portal displays for the
dashboard name. If you do not set the label, Process Portal uses the name of the
human service as the label.For information, see Globalizing dashboard names.
5. Create the user interface for the dashboard by using one
or more coaches. For information, see Building coaches. The coaches typically contain one of
more coach views. These coach views can be stock or responsive controls, controls from the Dashboard
toolkit, or custom coach views. For information about creating coach views, see Developing reusable views.Tip: Process Portal has a control that you
can use to set the current page as the start page in the contents area. When you are designing the layout to the coach, ensure that you compensate for the location
of this control. For example, move a coach view so that it is not overlapped by the control by using
a CSS rule to create a margin or add padding.
6 Within your custom dashboard, if you want the controlsin the Dashboard toolkit to navigate to within your custom dashboard,create a custom Navigation Controller. Add the custom Navigation Controllerto your custom dashboard. Tip: Some of thecontrols require that the Navigation Controller control is availablein the dashboard. For information, see the documentation for individualcontrols in Controls in the Dashboards toolkit . Tocreate a custom Navigation Controller, complete the following steps:
    1. Copy the Navigation Controller in the Dashboards toolkit
to your process application or to a toolkit that your process application
has a dependency on.
    2. Open the Behavior page of the copy
and select the load event handler.
    3 Edit the topic.subscribe callback functionso that it constructs the correct URL for the target dashboard. Youcan accomplish this goal by using utilities.generateCustomDashboardURL= function(/*string*/type, /*string*/appName, /*string*/serviceName,/*object*/params, /*string, optional*/ snapshotName) . For example, var urlType = null;if ((!!(window.parent)) &&(window != window.parent)) { // In Heritage Process Portal urlType = utilities.constants.PORTAL\_DASHBOARD\_URL\_TYPE; } else { // Not in Heritage Process Portal urlType = utilities.constants.SERVICE\_URL\_TYPE; }var targetLocation = utilities.generateCustomDashboardURL(urlType, "MyApp", MyHumanService", params)console.log(targetLocation); The params canbe constructed from the published event. It has the following format:params = { "tw.local.param01":"data" "tw.local.param02":"data2"} The URL that is created for navigation differs dependingon where the user sees the dashboard:

```
var urlType = null;
if ((!!(window.parent)) &&(window != window.parent)) { 
	// In Heritage Process Portal 
	urlType = utilities.constants.PORTAL\_DASHBOARD\_URL\_TYPE; 
} else { 	
	// Not in Heritage Process Portal 
	urlType = utilities.constants.SERVICE\_URL\_TYPE; 
}
var targetLocation = utilities.generateCustomDashboardURL(urlType, "MyApp", MyHumanService", params)
console.log(targetLocation);
```

```
params = {
	"tw.local.param01":"data"
	"tw.local.param02":"data2"
}
```

        - If the user sees the dashboard in Process Portal, the format of the URL
is
/dashboards/{PROCESS\_APP\_NAME}/{HUMAN\_SERVICE\_NAME}
followed by additional parameters to pass to the human service of the dashboard. For example, to
pass the process application ID, the URL is
/dashboards/{PROCESS\_APP\_NAME}/{HUMAN\_SERVICE\_NAME}?tw.local.processAppId=myProcessID.
        - If the user sees the dashboard in Process Designer or in a custom
portal, the format of the URL is /teamworks/executeServiceByName?processApp={PROCESS\_APP\_NAME}&serviceName={HUMAN\_SERVICE\_NAME} followed
by additional parameters to pass to the human service of the dashboard.
7. In any custom coach view that needs to perform dashboard
navigation, publish the event to the topic that the Navigation Controller
subscribes to. The callback function constructs the payload
for the event.For example, the Process Summary coach
view in the Dashboards toolkit has the following callback:this.doNavigationCallback = function \_doNavigationCallback\_ProcessSummary(evt){
	try{
		var data = (!! this.context.binding) ?  this.context.binding.get("value") : null;
		if(data!=null && typeof(data.processId)!="undefined" && data.processId!=""){
			var params = {};
			params[dutils.constants.DASHBOARD\_NAVIGATION\_SOURCE] = "ProcessSummary";
			params[dutils.constants.DASHBOARD\_NAVIGATION\_DESTINATION] = dutils.constants.PROCESS\_PERFORMANCE\_SERVICE;
			params[dutils.constants.PROCESS\_ID\_PARAMETER] = data.processId;
			topic.publish(dutils.constants.DASHBOARD\_NAVIGATION\_TOPIC, params);
		}
	} catch (e) {
		console.error(e);
	}
};In this case, the payload is:"sourceControl":"ProcessSummary", 
"destinationService":"Process+Performance",
"tw.local.processAppId":"myProcessID"
For more examples, see the Navigation Controller and
the coach views in the Dashboards toolkit.