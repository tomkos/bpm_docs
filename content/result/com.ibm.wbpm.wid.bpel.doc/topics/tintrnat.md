<!-- image -->

# Supporting other languages

## About this task

- Task display name
- Task description
- Task documentation
- Escalations.

- Display name
- Description
- Documentation
- Email messages.

To display human task properties, escalation properties,
or email messages in multiple languages, complete the following steps:

## Procedure

1 Right-click an empty area of the human task editor andselect Translate Text > Export .
    1. In the Select Export Directory window,
specify a file location and name for the output. The window displays a list of the property files that are exported.
A properties file is exported for each locale that is in the human
task.
    2. Click Finish.
    3. Have the content of each of the properties files translated
and rename each one according to the language that it represents.
For example, name a German properties file TaskName\_de\_DE.properties.Make sure that the text is ASCII encoded. To transform
a text file from the platform's native encoding to ASCII, you can
use the native2ascii tool that is provided with the Java™ SDK. Important: Before you
rename a task or escalation, ensure that you have imported all the
translated property files. After renaming a task or escalation, the
keys in the exported property files are no longer valid. To modify
translated text, you must export the property files again.
2 Right-click an empty area of the human task canvas andselect Translate Text > Import .

1. In the Select Import Directory and Property
Files window, browse to the folder where you stored the
properties files and click Open.
The window displays a list of the property files that
you can import.
2. Click Finish.
3. Save your work.
4 To change the default client locale, complete the followingsteps:

1. In the Outline view, click your task to choose the entire
task.
2. In the Details tab of the properties
area, select a language from the Default language field.

## Results

## Related concepts

- Versioning business state machines
- Ad hoc collaboration
- Before you begin: Client types and prerequisites

## Related reference

- Details tab: business state machine editor