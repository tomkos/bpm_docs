# Service call

Typically, this view uses two variables, one as the input data for the service, and the other as
the results. The input value is passed to and used by the service. The input value is of type
String. The input variable can be bound to another view, such as a Text view, to
allow the user to enter data manually. However, data binding is not required for the Service call
view to work.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

| Appearance configuration property   | Description                                                                                      | Data type   |
|-------------------------------------|--------------------------------------------------------------------------------------------------|-------------|
| Busy indicator                      | Displays the Busy icon that indicates that the service call is running. None Spinner Refresh Cog | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                         | Data type    |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Called service                    | Specifies the service flow with Ajax access that is called when the Service call view runs. It takes input value as an argument for the service flow, and outputs the result as the data that is bound to the view. | AJAX Service |
| Input value                       | Specifies the input value for the service flow with Ajax access. When Auto run is selected, changes to this value automatically start the service flow with the updated input.                                      | ANY          |
| Auto run                          | Runs the service flow with Ajax access on start and whenever the input data is changed.                                                                                                                             | Boolean      |

## Example

- A client-side human service that contains a UI page.
- Inside the page:
    - A Panel view named Service call Example that contains two Text views, one
called Name and the other called Result.
    - A Service call view that uses two variables:
        - An input variable of type string called data, which is bound
to the Behavior > Input value option of the Service call view. To allow the user to enter data in the text field,
data is also bound to the Name text view.
        - An output variable of type string called results, which is
bound to both the Result Text view and Service call view in their General > Behavior sections.
- A service flow with Ajax access, named Called Service Flow , which has thesame variables as the Service call view and contains a server script. Tip: The easiestway to create the service flow with the same variables as the Service call view is to clickNew next to Called service in the Configuration > Behavior section of the Service call view. Complete the wizard to create the service flow andthen configure its properties as follows.

- In the Overview tab, under Ajax Access,
Allow calls from all users is selected.
- In the Variables tab, the service flow has the same variables,
data (string) and results
(string).
- In the Diagram tab, select the script node and then, in the script
properties, under Script, add the following
logic:java.lang.Thread.sleep(1000);

if(tw.local.data !=null){
    var data = tw.local.data + "";
    if(data.length > 0)
    {
        tw.local.results = "Hello " + tw.local.data;
    }
}Line 1 adds a delay of one second (1000 ms) that allows the
Busy indicator cog to display spinning. The rest of the script checks if
there is input data added to the service. If input data is provided, the script adds the result
"Hello " to the input data.

- Under Configuration > Behavior, Called service is set to Called Service
Flow.
- Input value is set to data (string).
- Auto run is selected.
- Under Configuration > Appearance, Busy indicator is set to Cog.

- Before adding input data, the result is a panel that contains two empty text fields,
Name and Result. The Busy
indicator icon in the form of a cog spins in the bottom left corner to show that the
human service is running.
- When input data is added to the Name text field, for example,
Bill, after the cog stops spinning, the Result field
displays the text Hello Bill.

## Events

The user does not interact with the Service call view, but rather the events are activated when
the user gets a result or error from the service flow call.

- On load: Activated when the page loads. For
example:me.execute(${Data1}.getValue())
- On invoked: Activated when the service is invoked. For
example:${SvcButton}.setEnabled(false);
- On before result: Activated when the service with Ajax access returns a
result, but before the result is processed to allow for data augmentation. For
example:alert("Service call returned: " + data.results);
- On result: Activated when the service returns a result. For
example:alert("Service call returns " + me.getResult() );Tip:  Using .items to access date properties may
return values with an incorrect type. For example, dates can be represented as strings instead of
JavaScript Date objects. Use .toJSObject() or .get(index) to
access the list properties.
- On error: Activated when the service returns an error. For the error to be
returned, an AjaxError object should be used as an output variable inside the
service. The output variable can be used in conjunction with an error intermediate event to catch
any errors and set the AjaxError object accordingly. For
example:alert("Service error: " + me.getLastError().errorText)

## Methods

For detailed information on the available methods for the Service call view, see the Service call JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.