<!-- image -->

# Changing the format of mediation flows

## About this task

When you import a mediation flow that was created in a
previous version of IBM Integration Designer, the old format is maintained.
When you save the mediation flow, you are prompted to save the mediation
flow in the new format.

## Procedure

You can also convert your mediation flows from the Business
Integration view, by following these steps:

1. Select the projects that contain the mediation flows that
you want to convert.
2. Right-click and select Convert mediation flow
format.

## Results

- If you saved your mediation flow in a single file (this is the
default), it is saved in a file with a .mfc extension
- If you saved your mediation flow into multiple files to facilitate
team development, in addition to an .mfc file, an .mfcflow file is
created for each operation.
- For each mediation subflow, a file with the extension .subflow
is created.

- Mediation flow schema reference

Mediation flows have an XML schema format that is useful for developers who want to create patterns.