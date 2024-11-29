# Example: showing the label of a complex view

When you add simple views to a page or to another view, you automatically see their label at
design time and at run time. This is not the case for complex views, which contain multiple views.
When you add complex views to a parent view or page, there is nowhere to show their labels by
default. However, you can still show their labels by using the label general
configuration option.

In this example, you create the My Complex CV view with two text views and a
text area view. You then modify it so that you can see its label at run time. The example uses a
client-side human service and views.

1. Create a view that is called My Complex CV and add two text views and a
text area view to it. You can use default values for the views.
2. Create a client-side human service that is called My Human Service.
3. Open the page and add My Complex CV to it. The view label is not visible at
design time or run time.
4 To make the view label visible at design time:
    1. Open the My Complex CV view.
    2. In the Overview page, select Supports
a Label.
    3. Click Save or Finish Editing.
    4. If you open the page in the human service, the view label is now visible.
5 To make the label visible at run time:

1. Open the My Complex CV view.
2. In its layout, add an output text view.
3. In the General properties of the output text view, click  for the Label field and then clickSelect. In
the window that opens, expand General Options and then select
@label (String).Using the label of the output text to display the view name means that, at run time, the
name is styled as a label. If you instead set the binding to display the view, at run time, the name
is styled as normal text.
4. In the Visibility properties of the output text
view, click  for the Visibility field and then
clickSelect. In the window that opens, expand General
Options and then select @labelVisibility (String).
5. Click Save or Finish Editing.
6 Test that you have bound the view label:

1. Open My Human Service and open My Coach.
2. Change the label of My Complex CV to My Complex CV
Label.
3. Click Save or Finish Editing.
4. Run the human service. My Complex CV now shows the label that you gave it in
My Coach. The view label is now visible both at design time and at run time.