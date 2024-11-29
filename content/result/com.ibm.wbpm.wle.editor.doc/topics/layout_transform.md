# Applying bidirectional text layout transformation

## About this task

Complete the following steps for bidi text layout transformation:

## Procedure

1. From the palette, add a server script to a service, such
as a heritage human service. Note: This transformation
can be performed from any server-side service. To perform a text layout
transformation in a client-side human service, include a call to a
server-side service, such as an integration service, from within your
client-side human service flow.
2. In the Variables tab for the service,
add an input string variable for the string to be transformed.
3. In the Diagram tab, select the server
script.
4 In the Implementation tab of theProperties view, enter the script for calling the bidi engine to implementthe transform. For example:tw.local.Var = tw.system.bidiTransformation(tw.local.Var,"input\_bidi\_format", "outputBidiFormat", symmetricSwapping) where tw.local.Var1 isthe string to be transformed.The input BidiFormat andoutput BidiFormat can have the following values: In the following example, a logical left-to-rightstring is transformed to LRTL - logical right-to-left and the Booleanvalue isSymmetricSwapping is set to true : tw.local.Var1= tw.system.bidiTransformation(tw.local.Var1,"LLTR", "LRTL", true)

```
tw.local.Var = tw.system.bidiTransformation(tw.local.Var,"input\_bidi\_format", "outputBidiFormat", symmetricSwapping)
```

    - LLTR - logical left-to-right
    - LRTL - logical right-to-left
    - LCLR - logical contextual left-to-right
    - LCRL - logical contextual right-to-left
    - VLTR - visual left-to-right
    - VRTL - visual right-to-left
    - VCLR - visual contextual left-to-right
    - VCRL - visual contextual right-to-left

tw.local.Var1
= tw.system.bidiTransformation(tw.local.Var1,"LLTR", "LRTL", true)

5. Click Save or Finish Editing.

## What to do next