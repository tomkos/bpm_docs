# Example: creating a view using custom HTML

- Add custom HTML code to a view that defines a select view for choosing an account type, such as
Current or Savings.
- Add business objects to the view.
- Configure an event handler (load) with a custom script to bind the select
view selected value to the complex type business object attribute.

1 Add custom HTML code to a view:
    1. In a toolkit or process application, create a new view named
getAccountTypes.
    2. In the Layout page, add a Custom HTML item to the
canvas.
    3. In the properties under HTML, select the Text
option and provide the custom HTML code. For this example, you can use the following code to define
a select view:<select name="AccountType" size="1">
              <option value="Savings">Savings Account</option>
              <option value="Current">Current Account</option>
</select>
    4. On the Overview page, select Can Fire Boundary
Event.
2 Add business objects to the view.

1. In the Variables page, click the plus sign next to Business
Data
2. For the Variable Type, select the TSAPP\_ValidateDocumentCaseProperties
business object.
3. In the Name field, type caseProperties.
3 On the Behavior page, configure the load event handlerwith a custom script for mapping the custom HTML selected value to the business data attribute.

1 Register the Dojo button module and alias that the view will load dynamically.
    1. In the Behavior page, select AMD dependencies.
    2 Click Add and then specify the following information: Tip: This example uses an AMD module that is included in the infrastructure. If theAMD modules are not already included, see Adding custom AMD modules for informationabout how add and then access these modules.
        - In the Module ID column, type dojo/\_base/connect.
This declares a dependency on the module that provides event handling for DOM nodes and related
functionality.
        - In the Alias column, type connect. This is the
alias used in the code to refer to the connect module.
2. Under Event Handlers, select load and then provide
a custom script. For this example, you can use the following script:var selectElement = this.context.element.getElementsByTagName("select")[0];

var onChangeHandle = connect.connect(selectElement, "onchange", this, function(newValue){
if(this.context.binding){
var tempBinding = this.context.binding.get("value");
tempBinding.set("TSAPP\_AccountType", newValue.target.value);
}
});
Table 1. Notes about the script

Item
Description

(this == the view object)
The load event has the context of payload data as well as that of the business
data object associated with it (added in step 2).

connect.connect(selectElement, "onchange"
The onChangeHandle variable in the script has the new value
selected in the Select view. The onChange event of the custom HTML view is called
using connect.connect.
Tip: connect.connect(selectElement, "onchange" is derived from the
alias of the dojo/\_base/connect entry in the AMD dependencies. Therefore, the
script should be modified accordingly based on the alias name. For example, if
myConnect is the alias name, the script would look like
myConnect.connect(selectElement, "onchange".

this.context.binding.get("value").set("TSAPP\_AccountType",
newValue.target.value);
The new value selected in the Select view is bound to the business data
specific attribute (TSAPP\_AccountType).
4 To test your work, create a client-side human service and then do the following:

1. In the Variables page, add
TSAPP\_ValidateDocumentCaseProperties as an output variable.
2. Select the coach page, drag the getAccountTypes view onto the canvas, and
ensure that the TSAPP\_ValidateDocumentCaseProperties private variable was added
as the binding.
3. Click Save or Finish Editing.
4. Run the client-side human service. A browser opens and displays the selection list.

## Reference

| Library item     | Example name                                                                                                                                                                                                                      |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Business Objects | TSAPP\_ValidateDocumentCasePropertiesParameters:	TSAPP\_Zipcode (String)  	TSAPP\_Age (String)  	TSAPP\_AccountStatus (String)  	TSAPP\_CustomerType (String)  	TSAPP\_Name (String)  	TSAPP\_City (String)  	TSAPP\_AccountType (String) |