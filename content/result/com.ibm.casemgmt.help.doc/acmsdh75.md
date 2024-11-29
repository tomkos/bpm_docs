# Activities that start processes

You specify that a process activity is required for the case to complete or that it is optional.
You also specify whether the activity is started manually, automatically, or when a user adds the
activity in Case Client.

You can hide activities from view in the case client. For example, if you have activities that
have no value to the case worker, you can mark those activities as hidden when you design your
solution. Typically, hidden activities are controlled programmatically through business logic that
is built into the case management application.

You can mark an activity to repeat when there is a property change or when there is a
document filing precondition defined for the activity. An activity that is marked as repeatable can occur
multiple times during the lifetime of the case in which it resides and can cause new activities to be
created and repeated. Activity types can be restarted as needed to repeat, even if the activity is already
in complete state.

You can group predefined activities by sets: all-inclusive or mutually exclusive. Adding
activities to an all-inclusive set means that all activities in that set must be completed. Adding
activities to a mutually exclusive set means that if you start one activity in the set, you cannot
start any of the others. An activity can be included in only one set type. An activity that is
included in a set must have a
precondition.

To simplify a workflow, you can break a large activity into smaller, more manageable activities. For
example, one activity might be to process a loan request. You might break this large activity into separate
activities for assembling the loan documents, reviewing the documents, and accepting or rejecting the
request.

## Required activities

Activities that you make required for the case can be started automatically or manually as soon
as the case is created or after preconditions are met for the activity. For example, if the solution
that you are designing is for credit card disputes and one of the case types is for claims with
supporting documentation, you can create a required activity for a claim review as soon as
supporting documentation for a claim is added to the repository.

## Optional activities

Activities that you make optional for the case can be started automatically, or manually as soon
as the case is created or after preconditions are met for the activity. For example, if the solution
that you are designing is for automobile claims and one of the case types is for automobile
accidents, you can create an optional activity that can be manually started for the rental car
activity. Optional activities are displayed second on the Activities page.

## Discretionary activities

Activities that you make discretionary can be added by case workers as needed after a case is
created. For example, if the solution that you are designing is for automobile claims and one of the
case types is for automobile accidents, you can create a discretionary activity to request that a
field agent investigate the accident that is submitted by an insurance adjuster for possible fraud.
Discretionary activities are displayed last in the Activities page.

## Container activities

You can define activities that contain other activities called subactivities. Container
activities can start automatically, manually, or discretionary. Subactivities are created after the
container activity starts. The subactivities within a container activity cannot be discretionary.
They can be only automatic or manual.

- One subactivity for notifying the customer of the loan approval.
- One subactivity for providing the funds to the loan applicant.

If your administrator configured access to a business process management system, you can place
the workflow subactivities inside of container activities.

## Subactivities

The subactivities that you create within a container activity are created in Case Client only after the container
activity that they are in moves to working state. You cannot mark subactivities as discretionary.
However, you can move subactivities out of a container activity and then mark them as
discretionary.

## Tips for using activities that start processes

- Ensure automatic activities in a all-inclusive or mutually exclusive set don't rely on the same
precondition to start the activity.
- For automatic activities in a mutually exclusive set, don't satisfy the preconditions in the
same Save action from Case Client. For example, in Case Builder
you might define automatic activity2 to start on p2=2 and automatic activity3 to start when p3=3 and
configure them to be part of a mutually exclusive set. Then, in Case Client, if you make an update such as
p2=2 and p3=3 and save these changes together, the system becomes confused about which activity to
start among mutually exclusive activities because the precondition for both activities is satisfied
in same Save action. In this scenario, you will see the following
errors:[10/30/19 6:44:31:528 PDT] 00000a10 SystemOut     O CIWEB.ICMAPIPlugin Error: [deadmin @ 9.102.30.84] com.ibm.ecm.extension.icm.services.impl.CaseService.execute()
com.filenet.api.exception.EngineRuntimeException: FNRCE0066E: E\_UNEXPECTED\_EXCEPTION: An unexpected exception occurred. failedBatchItem=0 errorStack={
        at com.ibm.casemgmt.intgimpl.eventhandler.CaseEventHandler.onEvent(CaseEventHandler.java:101)
        at com.filenet.engine.handlers.EventActionWrapper.onEvent(EventActionWrapper.java:60)
        at com.filenet.engine.queueitem.SubscriptionProcessor.execute(SubscriptionProcessor.java:1254)
        at com.filenet.engine.queueitem.SubscriptionProcessor.fireOrQueue(SubscriptionProcessor.java:1071)
        at com.filenet.engine.queueitem.SubscriptionProcessor.processEvent(SubscriptionProcessor.java:999)
        at com.filenet.engine.queueitem.SubscriptionProcessor.processEvents(SubscriptionProcessor.java:908)
        at com.filenet.engine.queueitem.SubscriptionProcessor.fetchActionAndProcessEvents(SubscriptionProcessor.java:885)

Caused by: com.filenet.api.exception.EngineRuntimeException: FNRCE0066E: E\_UNEXPECTED\_EXCEPTION: An unexpected exception occurred. Message was: FNRPE0001E: [ILLEGAL\_DISABLED\_TASK\_CHANGE\_STATE\_OPERATION]: Change State operations are not allowed for disabled Tasks. failedBatchItem=0
        at com.ibm.casemgmt.intgimpl.eventhandler.TaskEventHandler.onEvent(TaskEventHandler.java:108)
        at com.filenet.engine.handlers.EventActionWrapper.onEvent(EventActionWrapper.java:60)
        at com.filenet.engine.queueitem.SubscriptionProcessor.execute(SubscriptionProcessor.java:1254)
        at com.filenet.engine.queueitem.SubscriptionProcessor.fireOrQueue(SubscriptionProcessor.java:1071)
        at com.filenet.engine.queueitem.SubscriptionProcessor.processEvent(SubscriptionProcessor.java:999)
        at com.filenet.engine.queueitem.SubscriptionProcessor.processEvents(SubscriptionProcessor.java:908)
        at com.filenet.engine.queueitem.SubscriptionProcessor.fetchActionAndProcessEvents(SubscriptionProcessor.java:885)
        at com.filenet.engine.queueitem.SubscriptionProcessor.postProcessSubscriptions(SubscriptionProcessor.java:631)
        at com.filenet.engine.persist.SubscribablePersister.postExecuteChange(SubscribablePersister.java:375)
        at com.filenet.engine.persist.ReplicablePersister.postExecuteChange(ReplicablePersister.java:130)