<!-- image -->

# Join behavior in activities

A join is a set of incoming links that connects an activity to
the rest of the process. When we speak of join behavior, we are referring
to two separate aspects: join condition and join failure.

## Join condition

- When an activity is the target of at least two incoming links,
you can configure its join behavior using a built-in expression, or
by customizing one yourself. This condition evaluates every one of
the incoming links (there can be more than one, and each one must
have a value in order to continue), and decides whether or not the
activity will be started.

## Join failure

- When an activity is nested within a parallel activity, and the
link conditions that lead to an activity conflict with those of its
join condition, then a fault is thrown on that activity. You can use
the join failure settings to determine whether or not to suppress
this fault, skip the activity that threw it, and continue with the
invocation of the process. When this happens, the activity does not
run, and the outgoing transition conditions are evaluated to false.