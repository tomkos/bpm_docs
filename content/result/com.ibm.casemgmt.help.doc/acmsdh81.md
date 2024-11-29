# Business objects

- To be able to reference a specific instance of the business object, you select one of the
business object properties as a title. In the example business object, Insured Party, you select the
ID property as the title because it is the one property that uniquely identifies the person.
- To use the business object in a solution, you must create a multivalued case property that is
assigned the business object as its data type. For the example business object, Insured Party, you
then can create a case property, Insured Parties, and assign this property a type of Insured Party.
A case worker then can enter information for each person in the Insured Parties table.

If you have business objects that have several properties in common, you can create a parent
business object that contains all the common properties. You then create subclasses to contain the
unique properties for each business object. For example, you might have business objects for
different types of insurance policies. Some properties apply to all policy types, such as policy ID,
customer ID, and agent. However, each policy type has unique properties. In this situation, you can
create a parent business object, Policy Object, that is assigned all the common properties. You then
define subclasses for Policy Object and assign these subclasses the unique properties. The
subclasses inherit all the properties that are assigned to the parent.

| Business object        | Parent        | Properties                                                                                                                                                |
|------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Policy Object          | None          | Policy ID  Customer ID  Agent                                                                                                                             |
| Vehicle Policy Object  | Policy Object | Policy ID (inherited from parent) Customer ID (inherited from parent) Agent (inherited from parent) Vehicle Type  Vehicle Make  Vehicle Model  Vehicle ID |
| Property Policy Object | Policy Object | Policy ID (inherited from parent) Customer ID (inherited from parent) Agent (inherited from parent) Property Type  Street Address  City  State            |

In this example, you can set the title to Policy ID on the Policy Object parent. The children
inherit the title unless you choose to override it by selecting a different property.

Because the Policy Object object does not contain complete information for a policy, you do not
want to use this object as a case property type. To prevent users from selecting the Policy Object
object as a case property type, select the Do not use this business object as a property
type check box for this object. Then, the child business objects show in the list, but
the Policy Object object does not.