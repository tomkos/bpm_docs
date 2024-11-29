# Example: creating a coach for tablets and smartphones

- For the computer, the inspector can see the entire Inspection Report
coach:
- For the tablet, the inspector can see the Findings part of the coach and the buttons. The
Inspection part of the coach is no longer visible.
- For a smartphone, the buttons stretch across the entire screen to make them easier to
select:

1 Create the Findings CV view. The layout of the view looks like the following screen capture:
    1. Create a view labelled Findings CV.
    2 In the Layout page, add the following views in order from top to bottom: By default, the layout arranges elements vertically so the views are stacked one on top ofthe other.
        - Section
        - Output Text
        - Section
        - Text Area

By default, the layout arranges elements vertically so the views are stacked one on top of
the other.

3. Select the first section and change its Layout configuration to
Horizontal. Repeat this step for the other section.
4. In the first section, add a Single Select view and a Text view. Relabel the Select view to
Building and rename the Text view to Area
inspected.
5. Relabel the Output Text view to Findings.
6. In the second section, add six Check Box views. Relabel the Check Box views to
Overhead,
Electrical, Furniture,
Lighting, Trip, and Other.
7. Relabel the Text Area to Comments.

<!-- image -->

2 Modify the appearance of the view:

1. Select the first section. In the general properties, set the Label
visibility to Hide. Repeat this step for the other section.
2. In the configuration properties of the first section, enable Automatic
Wrap. Repeat this step for the other section. By setting this property, if there is not
enough room to display all of the views side-by-side, the section moves some of them below the
others instead of displaying scroll bars.
3. Select the horizontal section that contains the check boxes. In its configuration options,
enable Style > Show Border.
4. Click Save or Finish Editing.
3 Create the Inspection CV view

1. Create a view labelled Inspection CV.
2 In the Variables page, add the following configuration options: When you create the configuration options, ensure that you set their type to String and Date.
    - inspector(String)
    - inspectionDate(Date)

<!-- image -->

3. In the Layout page, add a Text view and a Date Time Picker view. Relabel
the Text view to Inspector and relabel the Date Time Picker view to
Inspection date.
4. Select the Inspector view and, in its general properties, bind it to the
inspector variable.
5. Click Save or Finish Editing.
4 Create the Inspection client-side human service:

1. Create the client-side human service labelled Inspection.
2. In the client-side human service diagram, rename the coach to Inspection Report.
5 Define the layout of the Inspection Report coach:

1. In the Coaches page, select the Inspection
Report coach and then select to start with a two column grid.
2. Click Grid and then add a single column
grid below two column grid. Click the alignment button in the middle
of the cell to align its contents horizontally.
3. In the two cell grid, drag the border between the two so that
left cell occupies 8 of the 12 columns. The editor displays the columns
when you start dragging the border.
4. Click Content to switch to the content
mode.
5. Drag a section into the first cell and then drag another section
into the second cell. Rename the first section to Findings and the second section to Inspection.
6. Add two buttons to the single cell grid and then drag the OK button
into the cell as well.
7. Rename the first button to Cancel, the
second to Save and OK button to Submit Report.
8. In the Findings section, add the Findings CV view. In the Inspection section, add the Inspection
CV view.
9. Click Save or Finish Editing.
10. Run the Inspection human service. The web browser opens and displays
the coach.
6 Add more space between the Building and Area inspected views. The elements in the Findings viewmust also align with each other.

1. Open the Findings CV view and select the Building view.
2. In the positioning properties, set the padding to 0px 20px 0px 0px. In
the Padding field, the first number is for the top padding, the second number
for the right padding, the third number is for the bottom padding, and the fourth number is for the
padding margin.Alternatively, you can click the  icon beside the Padding field. In the window that opens, type
20px in the Right field and 0px
in the other fields. Click OK.
7 To remove the Inspection section for viewing the coach on a tablet:

1. Open the human service and switch to the medium screen by clicking  on the palette.
2. Click Grid and select the Inspection cell.
In the properties of the cell, set its Visibility to Hide. The palette displays the cell as
an invisible item.
3. Drag the border of the Findings cell so that it occupies the entire
grid.
4. Click Save or Finish Editing.
5. Run the human service again. If the browser is wider than 1024 pixels wide, the Inspection
section is visible. If you reduce the width to 1024 pixels or less, the Inspection section
disappears.
8 To make the buttons easier to use on a smart phone by stretchingthem across the screen:

1. Switch to the small screen by clicking  on the palette.
2. Select the cell that contains the buttons. In the properties of
the cell, set its Orientation to Vertical.
3. Click Save or Finish Editing.
4. Run the human service again. If the browser is less than 640 pixels wide, the buttons are
stacked vertically.