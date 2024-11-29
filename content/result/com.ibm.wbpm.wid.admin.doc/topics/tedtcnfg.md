<!-- image -->

# Editing test configurations

## About this task

- Adding modules to a test configuration

You can add one or more modules to any test configuration that is open in the integration test client. This enables you to use the test configuration to test the added modules and their components.
- Removing modules from a test configuration

You can remove one or more modules from any test configuration that is open in the integration test client. This enables you to more easily manage the remaining modules. However, you cannot remove a module from a test configuration if it is the only module in the test configuration.
- Adding component or reference emulators to a test configuration module

You can add one or more component or reference emulators to a module in any test configuration that is open in the integration test client. This enables you to emulate references, components, or imports in your module.
- Adding human task emulators

You can add one or more inline or standalone human task emulators to a test configuration module in the integration test client. This enables you to programmatically emulate human tasks with different outputs and automatically claim and complete the tasks in the test client rather than claiming and completing them manually in the Business Process Choreographer Explorer.
- Specifying a wait time for human task claims

You can choose to have a human task claimed immediately or you can specify an amount of time in milliseconds that you want to wait before a human task is claimed.
- Specifying a potential owner for a human task

You can choose to specify the user ID and password of the potential owner that you want to use to claim a human task. If you do not specify a user ID and password, the user ID and password used to log in to the server will also be used for the potential owner.
- Redefining emulators as manual

If you have an emulator that is defined as programmatic, you can redefine it as a manual emulator. This enables you to manually specify response values for the emulator when it is used in a test.
- Redefining emulators as programmatic

When you first add an emulator to a test configuration module in the integration test client, it is automatically defined as a manual emulator and you will need to manually specify response values for the emulator whenever it is used in a test. However, you can choose to redefine the emulator as programmatic, which enables you to automatically and programmatically specify response values for the emulator using a programmatic emulation file.
- Creating programmatic emulation files

You can create one or more programmatic emulation files for use with a programmatic emulator in the integration test client. This enables you to supplement existing programmatic emulation files with new programmatic emulation files that are customized for specific test purposes.
- Editing programmatic emulation files

You can edit any programmatic emulation file that you want to use with a programmatic emulator in the integration test client. This enables you to define an implementation file for a new programmatic emulator or redefine the implementation file for an existing programmatic emulator.
- Disabling emulators

You can disable one or more emulators. This enables you to prevent a component, reference, or human task from being emulated by an emulator.
- Removing emulators from a test configuration module

You can remove one or more emulators from a module in any test configuration that is open in the integration test client. This enables you to more easily manage the remaining emulators.
- Deleting programmatic emulation files

You can delete one or more programmatic emulation files. This enables you to more easily manage the remaining programmatic emulation files for use with the integration test client.
- Adding monitors to a test configuration module

You can add one or more monitors to a module in any test configuration that is open in the integration test client. This enables you to monitor a specific module wire or export for requests, responses, or both.
- Editing monitors in a test configuration module

You can edit a monitor for a module in any test configuration that is open in the integration test client. This enables you to select whether a specific wire or export in a module is monitored for requests, responses, or both.
- Removing monitors from a test configuration module

You can remove one or more monitors from a module in any test configuration that is open in the integration test client. This enables you to more easily manage the remaining monitors.
- Adding fine-grained traces

You can add one or more fine-grained traces to a module in any test configuration that is open in the integration test client. This enables you to specify fine-grained traces for supported components and trace the event path through the components during a test. Currently, the components with fine-grained trace support are business processes, state machines, and mediation flows.
- Editing fine-grained traces

You can edit a fine-grained trace for a module in any test configuration that is open in the integration test client. This enables you to select and track component variables and display them in the value editor when the fine-grained trace is generated. If you do not select any variables, the fine-grained trace will still be generated, but the variables will not be tracked and displayed in the value editor.
- Removing fine-grained traces

You can remove fine-grained traces from a module in any test configuration that is open in the integration test client. This enables you to more easily manage the remaining fine-grained traces.