<!-- image -->

# Java expressions

## Questions and answers about Java expressions

This section contains some questions and answers about the use
of Java expressions in the test data table of the test suite editor.

Question: Why is there a null value for a variable used
in a Java expression?

Answer: The variable is not being
initialized in the request message because it is not being used in
an invocation. You must use the variable in a test step in order for
it to be initialized correctly, such as an Invocation, Wait on, or
Wait step.

1. Send a request for a new customer ID.
2. Receive a response with the new customer ID.
3. Send a new request using the customer ID received in step 2.

Answer: Yes, this
is a typical way to reuse the variables in the test data table. In
this scenario, the customer ID is expressed as an expected variable
in the test data table and the variable can be used in a subsequent
request.

Question: I have a returned response that contains
a Customer ID value. I want to populate an input parameter of a new
request with the Customer ID. I assume that this requires a Java expression
in the new request to populate a value with the Customer ID value
of the initial response, but it is not obvious how to use a Java expression
to accomplish this task. The test data table defines the response
as a DOM Document type and there does not seem to be a simple way
to write a single Java expression to obtain a reference to the Customer
ID that is contained in one of the nodes in the DOM Document. Is there
any way to accomplish this with a Java expression?

Answer: Yes. There is a utility class named com.ibm.wbit.comptest.ctnative.runtime.utils.DOMHelper
that is used internally to extract the values in a DOM Document type
object. You can use the utility method getSelectedNode(target, xpathExpr,
nsInfo) to extract the field that you want to reference in your other
variables. In your scenario, the target will return your DOM Document
object and the xpathExpr will be the XPath to the Customer ID value.
The nsInfo is not relevant in your scenario and you can simply set
it to null. The following code fragment shows how to use the utility
class:

```
DOMHelper.getSelectedNode(responseDocument,
"soap:Envelope/soap:Body/ns5:operation1/input1/field1", null)
```

Note that the namespace prefix in your XPath must match the namespace
prefix in your response message. To use the helper class, you need
to import it into your test suite using the Import page in the Test
Data Table view. You can simply switch to the Import page and add
the DOMHelper class in the list. This enables you to reference the
utility class in your variables using the Java Expression format.

Alternatively, you can also create a utility method yourself that
takes a DOM Document type as a parameter to extract the value that
you want and save your Java class in your component test project.
You can then switch to the Import page in the Test Data Table view
and add your custom Java class in the list. Now you can reference
your Java class in your variables using the Java expression format.

Question: I notice that DOMHelper.getSelectedNode returns
a Java object. Does the object represent the String value of the element
value or is it a node from which I need to extract the String? For
example, assume that the message looks like the following code fragment:

```
<soap:Envelope>
  <soap:Body>
    <ns5:operation1>
       <input1>
          <field1>hello world</field>
```

Does the
call to DOMHelper.getSelectedNode return a Java object that I can
cast to a String that contains "hello world"? Or is it a node object
of some type that I need to perform a further operation on?

Answer: It either returns a String or a DOM Node. In your
example, it returns the "hello world"  string and it will return a
Node type if the node does not  have a text value (such as input1 in your example). If you want to get the "hello
world" string, you actually need to append "/text()" at the end of
your XPath. Otherwise, you will get the DOM Node type instead. Similarly,
if the field you want to extract is an attribute, you will need to
insert "@" before the node name in your XPath.

Question: What do I do if I need multiple Java expressions to determine if
a test passed?

1. Create a Java class in the test project (if you want, it can be
in a new Java package).
2. Create a public static method that returns a boolean that will
perform the verification logic.
3. Typically, the logic will need the variable from the data table,
so the method argument will usually be a DataObject.
4. Write the verification logic.
5. In the test data table, right-click the variable and select Add Operator > Condition.
6. Edit the expression so that it calls your test method.

```
myVar:MyVar
-- myData:MyData
----data1:String
----data2:String
```

1. In a Component Test project, create a class mytestpackage.Tester:package mytestpackage;

import commonj.sdo.DataObject;

public class Tester {
    public static boolean checkValues(DataObject dObj) {
        boolean isPassed = true;
        System.out.println("Checking values");
        String d1 = dObj.getDataObject("myData").getString("data1");
        String d2 = dObj.getDataObject("myData").getString("data2");
        if (d1.startsWith("a123"))
        {
            if (s.equals("b456")) isPassed = true;
            else isPassed = false;
        }
        return isPassed
    }
}
2. Save the class and ensure there are no compile errors.
3. In the test data table, right click the myVar variable and select Add Operation -> Condition.
4. Edit the condition (default is the expression, true), so that
it calls Tester. mytestpackage.Tester.checkValues(myVar)

Question: How can I determine if an array
has the required number of elements?

1. In the data table, under bo1, right-click bo2 and select Add Operator > Condition.
2. Click the expected cell to put it in edit mode, and then change
the value null to bo1.getList("bo2").size() == 5.
3. Optional: Enter expected values for the fields of up to five bo2
elements. Checking the values of nested array data can be done in
addition to setting a condition on the size of the array.