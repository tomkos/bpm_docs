<!-- image -->

# Breakpoints in the integration debugger

In the integration debugger, you can set breakpoints on one or
more elements of a component. You can also set breakpoints in the
source code of Java snippets and conditions. When
a component thread pauses at a breakpoint, you can control program
flow or alter the state of the running component.

Depending on the kind of component that you are debugging, you
can set a breakpoint, entry breakpoint, or exit breakpoint on a component
element. If you set an entry breakpoint on an element, the breakpoint
will pop before the element is invoked. If you set an exit
breakpoint on an element, the breakpoint will pop after the
element is invoked.

The effectiveness of a breakpoint in stopping code execution when
it is reached depends on whether it is enabled or disabled. An enabled
breakpoint causes normal code execution to stop and the integration
debugger to be invoked if an attempt is made to invoke the instruction
at the location of the breakpoint. By comparison, a disabled breakpoint
will not stop code execution.

If you are debugging a business process, a breakpoint that is set
in a process will automatically be set in all instances of the process.
If you create new instances of the process, they will inherit all
of the breakpoints. However, you can choose to restrict a breakpoint
to one or more specific threads of a process. Any breakpoint that
is removed from a process is also automatically removed from all other
instances of the process.

In the Debug perspective, you can work with breakpoints in both
the component editors and the Breakpoints view. The elements that
you can set breakpoints on are listed in the following table:

| Component editor                                   | Business integration components   |  Elements that you can set breakpoints on           |
|----------------------------------------------------|-----------------------------------|-----------------------------------------------------|
| Business process editor                            | Business processes                | Activities, Java snippets                           |
| Business state machine editor                      | State machines                    | States                                              |
| Business object map editor                         | Business object data maps         | Transformations, Java snippets                      |
| Business rule set editor                           | Rule sets                         | Rules, templates, conditions, actions               |
| Decision table editor                              | Decision tables                   | Conditions, actions, values, terms                  |
| Visual snippet editor                              | Visual snippets                   | Nodes, custom visual snippets, Java visual snippets |
| Mediation flow editor and mediation subflow editor | Mediation flows                   | Mediation primitives, nodes                         |
| XML map editor                                     | XML maps                          | Transformations                                     |

Note that when you use the Refactor menu
item to change a component, all breakpoints associated with the component
are either automatically modified or deleted. Also, if you change
a component file outside of the IBM® Integration
Designer environment,
any associated breakpoints may also be modified or deleted automatically.