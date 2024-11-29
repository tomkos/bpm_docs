# Binding a variable to a custom HTML component in a heritage
coach (deprecated)

## About this task

## Procedure

1. Open the service that contains the heritage coach that
you want to work with and then click the Coaches tab.
2. Drag a Custom HTML control from the palette onto the design
area.
3. While the Custom HTML control is selected, click the Presentation
option in the properties.
4. In the HTML text box, type the variable
whose value will populate the HTML block at run time. In
this example, tw.local.myHTMLBlock is declared in
the Variables tab for the service and then used to set the label of
the HTML block at run time. Type the following in the HTML text box: <p><#=tw.local.myHTMLBlock#><p> .
5. To render the content in the HTML block, run the service. 
When you run the service, the variable is evaluated and its
runtime value is then passed to the heritage coach. For a quick test,
define a default value for the variable from the Variables tab.
Select the variable and then, under the Default Value section,
click Has Default. When Has Default is
selected and the default value is added to the field, which is This
is the default value that can be used to test the Coach.
The heritage coach displays the runtime content of the
HTML.