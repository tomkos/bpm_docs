# Unicode names are incorrect in case package for documents with non-English characters in the
file name

## Symptoms

## Resolving the problem

There is no way to fix a document name in the tooltip or security warning dialog
box. However, accepting the security warning opens the correct document.

- Continue to use non-English Unicode file names, knowing that the document file names will be
incorrect when the files are extracted from the case package zip file.
- Include only those documents that do not have non-English Unicode file names in the case
package.
- Rename the extracted document with the embedded non-English Unicode file name that is listed in
the case package PDF.
- Ensure that the third-party utility you use to unzip the case package fully supports UTF-8
format file names.