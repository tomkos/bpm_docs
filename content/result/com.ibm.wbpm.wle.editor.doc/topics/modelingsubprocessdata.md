# Declaring variables for a subprocess

## Before you begin

Variables declared in a subprocess are not tracked by the Business Performance Data
Warehouse.

## Procedure

1. Open your subprocess or event subprocess by double-clicking the activity in the parent
process.
2. Go to the Variables tab.
The input and output variables declared in the top-level process are visible, as are any
private variables declared in the parent process. You can access these variables from within your
subprocess or event subprocess, passing values between any subprocess activities that might require
them. For example, if you are modeling the Get Customer Order subprocess of a larger Customer Order
Handling process, you might need to access the Customer Account variable that is declared in the
parent process.
3. Create private variables for any data that is used only within the context of the
subprocess or event subprocess and any subprocesses it contains. For example, the Get Customer Order
subprocess might need to use a private variable that is used to authenticate the customer service
representative onto the ordering system. This data is not needed outside of this part of the larger
Customer Order Handling process, so it is a private variable that is visible only within the
subprocess and its contained subprocesses. 
Note: Variable names declared in a subprocess or event subprocess cannot be the same as variable
names declared in its parent process. If there are multiple layers of embedding, with subprocesses
contained within other subprocesses, variable names must be unique throughout the entire subprocess
hierarchy. In addition, if you specify an alias to use for business data in Process Portal searches, this
alias must be unique within the top-level process and across all subprocesses and event subprocesses
under the same top-level parent.
4. Click Save or Finish Editing.

## What to do next

Now that you have declared your private variables, activities within your subprocess or event
subprocess can use these variables to capture business data. To pass data between the activities
inside your subprocess, you need to map the input and output data required for these activities. For
more information about mapping input and output data, see Mapping input and output data for an activity or step.