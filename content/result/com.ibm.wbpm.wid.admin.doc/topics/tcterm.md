<!-- image -->

# Terminating component instances in the integration debugger

## About this task

## Procedure

1 If you want to terminate a single component instance andleave its threads visible in the Debug view, complete the followingsteps:
    1. In the Debug view, ensure that the correct stack frame
is selected for the component instance that you want to terminate.
    2. Click the Terminate icon . The component instance terminates and its threads are flagged
with the terminated component thread symbol .
2 If you want to terminate a single component instance andremove its threads from the Debug view, complete the following steps:

1. In the Debug view, ensure that the correct stack frame
is selected for the component instance that you want to terminate.
2. Right-click the selected stack frame and select Terminate
and Remove. The component instance terminates and its
threads are removed from the Debug view.
3 If you want to simultaneously terminate all active componentinstances in the Debug view, complete the following steps:

1. In the Debug view, ensure that a stack frame is selected
for any one of the component instances that you want to terminate.
2. Right-click the selected stack frame and select Terminate
All. All active component instances terminate and their
threads are flagged with the terminated component thread symbol .