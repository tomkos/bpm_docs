<!-- image -->

# Debugging mediation flows

1. Start the server in debug mode by selecting Debug from the server's
context menu.
2. Add the projects that you want to debug to the server.
3. Open the mediation flow that you want to debug.
4. Select a mediation primitive that you want the flow execution to pause at, right-click and
select Debug -> Add Breakpoint.
5. If you want to debug within a subflow, you must open the subflow and set a breakpoint on a
mediation primitive in the subflow.
6. Open the assembly diagram and launch the integration test client to test the mediation flow
component.
7. Enter the test data in value editor of the integration test client.
8. Click Continue to start running the test.
9. The flow execution will pause at the first breakpoint. You can inspect the message coming in to
the mediation primitive in the Variables view.
10. When you have inspected the message, you can then step over the primitive or continue the flow
execution until it hits the next breakpoint.