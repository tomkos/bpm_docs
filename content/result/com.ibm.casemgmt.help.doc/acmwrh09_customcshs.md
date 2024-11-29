# Creating a custom case page using human services

## Before you begin

## About this task

A page contains the user interface elements that are required to complete an
activity. Case Builder provides
different default page layouts for an action, for example, Add Case that is
widget-based and Add Case Default (Human Service) that is human
service-based. Set your default page layouts to human service-based pages.

The new human service page is hosted in Case Client in the Case
Details adapter page. See Adapter pages. The case toolbar widget
displays the toolbar, and the client-side human service viewer displays the human service, which you
edit to create your custom page. After you create your case page, you can
test it in the development environment, then deploy your case solution to a production
environment.

<!-- image -->

## Procedure

To create a custom human service case page layout:

1. Open your case solution and case type.
2. Under Case Type, click the New Case Details
layout link.
3. In the Views tab of your case solution, under Case
Layouts, enter a name and define the layout for the new human service custom
page. Notice that an adapter page is chosen by default. You can edit this adapter page if
you want to combine human service views with widgets.
4. Click OK to save the new custom human service page. The
new page is now listed in the Views tab. This page is an editable copy of the
default page.
5 Customize your new case layout as needed:
    1. Click the case layout name. The client-side human service editor opens in
Workflow Designer.
    2. In the editor, click Coach and select Case
Details to open your page. You're now seeing the coach layout that shows UI
elements (views) and tabs for Overview, Properties,
Documents, Activities, History,
and Tasks.
    3. Customize the layout by moving, arranging, and adding views as needed. See
Views in the Case toolkit.
    4. You must add the required case properties to the Properties
tab. All the case properties that you create are stored in the caseProperties
content object. Under Drag a component to your page, click
All views > Variables, then
drag the required properties onto the drop zone in the Case Properties
view.
6. Deploy and run the case solution, which takes you to the Case Client. The user you're
logged in as must be in the role associated with the case solution. Otherwise, ask your
administrator to add the user to the role.
7. From the Cases page, add a case to the
solution.
8. Open the case that you have just added. Your case page, which opens in
Case Client using the custom
layout that you created, might look similar to the following example,

where area 1 is the toolbar that contains the header and some default buttons, and area
2 is an iFrame that includes client-side human service-based views that are laid out as tabs
(similar to the layout of a process instance).For more information about views, see
Views in the Case toolkit.