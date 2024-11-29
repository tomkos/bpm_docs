# Building coaches

## About this task

In the first stage of designing a coach, your goal might be to build a mock-up. The mock-up
contains static elements to visualize what data the coach needs at run time and where the coach
displays the data in its layout. After you complete the first stage to design the look of the coach,
you then feed real business data to the views in the coach. This step
requires you to create bindings between the views and the data structures (variables) that represent
the business data in your workflows. Your business users can then interact with the business data,
which helps them make the appropriate decisions.

## Procedure

Building a coach is often an iterative process in which you loop back to refine the
coach as you build it. Although you can complete some of the steps in any order, in general you take
the following steps:

1 Create one or more mock-ups for the coach. Use the mock-ups to identify elements that arecommon with other coaches. Identify the following information: You can then use this information to decide which parts of the coach you canimplement as reusable views. For example, after you create the mock-up, you see that your coachcontains two sets of identical address fields. Instead of creating the two sets of address fields inthe coach, you create one address field view. You can then use the view for both sets of addressfields.
    - The elements that are reusable
    - The best layout for the user interface elements in the coach
2. If there are toolkits that contain artifacts that your coach can
use, add a dependency to these toolkits. These artifacts include business objects, views, and files.
The dependency is to a particular snapshot of the toolkit. If you are revising an existing coach,
you can upgrade the dependency to a different snapshot of the toolkit. The upgrade is optional. If
you do not do the upgrade, the coach continues to use the existing dependency.  
Tip: Earlier process applications
have a default dependency on the Coaches toolkit (deprecated). Newer process
applications
have a default dependency on the UI toolkit.
3. If the views that your coach will use do not exist, create them. For information, see
Developing reusable views.
4. In the human service diagram, add the coach to the diagram and then double-click it to
edit it.
5 Add views or variables onto the layout of the coach.These can be the views that you created earlier. The variables are business objects and their parameters are defined forthe human service. For variables, the designer puts the view that is associated with the businessobject or parameter type onto the layout. For example, if you add a variable that is of the Stringtype, the designer puts a text view that is bound to the variable. If the variable type does nothave an associated view, the designer puts a placeholder message on the layout instead. You can thenuse the placeholder to specify the binding between the variable and a view. Important:

- Uninitialized variables that are bound to any view are automatically initialized to default
values that are appropriate for the variable type (for example, String--""
empty string, integer--0,
boolean--false, complex object--{}
empty object). Note that if the coach optimization is enabled,
initialization changes to formerly uninitialized variables that receive an explicit default value
when the coach is loaded are not sent back for processing unless the changes are made by the user.
For more information about improving performance by enabling the coach optimization, see Enabling optimization for coaches.
- For correct coach modeling, it is recommended that you
do not rely on the coach initialization of variables. Instead, you should explicitly initialize all
the variables that are bound to the coaches to the appropriate default values. Alternatively, you
can make adjustments for the fact that variables might not be initialized after the coach step in
the human service.
6. To lay out content in the coach, use the grid to specify cells. Each cell provides a
location on the coach to display its contents. For information, see Laying out a coach or view using the grid layout.
For example, you have views that display metadata and views that display a form. You can create a
cell on the left to display the form views and a cell on the right to display the metadata views.
Use the content mode to add the appropriate views to the cells.
7. To edit the view instances, select them and then change their properties.  
For example, for text fields and buttons, change the label to something useful for users. Many views
contain configuration options that you can set for each instance. You can also override the styling
of the view instances by adding CSS classes and attributes as HTML properties. These CSS classes are
defined elsewhere such as in the view definition in a CSS file uploaded as an included
script.
8. If the views support having different types of visibility, define their visibility. For
information, see Setting the visibility of views. 
Important: You can set the visibility of the views. Custom views might not provide you
with this functionality. If a custom view does not support setting visibility, contact the developer
of the view to add support for this functionality.
9. Wire the coach in the human service diagram by connecting boundary events that the views
fire to the appropriate elements.
10. If needed, validate the data in the coach.  For information about validating
coaches in client-sided human services, see Validating coach data without exiting a coach and Validating coach data after exiting a coach. For
information about validating coaches in heritage human services (deprecated), see Validating coaches in heritage human services.
11. Click Save or Finish Editing.
12. Click Run
 to run the
service.
13. Review the coach and update the views it contains until the coach
looks and behaves as you intended.