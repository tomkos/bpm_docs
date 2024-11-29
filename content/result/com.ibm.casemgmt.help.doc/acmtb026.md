# Unexpected behavior when you use choice lists that have duplicate values with unique display
  names

## Symptoms

The duplicate
values are not removed from the choice list. That means that when users select the value, the first
instance of the value is selected (in the current example, First). In a multi-value property, if you
add Primary, it is converted to First. The Summary view and Case Details view show the value
selection as First.

However, if you select the value from a single value property, the
behavior changes. You can select Primary from the choice list for the single value property. In this
instance, the Summary view displays First, while the Case Details view displays Primary.

You
might also encounter issues where the user chooses the second value of two duplicate values, for
example, in a check list box editor. The selection might disappear and default to the first instance
of the value.

## Resolving the problem