# Debug actions in the Inspector

The actions that are available in the Inspector depend
on the state of the element you selected.

The following table
lists the debug actions that you can take on an element that you are
debugging.

| Action                      | Description                                                                                                                                                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step over                   | Move the execution to the next step in the flow.                                                                                                                                                                         |
| Step into                   | Stop the execution on a breakpoint before the step is run.                                                                                                                                                               |
| Show window                 | Open the debugger browser window, or bring it to the front. The debug runtime requires a browser window to be open during the debug session. If you accidentally close the window, you can re open it using this action. |
| Refresh                     | Refresh the content of the flow with the latest updates.                                                                                                                                                                 |
| Terminate                   | Cancel the current debugging session before the flow reaches the end.                                                                                                                                                    |
| Run                         | Run to completion. Available for flows other than client-side human services, such as heritage human services.                                                                                                           |
| Run and stop on breakpoint. | Run until an enabled breakpoint is encountered or the flow terminates. Available for client-side human services and service flows.                                                                                       |