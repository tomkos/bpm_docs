# Building an Ajax service with heritage coaches (deprecated)

## Procedure

The first part of this procedure takes you through the
steps of creating an Ajax service. Subsequent steps describe how to
associate this service with a coach in order to populate fields in
a user interface or form.

1. In the left hand navigation, hover over the Implementation
category, and click the plus (+) sign. Select Ajax Service.
2. Name your new service. For example, if you were building
a form for users to look up product information based on a supplier
name, you might have a service called "Query Product Line".
3. With the new service open in the diagram editor, drag a
Server Script component from the palette, and use sequence lines to
connect the script to the Start and End Events.
4. Declare the variables to pass into and out of your service
in the Variables tab. For example
if you were planning to use the service to accept the name of a supplier,
and return a set of product information, you might create an input
variable called "Supplier" of type string and an output variable called
"ProductInfo". Because the product information is complex, you can
create a new business object called "ProductLine" which contains fields
for product SKU, description, and price. For more information
on how to create variables see Declaring and passing variables and Creating business objects.Tip: For
this example, because you are expecting multiple products to be returned,
be sure to enable the Is List check box for
the ProductInfo output variable. Also For the Supplier variable,
ensure that the Has Default check box is enabled.
5. Click the Diagram tab and then click the Server Script
component in the diagram.
6. In the Implementation properties, enter the script for
the Ajax service to run. In the example described above, you might
have the following script using the specified variables sku , description ,
and price for two different suppliers: QuickServ and ProServ.
tw.local.ProductInfo=new tw.object.listOf.ProductLine();

switch(tw.local.Supplier)
{
case "QuickServ":
tw.local.ProductInfo[0] = new tw.object.ProductLine();
tw.local.ProductInfo[0].sku = "Z34RT1GF";
tw.local.ProductInfo[0].description = "PowerServ 1500";
tw.local.ProductInfo[0].price = 3540;
tw.local.ProductInfo[1] = new tw.object.ProductLine();
tw.local.ProductInfo[1].sku = "YT76UJ8F";
tw.local.ProductInfo[1].description = "PowerServ 1735";
tw.local.ProductInfo[1].price = 3750;
break;
case "ProServ":
tw.local.ProductInfo[0] = new tw.object.ProductLine();
tw.local.ProductInfo[0].sku = "Z34RT1GF";
tw.local.ProductInfo[0].description = "Reliant DW";
tw.local.ProductInfo[0].price = 2039;
tw.local.ProductInfo[1] = new tw.object.ProductLine();
tw.local.ProductInfo[1].sku = "YT76UJ8F";
tw.local.ProductInfo[1].description = "Reliant X1";
tw.local.ProductInfo[1].price = 6750;
}
7. Save your work.

Now you need to associate the Ajax service you just created
with a Human Service containing a coach.

1. Create a new Human service or open an existing one. To
continue with the example above, you could create a Human Service
named Select Supplier .
2. Drag a Coach from the palette to the service diagram and
then use sequence lines to connect the Coach to the Start and End
Events.
3. Add variables to your new Human Service. Click the Variables tab
and add a private variable named product of type ProductLine .
Enable the Is List and Has Default check
boxes for the product variable.
4. Click the Coaches tab and then drag a Text control from
the palette to the Coach editor.
5. Click the Input Text control in the Coach editor to select
it and then click the Input Text option in the properties.
Change the Label field for this control to Supplier:.
6. Drag the product variable from the palette
to the Coach editor. This automatically creates a
table control.
7. Click the table control in the Coach editor to select it.
8. Click the Presentation option in
the properties for the table control and in the Dynamic
Data section, select Ajax Service .
9. From the Choose Control as Input drop-down list, select Supplier
(Input Text) .
10. Click the Select button and choose
the Query Product Lines Ajax service.
11. Save your work.
12. Click the Run Service button in
the upper right corner. The Coach runs in a browser and when you provide
one of the Supplier names included in the Ajax script (QuickServ or ProServ),
the Coach displays the information for that supplier. If
the supplier information does not immediately display, reload the
browser page.