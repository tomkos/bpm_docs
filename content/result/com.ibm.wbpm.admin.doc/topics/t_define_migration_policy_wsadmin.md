# Defining the instance migration policy by using a wsadmin command

## Procedure

1. Run the BPMCheckOrphanTokens wsadmin command. For more information about the
BPMCheckOrphanTokens command, see BPMCheckOrphanTokens wsadmin command.
A policy file is generated that shows the orphaned activities (steps).
2. Review the instance migration policy file to determine if changes are needed.
By default, orphaned activities have a step element added to the file with the delete
operation set for each step element. Therefore, if no step elements are in the file, there are no
orphaned activities. Do not modify the process, step, and other parent XML elements. For each step,
a delete XML element is added, for example <delete suspendProcess="false"/>.
Tip: For advice and considerations regarding moving or deleting tokens, see Managing tokens.
3. To move orphaned tokens, change the delete XML element to a move element, as shown in the
Results section.
The move element requires two string attributes: name and
targetStepId. Use the name and
targetStepId associated with the activity you want to move the orphaned token
to. You can get these values from IBM® Process
Designer. In Process Designer, open the target
snapshot and corresponding process. Then, select the target activity for the token and open the
Properties view for it. In the General tab of the Properties view, you will
find the name to use for the name attribute, and in the
Documentation tab of the Properties view you will find the ID to use for the
targetStepId attribute of the move element. The attributes are case
sensitive.
4. Optional: 
You can suspend the process instance after an orphaned token has been
deleted or moved so you can edit the data before resuming the instance. To suspend the process,
change the suspendProcess attribute from false to true.

## Results

```
<?xml version="1.0" encoding="UTF-8"?>
<orphanTokenPolicy>
  <processApplication acronym="HSS" id="2066.9ab0d0c6-d92c-4355-9ed5-d8a05acdc4b0" name="Hiring Sample">
    <sourceSnapshot acronym="RHS8570" id="2064.f1659d94-2365-4903-8a90-9fa62f3ccd31" name="Responsive Hiring Sample v8570\_01"/>
    <targetSnapshot acronym="OTT" id="2064.b15dcea3-1e3f-4721-9a6c-b3f23046f68c" name="Ophaned Token Test"/>
    <process bpdId="25.c904b3b1-afc1-4698-bf5a-a20892c20275" name="Standard HR Open New Position">
      <step id="bpdid:431b0753c33842e2:3d5457c0:141a2fd3448:-75fb" name="Submit position request">
        <move name="User Task" suspendProcess="true" targetStepId="e78fd2f7-c441-4011-8a42-ae339bf3f581"/>
      </step>
      <step id="bpdid:431b0753c33842e2:3d5457c0:141a2fd3448:-7576" name="Send escalation notice">
        <delete suspendProcess="false"/>
      </step>
    </process>
  </processApplication>
</orphanTokenPolicy>
```

## What to do next