# Which artifacts should I use?

<!-- image -->

Your first decision is whether to use client-side human services or heritage human services.

## Client-side human services

Client-side human services use newer technologies for choreographing user interfaces. To use
client-side human services, you must be in the designer.

Client-side human services are built in the designer and run in a web browser. When you are using
client-side human services, you are provided with sets of UI views and responsive coach views
(deprecated), which you can use to create pages and complex user interfaces.

It is generally recommended that you use client-side human services unless you are editing a
heritage human service that was created in an earlier product
version.

## Heritage human services (deprecated)

If one or more of the conditions listed earlier apply, use heritage human services. To create or
edit heritage human services you can use the designer, which provides support to facilitate
migration of heritage human services from an earlier version. You can update your heritage human
services in phases over time and eventually convert them to client-side human services. If you work
with heritage human services in the designer, you can convert the deprecated responsive
coach views into UI views and use the grid layout to modernize your user interfaces. See Converting deprecated functions. You can also use the simple validation pattern that the designer provides
to validate the data in your coaches. See Validating coaches in heritage human services.

Heritage human services run on the server but display their user interfaces in a web browser. A
process application can have both
heritage human services and client-side human services and both types can use the same views.
Whether you choose to use client-side human services or heritage human
services, make sure that you avoid mixing UI views, responsive coach views (deprecated),
and non-responsive coach views in the same coach.

When you are using heritage human services, you must decide whether to use responsive
coaches, or coaches for a particular user interface. A heritage human service can have
responsive coaches, and coaches in its flow.