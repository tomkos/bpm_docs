<!-- image -->

# Editing programmatic emulation files

## Before you begin

- Automatically when you finish creating a new programmatic emulation
file.
- Manually when you want to edit an existing programmatic emulation
file.

If your test is invoking a one-way operation, the test will
return a result of Passed, but the emulation will not actually run
unless you have followed the instructions in the topic "Emulating
components and references when invoking one-way operations".

## About this task

## Procedure

1 If the programmatic emulation editor is not already openin the workbench, complete one of the following steps to open it: The programmatic emulation editor opens.
    - If you want to edit a programmatic emulation file for a specific
programmatic emulator that you currently have selected in the Configurations
page of the test suite editor, click the link on the name of the programmatic
emulation file beneath the Programmatic Emulation radio
button.
    - If you want to edit a programmatic emulation file in a module without
first selecting a programmatic emulator in the Configurations page
of the test suite editor, go to the Business Integration view and
right-click the module that contains your programmatic emulation file,
then select Test > Load Emulator to open
the Load Emulator wizard. Navigate to the programmatic emulation file
(which has a default file extension of .emulate), then select
it and click Finish.
    - If you want to edit a programmatic emulation file in a component
test project without first selecting a programmatic emulator in
the Configurations page of the test suite editor, go to the Business
Integration view and expand both your project and the Emulators subfolder,
then right-click the programmatic emulation file and select Open.
2 If you want to move the programmatic emulation file toa different project, folder or package, complete the following steps:

1. In the programmatic emulation editor, click Move.
The Move window opens.
2. In the Choose destination list,
select the project, folder or package where you want to move the programmatic
emulation file.
3. Click OK. The programmatic emulation
file is moved and any references to the file are updated to reflect
the new file location.
3 If you want to rename the programmatic emulation file,complete the following steps:

1. In the programmatic emulation editor, click Rename.
The Rename Compilation Unit window opens.
2. In the New name field, type the
new name that you want to assign to the programmatic emulation file.
3. Click OK. The programmatic emulation
file is renamed and any references to the file are updated to reflect
the new file name.
4 If your programmatic emulation file does not yet have anyimplementation and you now want to define an implementation for it,complete the following steps:

1. Beside the Overview tab at the
bottom of the programmatic emulation editor, click the tab that is
named for the operation that you are emulating. The Define Emulation
page opens.
2. Depending on whether you want to define the implementation
as a visual snippet or a Java™ snippet,
select either Visual snippet editor or Java
snippet editor.
3. Click Define Emulation. The Emulate
Operation page opens with either a visual snippet editor pane or a Java snippet editor pane.
4. In the visual snippet editor or the Java snippet
editor, define the implementation for your programmatic emulation
file. Note that in the Java snippet editor, the Throws field
displays the available exceptions that you can define in your code.
At any time, you can click Clear Emulation to
remove all content from the editor and start over. (Information about
creating and using visual snippets is found in the IBM® Integration
Designer topic
"Customizing behavior with visual snippets.")
5. When you have finished defining the implementation,
press Ctrl-S to save your changes and close
the programmatic emulation editor.
5 If your programmatic emulation file already has an implementationand you want to modify it but not redefine it as a differentsnippet type (visual snippet or Java snippet),complete the following steps:

1. Beside the Overview tab at the
bottom of the programmatic emulation editor, click the tab that is
named for the operation that you are emulating. Depending on whether
the implementation is defined as a visual snippet or a Java snippet, the Emulate Operation page opens
with either a visual snippet editor pane or a Java snippet
editor pane that contains your implementation.
2. In the visual snippet editor or the Java snippet
editor, make the modifications to the implementation. Note that in
the Java snippet editor, the Throws field displays
the available exceptions that you can define in your code. At any
time, you can click Clear Emulation to remove
all content from the editor and start over.
3. When you have finished defining the implementation,
press Ctrl-S to save your changes and close
the programmatic emulation editor.
6 If your programmatic emulation file already has an implementationand you want to redefine it as a different snippet type (visual snippetor Java snippet), complete the following steps:

1. Beside the Overview tab at the
bottom of the programmatic emulation editor, click the tab that is
named for the operation that you are emulating. Depending on whether
the implementation is defined as a visual snippet or a Java snippet, the Emulate Operation page opens
with either a visual snippet editor pane or a Java snippet
editor pane that contains your implementation.
2. Click Redefine Emulation. The
Define Emulation page opens.
3. Depending on whether you want to redefine the implementation
as a visual snippet or a Java snippet,
select either Visual snippet editor or Java
snippet editor.
4. Click Define Emulation. The Emulate
Operation page opens with either a visual snippet editor pane or a Java snippet editor pane.
5. In the visual snippet editor or the Java snippet
editor, define the implementation for your programmatic emulation
file. Note that in the Java snippet editor, the Throws field
displays the available exceptions that you can define in your code.
At any time, you can click Clear Emulation to
remove all content from the editor and start over. (Information about
creating and using visual snippets is found in the topic "Customizing
behavior with visual snippets.")
6. When you have finished defining the implementation,
press Ctrl-S to save your changes and close
the programmatic emulation editor.

## Example