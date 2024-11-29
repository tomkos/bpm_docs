<!-- image -->

# Adding qualities of service qualifiers

## About this task

The system tries to anticipate your needs by generating
qualifiers when you add interfaces and partner references and when
you generate an implementation or synchronize from an implementation.
You can also add your own qualifiers to the module.

See "Quality
of service qualifier reference" under related reference for a list
of qualifiers and an entry point to additional information.

Follow
these steps to add qualifiers:

## Procedure

1. Select an artifact. Qualifiers can be set on
interfaces, partner references, or implementations.
2. In the Properties view, click the Details tab
to set qualifiers on interfaces and references. Click the Implementation  tab
to set qualifiers for the component's implementation. Here
is an example of the qualifiers page for a partner reference:

Here
is an example of a qualifiers page for a human task implementation:
3. If required, expand the tree in the properties to select
the element. Qualifiers are displayed in their own page. Click the Qualifiers tab
to show the settings.
4. On the Qualifier page, use the Add and Delete buttons
(in the top part of the page) to add and remove qualifiers for the
selected element. Qualifiers can be inherited from parent elements.
Listed qualifiers in gray means that the qualifiers are inherited.
You can click Override to override the parent
qualifier with a different setting. Selecting the qualifier in the
top part of the page will display its details in the lower part of
the Qualifiers page. You can drag the separator bar between these
two sections of the Qualifier page to expand the area that you want
to view.

## Example

The following Properties view shows two qualifiers for
the CustomerInfoInterfacePartner reference; the Reliability qualifier
is inherited from the References and the Suspend Transaction qualifier
is specified for this reference:

## What to do next