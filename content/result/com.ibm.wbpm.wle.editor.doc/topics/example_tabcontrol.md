# Example: creating a tabbed coach (deprecated)

In this example, you have a Customer business object that contains many
properties. To capture or display all of these properties within a single coach, the Tab view is a
good choice.

<!-- image -->

<!-- image -->

<!-- image -->

1 Create the Customer business object. Customer hasid(String) , firstName(String) , andlastName(String) parameters. It also has two complex parameters:phoneNumbers(PhoneNumber) and addresses(Address) . With the Customer business object, addresses is an array of theAddress type, so ensure that you select List forit. For information about creating business objects, see Creating business objects .
    - PhoneNumber is a business object that has home(String),
work(String), and cell(String) parameters.
    - Address is a business object that has number(String),
street(String), and city(String) parameters.

With the Customer business object, addresses is an array of the
Address type, so ensure that you select List for
it.

<!-- image -->

2 Create the view for the PhoneNumber business object:

1. Create the PhoneNumberView view.
2. In its Variables page, add a variable named
phoneNumber and set its type to the PhoneNumber business
object.
3. In the Layout page, add the home, work,
and cell parameter variables onto the layout. A Text view is added to the layout
for each variable because it is the view associated with the String type.
3. Create a client-side human service named Customer Human Service.
4. In the human service diagram, rename the coach to Customer Coach.
5. In the Variables page, add the Customer business object as a private
variable.
6. Go to the Coaches page and start with a default coach.
7. In the Coaches page, delete the default OK button
and add a Tabs view to the Customer Coach layout.
8 Create the General page:

1. Add a section to the Tabs view. A tabbed page can contain only one element directly. By adding
the section, you can then add as many elements as you want into that section.
2. Rename the section to General. The name that you see on the tab comes
from the label of the section.
3. Drag the id variable onto the section. The id variable is a
parameter of the Customer business object.
4. Drag another section into the first section below the id text view. In
the configuration options of the second section, change its layout to
Horizontal.
5. Drag the firstName and lastName variables onto the horizontal
section.The Id, firstName, and lastName
variables are parameters of the Customer variable.
9 Create the Phone Numbers page:

1. Drag the PhoneNumberView view onto the + part of the tab view. If you did not
add a tag to the view, you can find it in the NoTags category on the palette.
You can see a PhoneNumberView tab in the tab view.
2. Bind the PhoneNumberView view to the customer.phoneNumbers
variable. This action means that any data users enter into the fields gets set in the variable for
the heritage human service.
3. Select the tab.
4. In the General properties, change the label of the
PhoneNumberView instance to Phone Numbers.
10 Create the Addresses page:

1. Drag the addresses variable onto the tab view. You can see an
Addresses tab in the tab view. If you select the tab, can now see a table
with a column for each property defined in the Address business object.
2. In the Configuration properties, select Show Add Button and
Show Delete Button. By doing this step, you can add and subtract address rows
when you run the heritage human service later in this example.
11. Add a button view below the tab section and relabel it to OK, The button
broadcasts a boundary event and you can use it to wire the coach in the heritage human service
flow.
12. In the diagram, connect the start node to Customer Coach and then connect Customer Coach to the
end node.
13. Click Save or Finish Editing.
14. Test the client-side human service by clicking the  button.