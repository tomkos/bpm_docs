# Search tips for documents

- Click Add > Add Document from Repository on the Documents tab in the Case Information widget.
- Click Add in the Attachment widget and then select Add
Document from Repository.

You can refine your search by using operators in the search term.

| Widget name and view                                                                                      | Version used                           |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------|
| Attachment widget, attachment name                                                                        | Current version document name          |
| Documents view for the Case Information widget, document name                                             | Major version (released) document name |
| Attachment widget, document propertiesDocuments view for the Case Information widget, document properties | Current version document properties    |
| Viewer widget                                                                                             | Current version document               |

In addition, an attachment can be defined to use a specific version of a document. The Attachment
widget will always display the specific version of the document and the properties for that version
even if more recent versions exist.

## Searching for exact words or phrases

You can search for an exact phrase by enclosing
it in double quotation marks ("). For example, the search term "insurance
claim" searches for the two-word phrase insurance claim, not the separate
words insurance and claim. The search term insurance
claim, without the quotation marks, searches for the separate words
insurance and claim.

## Searching with wildcard characters

## Searching with Boolean operators

| Search term                             | Results                                                                                                                                                  |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| automobile AND "major loss"             | Narrows the search to include documents that must contain both the term automobile and the phrase major loss anywhere in the document.                   |
| automobile OR "major loss"              | Expands the search to include documents that contain either the term automobile or the phrase major loss anywhere in the document.                       |
| automobile -"major loss"                | Searches for documents that contain automobile and that do not contain the phrase major loss anywhere in the document.                                   |
| automobile OR truck -"major loss"       | Searches for documents that contain either the term automobile or the term truck and that do not contain the phrase major loss anywhere in the document. |
| automobile OR (truck AND -"major loss") | Searches for document with automobile and documents that do not have automobile but that have the word truck but not the word -"major loss".             |

## Searching with match conditions