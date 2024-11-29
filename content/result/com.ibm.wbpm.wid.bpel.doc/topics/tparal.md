<!-- image -->

# Working with parallel activities

## About this task

You can create a parallel process as follows:

## Procedure

1. Drop a parallel activity onto the canvas.
2. Populate the parallel activity with the activities required
to create the parallel flow.
3 Link them up as follows:
    1. Hover your mouse pointer over the source activity until
a yellow circle appears below it as shown in the image . Click the yellow circle,
and drag the link to the source activity and release the mouse button.
Alternatively you can right-click an activity and select Add
link from the menu.
    2. Create the necessary links between each of the nested
activities. When you are done, there should be a clear control path
through the activities.
4 Create any necessary conditions as follows:

1. Click the link to highlight it.
2. In the Details page of the properties
area, click Create a new condition.
3. Configure the condition using the settings on this page.
You can use a Simple expression language
(True, False, or Otherwise) or program the condition using either Java or XPath.
If you choose Java™, you can
use the snippet editor to visually compose the code, or enter it directly
into the Java editor yourself.
Note: The
simple expression language is far more limited than XPath or Java, but if the condition you are
trying to express can be expressed using the simple language then
it is recommended to do so.

## Example

<!-- image -->

- on outgoing gateways all links are followed if their evaluation
condition is true,
- on incoming gateways the process waits for all incoming links
before proceeding.

## Related tasks

- Working with structured activities
- Linking activities within parallel and generalized flow activities