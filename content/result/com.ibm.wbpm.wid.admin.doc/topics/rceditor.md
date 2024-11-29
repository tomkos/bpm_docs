<!-- image -->

# Component editors and the integration debugger

The integration debugger can be used in conjunction with
the following component editors:

- Business process editor
- Business state machine editor
- Business object map editor
- Business rule set editor and decision table editor
- Visual snippet editor
- Mediation flow editor
- XML map editor

In the component editors, there are several integration debugger
symbols that can appear either before, during, or after a debugging
session. These symbols are described in the following table.

| Symbol   | Description                                                                                                                                 |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------|
|          | The breakpoint is installed and enabled.                                                                                                    |
|          | The breakpoint is installed and disabled.                                                                                                   |
|          | The breakpoint is enabled but restricted to one or more threads of the business process.                                                    |
|          | The breakpoint is enabled in a line of source code in the Java™ snippet editor or the condition editor.                                     |
|          | The breakpoint is enabled in all threads of the component.                                                                                  |
|          | The breakpoint is disabled.                                                                                                                 |
|          | The breakpoint is popped.                                                                                                                   |
|          | In a business process, the link followed if a transition condition evaluates to true. Or, in a mediation flow, the connection that was run. |
|          | In a business process, the link followed if a transition condition evaluates to false.                                                      |
|          | The link followed in a business process if a transition condition is skipped.                                                               |
|          | A condition evaluated to true or an action was run in a business rule set or decision table.                                                |
|          | A condition evaluated to false or an action was not run in a business rule set or decision table.                                           |
|          | An exception was encountered in executing a mediation primitive in a mediation flow.                                                        |