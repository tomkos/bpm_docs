# Fan Out mediation primitive properties

## Mode
mode

## Iterate
Expression iterateExpression

When in iterate mode, the
out terminal is fired once for each occurrence of the repeating element that
you specify, using an XPath expression.

For
example, if the body of the SMO contained the following repeating
element /body/input/accounttype[], an input message
might contain the following account types: /body/input/accounttype[0]=gold and /body/input/accounttype[1]=platinum.
If you set the XPath to /body/input/accounttype[],
the out terminal would be fired twice: once
with the FanOutContext containing gold and
once with the FanOutContext containing platinum.
If the input message does not contain any occurrences in the repeating
element, the noOccurrences terminal is fired.

## Batch Count
batchCount

An integer of 0 equates to: Check for asynchronous responses after all messages have been
fired. Therefore, the Fan Out mediation primitive fires all aggregation iterations before
checking for any asynchronous service responses.

An integer of greater than 0 equates to: Check for asynchronous responses after {n}
messages have been fired, where you can specify the value of {n}.
This allows you to specify how many messages should be fired before asynchronous responses are
handled. For example, a count of 1 would fire a single aggregation iteration and all resulting
service responses would be received and processed before starting the next aggregation iteration
(this is the default). The service responses would all be received before starting the next
iteration. A count of 2 means there would be a maximum of two firings of the Fan Out output terminal
before all service responses were collected. If the number of output terminal firings was not an
exact multiple of 2 then any service responses resulting from the final firing would still be
collected and processed as normal.

## Considerations

The Fan Out mediation primitive
has a single promoted property, Batch Count, whose
value you can change from the runtime administrative console.

## Sample XML code

```
<node name="startAggregation" type="FanOut">
  <property name="mode" value="1"/>
  <property name="iterateExpression" value="/attachments"/>
  <inputTerminal/>
  <outputTerminal>
    <wire targetNode="UDDIEndpointLookup"/>
  </outputTerminal>
  <outputTerminal name="noOccurrences"/>
  <failTerminal/>
</node>
```