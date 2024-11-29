<!-- image -->

# Broadcasting messages

## Before you begin

## About this task

<!-- image -->

## Procedure

1. FanOut1 is dropped on the canvas and configured in iterate
mode. The XPath expressions is configured to point to the repeating
element of order items, in this case itemName. The FanOutContext is
of the same type as the repeating element.
2. XSLTransformation1 maps to the message type that the callout
requires by mapping the order item in the FanOutContext to the body
of the target service message object.
3. The output terminal of FanOut1 fires for each order item
in the message, which invokes the callout for each item.