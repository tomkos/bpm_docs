<!-- image -->

# Activity jump targets

- You can perform activity jumps within sequence activities. This
means that the source activity and target activity of the jump must
be in the same sequence and both are not nested in other structured
activities.
- You can perform activity jumps within flow activities. In this
case, the source activity and target activity of the jump can be directly
nested in a flow activity and there must be only one path in the control
flow from source to target.
- Additionally, you can jump outside of a scope if there is only
one activity contained in the scope. For example, it is possible to
jump from an invoke activity with an attached handler.
- You can also perform activity jumps within cyclic flows, whereby
the source activity and target activity of the jump are also directly
nested in the cyclic flow and are not nested in other structured activities.

<!-- image -->