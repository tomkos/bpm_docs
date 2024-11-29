<!-- image -->

# Creating artifact evolutions

## About this task

## Procedure

1. Launch the New Artifact Evolution wizard by clicking File > New > Artifact
Evolution.
2. From the New Artifact Evolution wizard, create a new library
to use for the artifact evolution by clicking New.
The New Library window opens. Enter a new library name and click Finish.
3. From the New Artifact Evolution wizard, enter a name for
the artifact evolution and click Next.
4. In the new XSD Schema window, click Browse to
find the new XML Schema(s) which contain the new versions of business
objects to be imported into the new library. Click Next:
5. From the list of new artifacts, select the ones that will
replace existing artifacts, or click Select All if
you are unsure which new artifacts correspond to existing ones.
6. Click Finish. An artifact evolution
has been created in the library.
7. Next, you must add existing projects/libraries which contain
the existing artifacts to be replaced by their new versions. Right-click
in the editor view and select Add project  from
the pop-up menu. The Add project containing old artifacts window
box opens. Select the module or library containing the existing artifacts.
The existing artifacts are added to the artifact evolution editor.
8 To define how the differences between new and existingartifacts should be propagated, you have to associate the new artifactswith the existing ones. You can do that by clicking and dragging fromthe new artifact to the appropriate existing artifact. However, theartifact evolution editor can do some of this for you automatically.To automatically connect the new and existing artifacts, select the AssociateArtifacts With Same Names icon from the toolbar. The connectionsare made and the artifact differences are highlighted in the editor.The artifact differences icons are used as follows:
    1. - indicates a difference in artifact namespaces
    2. - indicates a difference in artifact names
    3. - indicates a difference in artifact contents
9. The Properties view shows artifact contents and differences
between associated artifacts. Select the connection in the artifact
evolution editor view and the Properties view will show the Details
and Description for review. You can view the content of both the existing
and new business objects as well as what the differences between those
business objects are.
10. Also, all of the differences between associated artifacts
are presented in the Problems view.
11 Next, to modify the existing artifacts and their dependenciesaccordingly to the new artifacts, you must refactor. After refactoring,the artifact evolution editor will update the view to remove the artifactdifferences indicated before refactoring. The following examples arethe toolbar actions for refactoring:

1. - Select
this icon from the toolbar to refactor the artifact name differences.
The Refactor Artifact Differences window opens with a list of name
differences to refactor. Click OK to finish.
2. - Select this icon from the toolbar to refactor
the artifact namespace differences. The Refactor Artifact Differences
window opens with  a list of namespace differences to refactor. Click OK to
finish.
3. - Select this
icon from the toolbar to refactor artifact content. Click OK to
finish.
12. Next, you must overwrite the existing schema file(s) with
the new one(s) by clicking the Overwrite Existing Artifact
Files With The New Ones  toolbar icon.

## What to do next