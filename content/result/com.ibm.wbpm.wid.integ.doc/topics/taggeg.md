<!-- image -->

# Example: Fan Out and Fan In

## About this task

<!-- image -->

The service
request that is input into the mediation flow contains data for field1. This
data is passed to another service that populates field2 with data based on
the value of field1. This is done iteratively for all data elements in the
array, and the result is returned back to the service requester.

Lets
assume that there are two data elements (myBOs) in the array that is input
into the mediation flow, as shown in the xml below:

```
<?xml version="1.0" encoding="UTF-8"?>
<ns0:inputArray xmlns:ns0="http://TestLib/ArrayInterface" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <myBos>
    <field1>049</field1>
    <field2></field2>
  </myBos>
  <myBos>
    <field1>077</field1>
    <field2></field2>
  </myBos>
</ns0:inputArray>
```

<!-- image -->

These are
the steps in the mediation flow:

## Procedure

1. The user sets MyBoArray to be the shared context in the properties
page of the input node.
2 The user sets the Fan Out primitive to fire the output operationfor each element in the XPath expression /body/operation1/inputArray/myBos.The Fan Out primitive performs the following actions:
    1. Populates the iteration count in the Fan Out primitive context
with the element count of 2.
    2. Copies the first array element from the message body to the
Fan Out context
    3. Fires the output terminal with the Fan Out context containing
the first element, which has 049 as the value of field1
3. The interface of the service invoked by the service invoke primitive
takes a business object, MyBo as input. In XSLT1, the user defines a map between
the element from the Fan Out context to the elements of MyBo in the input
message body.
4. Service Invoke calls out to the service and puts the response in
the output message body.
5. In XSLT2, the user defines a mapping between the response from
the output message body and the shared context business object that was set
in step 1.
6 The Fan in primitive is the decision point in the flow. Becausethe count of two has not been reached, the mediation flow tracks back to FanOut1.

1. FanOut1 copies the second array element from the message body
to the Fan Out context
2. Fires the output terminal with the Fan Out context containing
the second element, which has 077 as the value of field1
3. Steps 3 - 6 are repeated. All the elements in the array are
now populated with data in the shared context.
4. Because the count of two has been reached, Fan In fires its
output terminal.
7. In XSLT3, the user defines a map between the elements of the shared
context business object to the input message body.