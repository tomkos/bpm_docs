<!-- image -->

# The building blocks of the business state machine editor

- Interfaces
- References
- Variables
- Correlation sets
- States
- Transitions
- Action bar objects

## Interfaces

The interface  is
a set of operations the business state machine accepts and responds
to.

## References

The reference  is
not an interface, but instead tells the business state machine where
to find operations that it can invoke. More to the point, it specifies
the interface that is used in the invocation of another component.

## Variables

Variables  store
the data that are used by a business state machine, and can be either
a business object or a simple type.

## Correlation sets

A correlation
set defines properties that are used to distinguish one instance of
a business state machine from another within a runtime environment.

## States

1. The state begins with the running of any existing entry actions.
2. The state will then stop and listen for an event to occur.
3. When an event occurs, a path is chosen that is appropriate to
it.
4. An exit action (if there is one) runs before the business state
machine transitions to another state.

There are five different kinds of states:

- Initial state The first state and starting point of any business state machine or composite state, the initial state is where things begin.

When used in a primary business state machine, an initial state has one outbound transition that defines the operation that starts the business state machine.

When used in a composite state, the outbound transition must be automatic.

In both cases, there can be only one outbound transition, and it cannot be guarded.
- State Use a state to represent an individual discrete stage in your business state machine diagram. 

A simple state may define both an entry and an exit action, and when it is entered, it enables all of its outbound transitions.
- Composite state A composite state is an aggregate of two or more states. Use them to decompose a complex business state machine diagram into an easy to comprehend hierarchy of business state machines. It can also be done to facilitate exception and error handling by making it possible to define a single exception transition that is valid for all states nested within the composite state.

Composite states may define one or more outbound exception transitions, or a single default transition (see definitions below).
- Final state When used in a business state machine, the final state is where the business state machine comes to a normal end.

When it is contained in a composite state, the movement to final state will fire the composite state's default transition.

A final state may define an entry action, but it may not have an exit action.
- Terminate Use this state to bring a halt to all activity within the business state machine. It is an abnormal end to a business state machine.

In the main business state machine, a terminate state ends the processing. When used within a composite state, a terminate state is used to indicate and abnormal end, and it will cause the whole business state machine to stop. A terminate state may define an entry action, but it may not have an exit action.

## Transitions

A transition  channels
control from one state to the next by recognizing the triggering event,
evaluating the conditions necessary for control to flow through it,
and determining what actions can occur should processing be allowed.
An event can trigger more than one transition at a time, but only
one of those transitions will fire.

1. Call event - the transition is triggered when the correct operation
is called
2. Timer event - the transition is triggered when the timer expires
3. Completion event - the transition is triggered when the source
state is entered and its entry action, if any, runs.

If an event triggers more than one outbound transition
from a given state, the order that the transitions are checked is
undefined. In the case of nested composite states, if an event triggers
transitions in more than one composite state, the transitions are
checked from the innermost composite state to the outermost composite
state.

- A transition is disabled when the current state of the
business state machine is any other state than the source state of
the transition. While disabled, a transition will ignore any instances
of its trigger event.
- A transition is enabled when the current state of the
business state machine is the source state of the transition.
- A transition is triggered when it is enabled, and an instance
of its triggering event occurs.
- A transition is fired if it is triggered, and either has
no guard condition or, the condition evaluates to true.

- Default transitionsA default transition is an unguarded, automatic transition whose source state is a composite state, and whose trigger is a completion event. A default transition fires whenever a final state within the composite state is entered. If a composite state defines a default transition, it must define a final state and vise versa.
- Exception transitionsException transitions are transitions whose triggering event is either a timer event or a call event, and whose source state is a composite state. Exception transitions are enabled when the composite state is entered and triggered when their triggering event occurs, regardless of which substate the composite state is in. If a substate defines a transition with the same triggering event, the guard, if any, of that transition will be checked before the exception transition. That is, transitions fire from the inside out.
- Simple transitionSimple transitions have source and target states that are different, and where exit and entry actions run.
- Self transitionsIn a self-transition, the source state and the target state are the same.

There are two kinds of self transitions. An external transition is one that runs both the exit and entry actions and registers a change of state. Conversely, an  internal transition is a self transition that does not allow the exit and entry actions to run. Internal transition cannot be defined on a composite state, an it's triggering event must be either a call event or a timer event.

## Action bar objects

These objects
appear within the action bar, and are modifiers that are used on states
and transitions.

There are six kinds of objects:

- Entry Entry is the action that runs when coming into the state.
- Exit Exit is the action that runs when leaving the state.
- Operation An operation is an external prompt, represented by an interface, that attempts to trigger a movement from one state to another.
- Timeout A timeout imposes a time limit on how long the business state machine should remain in the state. It can be an expiration (the date and time when the state expires), or a duration (the length of time to remain in the state).

Use a timeout to ensure that the state will not be maintained indefinitely while waiting for an operation that may never occur.
- Condition Use a condition to guard the transition, and allow the transition to the next state if the condition evaluates to True.
- Action An action is an activity that runs when transitioning from one state to another.