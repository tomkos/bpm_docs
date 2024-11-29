# Adding sections to a heritage coach and controlling the layout (deprecated)

## About this task

The following steps describe how to build a mockup of
a heritage coach that enables personnel in a call center to collect data about customer issues. The
mockup allows you to demonstrate the design to users as you develop a plan for the steps within a
process. You can use feedback from users to refine the design and thus help guarantee that the
eventual implementation meets all requirements.

## Procedure

1. To start developing the mockup, change the title of the heritage coach by clicking the IBM® Business Automation Workflow heritage coach title bar in the design
area.
2. In the heritage coach option of the properties, type Initiate New Case - Enter Customer
Information.
3. Drag a Two-Column section from the palette onto the design
area so that it is positioned directly below the existing Section
Title.
4. Drag four Text controls from the palette onto the design
area so that two Text controls are in each column side by side.
5. Click the Section Title in the design area and in the properties
type Customer Information in the Title text box.
6 Change the text labels for the fields. Clickan Input Text control in the design area and in the properties, changethe Label for each control to match the following list:
    - Name:
    - Phone:
    - Email:
    - Physical address:
7. Right-click the default Checkbox control, and from the
pop-up menu that opens, select Delete. Do the
same for the default Input Text control. Neither of these controls
is needed for this sample Coach.
8. Drag a One-Column with Title section from the palette onto
the design area so that it is positioned directly below the existing
Customer Information section.
9. While the new section is still selected, type Case
Information in the Title text box in the properties.
10. Drag a Text control from the palette onto the design area
and place it in the new Case Information section.
11. While the new Text control is still selected, type Case
Type in the Label text box under the Common section.
Then choose Single Select from the Control
Type field under the Behavior section.
12. Select the Presentation option in the properties and in
the Manual Data section, click the Add button.
13. Add values and display text.  In the Manual
Data section, use the Add button
to add the values and display text shown in Table 1.
Table 1. Values and display
text to add under the Manual Data section

Value
Display text

billing
Billing

defect
Product defect

tracking
Late Shipment
14. Drag a Date Selector component from the palette onto the
design area and place it directly below the drop-down control in the
new Case Information section.
15. In the properties for the Date Selector component, change
the label to Date Received .
16. Click the default Button Group at the bottom of the design
area, click the Presentation option in the properties, and change
the label for the OK button to Submit.
Important: The action associated with any given
button applies only to the fields and other controls in the same section
as the button.
17. Save your work.
18. Click the Preview tab to see how the heritage coach will look when the service runs. You can
make adjustments as you see fit in the Design tab.

Lets change this scenario slightly. In this version a service gets input data at run time which
is used to populate the values of the drop-down list. Since these values are only known at run time,
the values will not appear when you press the Preview tab at development
time. These values will appear in the user interface at run time.

- Setting column widths in a heritage coach (deprecated)

Learn how to change the column width for each section of a heritage coach.
- Setting the number of columns in a heritage coach (deprecated)

Learn how to set the number of columns for each section of a heritage coach.