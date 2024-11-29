# Boundary events

You can use named boundary events in both views and custom views; however, only one boundary
event can be specified per view. The Button view has boundary events specified by default.

When you create a view, you specify a boundary event in the Overview
properties, under Usage. You must add JavaScript code to trigger the event at the appropriate time using the
this.context.trigger(callback) application programming interface (API). This code
is part of the behavior defined in the Behavior properties.