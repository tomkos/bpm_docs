# Managing toolkit dependencies

## Before you begin

## About this task

When you create a toolkit dependency and that toolkit is later updated,
an icon indicates that a more recent version of the toolkit is available. You can choose to upgrade
the dependency or to ignore the new version.

When you use an asset from a toolkit dependency, make sure that the name of the asset is not in
use in another toolkit dependency. Duplicate naming can cause inconsistent behavior.

When you change the toolkit version, items in the application might be affected if the items
refer to elements that are not in the new toolkit version. In such cases, you need to add these
elements to the new toolkit version, or modify the items to fix the reference.

When you delete a toolkit dependency, you must be sure to update any items in the process application that
refer to the toolkit elements. For example, if a service from the toolkit is the implementation for
an activity, the implementation is missing or broken as soon as you remove the toolkit dependency.
Missing implementations are marked with alert icons in the properties for the affected activity.

## Procedure

To create, update, or delete a dependency on a toolkit, complete the following
steps:

1. In the designer, open the process application or toolkit whose dependencies you want to modify.
2 Follow the required option: Note: Only toolkit versions that are compatible with your project's target environment arelisted.
    - To create a dependency, click the plus sign next to Toolkits, and
select the version of the toolkit that you want.
    - To update or delete a dependency, click the arrow next to the toolkit dependency. Choose
Change Version of Dependency or Remove Dependency from
the pop-up menu, and select the version that you want.

## Results