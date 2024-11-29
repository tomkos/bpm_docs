<!-- image -->

# Example: Changing the values of a relationship instance

## About this task

## Procedure

1. Open the administrative console.
2. If security is enabled, log in as a user with administrator
privileges.
3. In the navigation pane, click Integration
Applications > Relationship Manager.
4. Open the relationships page for the server you want to
manage. Click Relationships next
to that relationship services MBean.A relationship
named SampleCustID should be visible.
5. Select SampleCustID, then click Query.
6 Locate the relationship instance for the customer This locates the relationship instance for the requestedcustomer and opens the Relationship Instances page.
    1. Click the query By role tab
    2. In the Role name field, select MyGLCustomer\_0 from
the drop-down list.
    3. In the Value field under Key
attributes, enter901
    4. Click OK

This locates the relationship instance for the requested
customer and opens the Relationship Instances page.

7. Click the relationship instance ID. This
displays the relationship instance data for customer ID 901 in the
GL application, including all the associated role instances.
8. In the MyGLCustomer\_0 role table, select the role instance ID with the key attribute
value 901, then click Delete. 
Note: It should not have any property values associated with it. If any other data
appears, you need to look at the role instance and record any data you want to keep.
9. Click Create to open the New
Role Instance page for creating a new role instance for
this relationship instance.
10. Enter 801 in the Value field
under Key attributes, then click OK.
The new role instance is saved, and you should see
a new role instance in the table.

## Results