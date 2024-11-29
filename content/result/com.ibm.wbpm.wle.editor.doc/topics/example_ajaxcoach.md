# Example: creating a coach that calls an Ajax
service

## About this task

In this step-by-step example, you are shown how to create
a coach that calls an Ajax service, create the Ajax service, and create
another coach to display information. It is a complete and self-contained
sample and does not have any prerequisites. The Ajax service examines
a letter. If it sees a Q, it returns the name QuickServ as
the name of the supplier. If it sees a P, it returns
the name ProServ as the name of the supplier. The
second coach displays product information from the supplier selected.

## Procedure

1 Create the heritage human service, the coach that callsan Ajax service, and the Ajax service.
    1. Beside User Interface, click + and
select Heritage Human Service. Name the service Display
Supplier Parts.
    2. Add a Coach to the left side of the canvas. Name the coach
Get Supplier Name. Add a Server Script to the right of
Get Supplier Name. Name the server script List Supplier
Parts. Add another Coach to the right of List Supplier
Parts. Name the Coach Show Parts from Supplier. Save your
work.
    3. Double-click Get Supplier Name. The coach editor opens. Add a
Text field to the canvas. Select the text field and in the
Properties view select the General tab. Change the
Label field to Enter Supplier: Q for QuickServ or P for
ProServ. 

Select the text field and in the Properties view select the
Configuration tab. Select Enable Autocompletion.
Beside Autocompletion Service, click New. The
New Ajax Service window opens. Enter the name Get Supplier
Name for the name of your Ajax service and click Finish. 
Click Variables. Note that the expected input and output variable names
(text and results) and their types have already been
created for you. 
Click Diagram. Add a Server Script to the canvas
and name it Get Supplier Name. Select Get Supplier
Name and click the Implementation tab in the
Properties view. Add the following JavaScript. This code will select the
QuickServ supplier name when Q is entered by a user and select the
ProServ supplier name when P is entered.

tw.local.results = new Array();
if(tw.local.text=="Q"){
    tw.local.results[0]=("QuickServ");
}
else if(tw.local.text=="P"){
    tw.local.results[0]=("ProServ");
}

Connect the Start node to Get Supplier Name and
Get Supplier Name to End. Save your work. Close the
Ajax editor.
 Back in the Get Supplier Name coach, add a Button
beneath the text field. Rename it Next. Save your work. Switch to
Diagram.
2 Create a server script that lists the supplier data.

1. Double-click List Supplier Parts.
In the Properties view, click the Implementation tab
and add the following JavaScript: tw.local.product = new tw.object.listOf.ProductLine();

switch (tw.local.supplier) {
case "QuickServ":
    tw.local.product[0] = new tw.object.ProductLine();
    tw.local.product[0].sku = "Z34RT1GF";
    tw.local.product[0].description = "Window Sill";
    tw.local.product[0].price = "$35.40";
    tw.local.product[1] = new tw.object.ProductLine();
    tw.local.product[1].sku = "YT76UJ8F";
    tw.local.product[1].description = "Glass Pane";
    tw.local.product[1].price = "$37.50";
    break;
case "ProServ":
    tw.local.product[0] = new tw.object.ProductLine();
    tw.local.product[0].sku = "Z34RT1GF";
    tw.local.product[0].description = "Door Latch";
    tw.local.product[0].price = "$20.39";
    tw.local.product[1] = new tw.object.ProductLine();
    tw.local.product[1].sku = "YT76UJ8F";
    tw.local.product[1].description = "Door Bell Chimes";
    tw.local.product[1].price = "$67.50";
}
Click Variables and Add
Private to create a variable for this data. Use private
variables for data that should be hidden. Name the variable product.
Click Is List as the variable will provide
a list of items. Click New to define a business
object that will contain the product data. Enter ProductLine for
the business object name. When the Business Object editor opens, click Add in
the Parameters section and add three variables: sku, description and price.
Leave the type as a String. Save your work. Close the Business Object
editor. Click Add Input to add a variable for
the user's input which will determine the supplier, that is, a Q for
QuickServ or a P for ProServ. Name the input supplier and
leave the type as String. Save your work.
Click Coaches.
Select Get Supplier Name and select the Text field.
In the Properties view, select General.
Beside Binding, click Select and
choose supplier from the menu. Save your work.
The binding in this case associates the input variable in the Human
service with the text element. Save your work.
3 Create a coach to display the supplier data.

1. Click Show Parts from Supplier. In the coach editor, expand
Variables and add product to the canvas. A table with
names taken from the product variable is created. Rename sku to
Stock Keeping Unit. Save your work. Note that you do not need to explicitly
bind the product variable to this coach as it was done for you when you selected product from the
Variables section.
2. Add a Button beneath the table. Rename it Close.
Save your work.
3. Return to the Diagram view and
wire your components together. Using Sequence Flow to
create arrows, wire Start to Get
Supplier Name. Wire Get Supplier Name to List
Supplier Parts. Wire List Supplier Parts to Show
Parts from Supplier. Finally, wire Show Parts
from Supplier to End. Save your
work.
4. Click Save or Finish Editing.
5 Test your human service.

1. Click Run Service in the upper right corner of the
Diagram view. In the first user interface, enter Q or
P. The user interface should complete the supplier name with
QuickServ or ProServ. Click Next.
2. In the next user interface you should see the parts
displayed from either the QuickServ or ProServ supplier. Click Close.