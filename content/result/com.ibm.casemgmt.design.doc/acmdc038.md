# Translating content solution assets that are stored in Content Platform Engine

## About this task

## Procedure

To translate the content artifacts:

1. In Administration Console for Content Platform
Engine,
browse to locate the object store that contains the artifacts that
you want to translate.
2. Click Actions and then select Localize
Class Definitions, Localize Property Templates,
or Localize Choice Lists.
3. Select a language.
4. Locate the artifacts in Administration Console for Content Platform
Engine and enter localized
values for the display names.

Table 1. Location of artifacts in Administration Console for Content Platform
Engine

Artifact label
Location in Administration Console for Content Platform
Engine

Case types
Use the Localize Class Definitions wizard
under Folder > Base Case > Case Folder. Translate the case
types that are defined in the solution.

Document classes
Use the Localize Class Definitions wizard under
Document class. If your case management application displays only the
document classes that are defined in a solution, you can translate only those document classes. If
your case management application displays all of the document classes, translate all document
classes.

Activities
Use the Localize Class Definitions wizard
under Activity > Case Activity. Translate only discretionary activities. You do not have
to translate the automatic and manual activity names because Case Client does not display translated
automatic and manual activity names.

Property templates
Use the Localize Property Templates wizard.
Order property templates by symbolic name. All of the case properties
for a solution are displayed together in the list because they all
have the same solution prefix.

Choice lists
Use the Localize Choice Lists wizard.
Find all of the choice lists with the same solution prefix. Translate
the display names of the choice list values. You do not have to translate
the display name of the choice list.
5. Click OK when you are done.
It might take several minutes for the changes to take
effect on all nodes in the Content Platform Engine cluster.