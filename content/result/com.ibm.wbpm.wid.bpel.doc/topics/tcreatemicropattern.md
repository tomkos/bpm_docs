<!-- image -->

# Creating a micropattern

## About this task

## Procedure

To create a micropattern, complete the following steps:

1. Open your BPEL process in the Business Integration view.
2. Select the activities in the process that you want to create
a micropattern from.
3. With your cursor on the assembly canvas, right-click and
then click Micropatterns > Create Micro-patterns.  The New BPEL Process Micropattern wizard opens.
4. Specify the name and description of the micropattern, and
the library in which it will be stored, and then click Next.
5. In Target Properties, select the
activities in the micropattern that will become target properties.
A target property is a specific function of an activity to which substitution
parameters are applied. The Define pattern parameters
and map them to target properties window of the New BPEL Process Micropattern wizard opens.
6 A point of variability is a variable that substitutesitself into your micropattern for a target property that you selectedin step 5. To define and map a point of variability, complete thefollowing steps:
    1. In the  Step 2: Define pattern parameters pane
of this window, click Add to add a variable.
    2. In the Step 3: Map pattern parameters to target properties
pane of this window, select a target property and then click Replace.
    3. In the Substitute Target Property Value window, enter the name of the target property that is to be
replaced with the variable that you defined in step 5a and then click OK.
7. Click Finish.