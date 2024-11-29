# Adding case widgets to a client-side human service page

## Before you begin

- Start with a case solution that has the required roles, case types, and properties. See Adding a solution.
- Ensure that you already have a client-side human service case page in your case solution, which
you created by using a custom page layout. See Creating a custom page.

## About this task

You can continue to use your favorite widgets with your human service page so that they are
displayed together in Case Client. After you create the case layout for your adapter page, you can edit it in Page Designer and add
your widgets to it. See Adapter pages.

A case layout page that you construct is based on the following elements.

<!-- image -->

## Procedure

To add widgets to the case layout, follow these steps.

1. Open your case solution and case type.
2. Go to the Views tab for the case type.
3. Under Case Layouts, find the layout for your case adapter page
that you created earlier.
4. Click the layout to open it in Page Designer. The page opens showing a
Client-Side Human Service Viewer widget.
5. Drag your widgets onto the page and arrange them the way that you want.
6. Deploy and run the case solution, which takes you to the Case Client. The user you're
logged in as must be in the role that is associated with the case solution. Otherwise, ask your
administrator to add the user to the role.
7. From the Cases page, add a case to the
solution.
8. From the cases list, open the case that you added earlier. Your case page
might look similar to the following example,

 where area 1 is the widget toolbar that contains the header and some default buttons, area 2 is
an iFrame that includes human service-based views in a custom arrangement, some laid out as tabs
(similar to the layout of a process instance), and area 3 is another case widget.