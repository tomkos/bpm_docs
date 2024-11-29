<!-- image -->

# Editing the test configuration

## About this task

- Adding modules

You can add one or more modules to the test configuration in the test suite editor. This enables you to use the test configuration to test the added modules and their components.
- Removing modules

You can remove one or more modules from the test configuration in the test suite editor. This enables you to more easily manage the remaining modules.
- Adding component or reference emulators

You can add one or more component or reference emulators to a module in the test configuration in the test suite editor. This enables you to emulate references, components, or imports in your module.
- Adding human task emulators

You can add one or more inline or standalone human task emulators to a test configuration module in the test suite editor. This enables you to programmatically emulate human tasks with different outputs and automatically claim and complete the tasks in the test client rather than claiming and completing them manually in the Business Process Choreographer Explorer.
- Emulating components and references when invoking one-way operations

When a component test invokes a one-way interface operation, the test will immediately complete and be marked as "passed". This is because there is no actual response to verify as having passed or failed. As a result, any emulators defined in the configuration (or any emulator definition tasks defined in the test case) will not run.
- Specifying a wait time for human task claims

You can choose to have a human task claimed immediately or you can specify an amount of time in milliseconds that you want to wait before a human task is claimed.
- Specifying a potential owner for a human task

You can choose to specify the user ID and password of the potential owner that you want to use to claim a human task. If you do not specify a user ID and password, the user ID and password used to log in to the server will also be used for the potential owner.
- Defining emulators as programmatic

When you first add an emulator to a test configuration module in the test suite editor, it is automatically disabled. However, you can choose to define the emulator as programmatic, which enables you to automatically and programmatically specify response values for the emulator using a programmatic emulation file.
- Creating programmatic emulation files

You can create one or more programmatic emulation files for use with a programmatic emulator in the test suite editor. This enables you to supplement existing programmatic emulation files with new programmatic emulation files that are customized for specific test purposes.
- Editing programmatic emulation files

You can edit any programmatic emulation file that you want to use with a programmatic emulator in the test suite editor. This enables you to define an implementation file for a new programmatic emulator or redefine the implementation file for an existing programmatic emulator.
- Disabling emulators

You can disable one or more emulators. This enables you to prevent an emulator from emulating a component, reference, or human task.
- Removing emulators

You can remove one or more emulators from a module in the test configuration in the test suite editor. This enables you to more easily manage the remaining emulators.
- Deleting programmatic emulation files

You can delete one or more programmatic emulation files. This enables you to more easily manage the remaining programmatic emulation files in the test suite editor.
- Adding monitors

You can add one or more monitors to a module in the test configuration in the test suite editor. This enables you to monitor a specific module wire or export for requests, responses, or both.
- Editing monitors

You can edit a monitor for a module in the test configuration in the test suite editor. This enables you to select whether a specific wire or export in a module is monitored for requests, responses, or both.
- Removing monitors

You can remove one or more monitors from a module in the test configuration in the test suite editor. This enables you to more easily manage the remaining monitors.
- Adding fine-grained traces

You can add one or more fine-grained traces to a module in the test configuration that is open in the test suite editor. This enables you to specify fine-grained traces for supported components and trace the event path through the components during a test. Currently, the components with fine-grained trace support are business processes, state machines, and mediation flows.
- Editing fine-grained traces

You can edit a fine-grained trace for a module in the test configuration that is open in the test suite editor. This enables you to select and track component variables and display them in the value editor of the test client when the fine-grained trace is generated. If you do not select any variables, the fine-grained trace will still be generated, but the variables will not be tracked and displayed in the value editor.
- Removing fine-grained traces

You can remove fine-grained traces from a module in the test configuration that is open in the test suite editor. This enables you to more easily manage the remaining fine-grained traces.