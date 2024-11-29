# Using a default human service page layout

## Before you begin

## About this task

A page contains the user interface elements that are required to complete an
activity. Case Builder provides
different default page layouts for an action, for example, Add Case that is
widget-based and Add Case Default (Human Service) that is human
service-based. Set your default page layouts to human service-based pages.

The new human service page is hosted in Case Client in the Case
Details adapter page. See Adapter pages.  The case toolbar
widget displays the toolbar, and the client-side human service viewer displays the human service.
After you create your case page, you can
test it in the development environment, then deploy your case solution to a production
environment.

<!-- image -->

## Procedure

To create a case page using the default human service page layout:

1. Open your case solution and case type.
2. Under Case Type, change the default widget-based Case
Details page layout to Case Details Default (Human
Service).
3. Deploy and run the case solution, which takes you to the Case Client. The user you're
logged in as must be in the role associated with the case solution. Otherwise, ask your
administrator to add the user to the role.
4. From the Cases page, add a case to the
solution.
5. From the cases list, open the case that you have just added. Your case page
might look similar to the following example,

where area 1 is the toolbar that contains the header and some default buttons, and area 2 is an
iFrame that includes human service views that are laid out as tabs (similar to the layout of a
process instance).