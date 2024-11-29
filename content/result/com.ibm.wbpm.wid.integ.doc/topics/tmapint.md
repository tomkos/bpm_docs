<!-- image -->

# Mapping interfaces in mediation flows

## Before you begin

## About this task

## Procedure

1. In the overview page of the mediation flow editor, click
the source operation that you want to map.
2. In the template selection window that appears, choose Operation
Map.
3. Select the target interface and operation, and click OK.
4. A request flow opens, showing a wired flow that has an
input node for the source operation, a callout for the target, and
an XSLT mediation primitive to map between the two.
5. Click the XSLT mediation primitive and click Finish in
the New XML Map wizard.
6. Map the source and target elements in the map editor and
save your changes.
7. If the source operation is a request response operation,
a response flow is also created to process the message that is returned
by the target operation. Complete the response flow using the procedure
described in the previous steps.