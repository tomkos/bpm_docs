<!-- image -->

# Specifying human task emulation values in the integration test
client

## Before you begin

- "Adding human task emulators"
- "Specifying a wait time for human task claims"
- "Specifying a potential owner for a human task"

## About this task

## Procedure

1. Launch the integration test client from the business process
that contains your human task.
2. In the Component field of the Events
page, select the name of your component that runs the human task.
3. In the value editor, specify an initial request parameter
value in the Value column.
4. Click the Continue icon . A Claim event is generated into the Events
area when the human task is run.
5. In the Events area, ensure that the Claim event
is selected.
6. In the value editor, specify output parameter values for
your human task emulator.
7. Click the Continue icon . A Return event is generated into the
Events area and the return parameter values are displayed in the value
editor.

## What to do next