# Adding and modifying document classes

## About this task

## Procedure

To add or modify a document class from the solution home page:

1. Click the Document Classes tab.
2 Select an existing document class to modify or create a document class. Option Description To add a document class To add a document subclass Tip: To view the properties that a document class inherited from a parent documentclass, select the View inherited properties check box on theProperties tab for the child document class. To modify an existing document class Click the document class name in the list. To reuse a document class Restriction: You cannot modify a reused document class. Properties of a reused documentclass are not displayed in Case Builder , and you cannot add newproperties to the reused document class.

| Option                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| To add a document class              | Click Add Document Class > New.Note: To create a new document class with similar properties as an existing one, choose the parent document class from the list. If you do not want the new document class to inherit properties, make sure no document class is selected.  Enter a name and a description for the document class. The Unique Identifier field is updated as you enter the name for the document class. You cannot change the unique identifier after you click OK.                                                                                                                         |
| To add a document subclass           | Select the parent document class in the list of document classes. Click Add Document Class > New subclass. Enter a name and a description for the document class. The Unique Identifier field is updated as you enter the name for the document class. You cannot change the unique identifier after you click OK. Click OK. On the Properties tab, add the properties that apply to this document subclass.  Tip: To view the properties that a document class inherited from a parent document class, select the View inherited properties check box on the Properties tab for the child document class. |
| To modify an existing document class | Click the document class name in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| To reuse a document class            | Click Add Document Class > Reuse Document Class. Select a document class that exists in Content Platform Engine.  Restriction: You cannot modify a reused document class. Properties of a reused document class are not displayed in Case Builder, and you cannot add new properties to the reused document class.                                                                                                                                                                                                                                                                                         |

3. Click OK.
4. Optional: 
Add properties to the document class. For more information, see Adding and reusing properties.
5. Optional: To hide a document class from the Case Client, select the
Hidden check box.
6. Click Save.
Case Builder does not save
your edits automatically as you work. When you click OK to close a dialog box
or an editor view, your selections are stored in memory. Click Save to store
your changes to the solution definition file. If you do not save your changes, you can save or
discard the changes before you close the solution.

- Document classes

Document classes help you to organize and classify the documents that belong to a case. You can provide additional information about the documents by assigning properties to the document class.