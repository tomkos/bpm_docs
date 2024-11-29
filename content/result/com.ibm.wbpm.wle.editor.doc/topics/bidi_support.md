# Bidirectional support in Process Designer

- If the direction of the window is right to left, its elements
are logically ordered from right to left and from top to bottom.
- Within a right-to-left window, the default direction of entry
fields is right to left, but entry fields that are to receive English
text or numeric input must be defined as having a left-to-right direction.
- Within the same window, text and graphics can have different directions.

- Contextual typing
- Layout transformation in Process Designer
- Islamic (Hijri) and Hebrew calendar support

When you are creating user interfaces in Process Designer, you can choose an
Islamic or Hebrew calendar. See Date Time Picker control.

- Applying bidirectional text layout transformation

Business Automation Workflow provides bidirectional (bidi) text layout options for process applications. Bidirectional text layout transformation can be applied to any string variable (either input or output) as part of the preprocessing, postprocessing, or implementation of a service. Typically, bidirectional text layout transformations are required for conversion of bidi textual data stored in databases to a Logical LTR format that is assumed by the Business Automation Workflow user interface, but can be used for other purposes.