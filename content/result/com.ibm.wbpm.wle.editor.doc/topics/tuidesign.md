# Creating user interfaces

Client-side human services provide a lightweight alternative to the earlier
human services, which are referred to as heritage human services and are deprecated. For more
information, see Client-side human services and Difference between client-side human services and heritage human services.

Human services are self-contained, independently deployable units of user interface that use
coaches to build the web pages that users see. Coaches comprise user interface elements called
views. You can create and use views to build a coach, then use the coach as part of a client-side
human service to build the user interface that you need. For information, see Coaches and Views.

- A task completion UI implements a specific activity in a process or case instance. It has access
to the details of the instance.
- A dashboard is a stand-alone user interface that users can run at any time. Users can access
dashboards through Process Portal, a case solution, or a custom UI.
- A startable service can be started at any time through Process Portal, a case solution, or a custom UI.
- A URL service creates a stand-alone UI that can be called directly through a URL.
- An instance UI can be an instance details UI or a launch UI. You can create custom instance UIs
and reuse them.

Reusable coaches and views can be saved to toolkits, which are libraries that can be shared
across applications. For example, the UI toolkit provides a rich set of out-of-the-box views that
you can use to create custom views from scratch or by aggregating other views. See UI toolkit.

Client-side human services can also contain scripts, other embedded client-side human services,
and service calls to other services. For more information, see Modeling client-side human services.

- Which artifacts should I use?

You can use a number of different artifacts to create or modify a user interface. These artifacts consist of client-side human services, heritage human services (deprecated), responsive coaches and coach views (deprecated), and UI views.
- User interface concepts

People interact with process applications through user interfaces, which you can create using a number of artifacts.
- Modeling client-side human services

When you model a client-side human service, define the activities, dashboards, or instance user interfaces that case workers or people who participate in processes use in Process Portal.
- Building coaches

You can build a coach for a user interface page that enables business users to interact with a service.
- Developing reusable views

To contain functions or user interface elements that another view or page can use, create a view.
- Laying out a page or view using the grid layout

You can layout a page or view by using cells in a grid.
- Tips for debugging view lifecycle method inside client-side human services

To debug your views inside a client-side human service, you need to use the debugging features of your browser along with the debugging features of the inspector view.
- Tips for debugging views in Process Portal

You can debug the lifecycle method for your views in Process Portal.
- Enabling JavaScript debugging for coaches

 Traditional: 
For debugging purposes, you can set your coaches and views to use the readable versions of Dojo and the Coach framework JavaScript.
- Accessing coach performance statistics

As you develop and test your user interface pages, you can access statistical data that helps you evaluate coaches and ensure an optimal user interface performance.
- Enabling optimization for coaches

 Traditional: 
To improve performance by reducing the amount of data that is sent back to the human service and the processing time, optimization for coaches can be enabled. By default, the optimization is turned off. If required, you can enable the coach optimization by adding a new custom property in the administrative console.
- Troubleshooting user interfaces

The following sections list issues that you might encounter and information about possible solutions.
- Responsive settings for views

At run time, users can interact with your process application interfaces by using a range of devices, each of which have their own characteristics, such as screen size and standard user-interface conventions.
- Coach and view examples

This section includes some examples that demonstrate how to create and code the various parts of coaches and views.
- Localizing process applications

Localizing your process applications enables users in different language locales to interact with the  interfaces in their own languages. In addition to providing translated versions of your process applications for business users, you can also specify localized strings for your design-time users, for example, users that are creating their own interfaces using custom views that you provide.
- Creating and updating themes

 Traditional: 
You can create a theme to provide common styling to a set of views. You can update the theme of a running process application without having to redeploy the process application.
- Conversion of deprecated functions in imported process applications and toolkits

To prepare a process application to be deployed to multiple device types, ensure that its artifacts and the artifacts in its corresponding toolkit dependencies are suitable for use on both mobile and desktop devices.
- Re-creating heritage human services as client-side human services in the Process Designer

To gain the improved performance of a client-side human service and use its responsive features, you can convert a heritage human service (deprecated) into a client-side human service. The conversion might require you to re-create some of the human service logic in the Process Designer.
- Building heritage human services (deprecated)

Build a heritage human service when you want an activity in your process or business process definition (BPD) to create an interactive task that process participants can perform in a web-based user interface.
- Building heritage coaches (deprecated)

When you build heritage human services (deprecated), you can use heritage coaches, which provide the interfaces for end-user interaction.