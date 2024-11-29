<!-- image -->

# How the store-and-forward feature works

You set the store-and-forward qualifier in Integration Designer. This qualifier can be specified on an import, a
SCA export, or a component. It can be specified for all interfaces of the component, a specific
interface, or a specific operation. The exception part of the qualifier can apply to any of these
different levels. However, the state (store or forward), applies at the component level only.

When an application with a store-and-forward qualifier is deployed to the server, and runtime
validation is enabled, a runtime validator confirms that the qualifier is specified correctly. If
there are any errors during validation, the installation of the application is stopped. If there are
any warnings, they are displayed in the log file and the installation of the application is allowed
to continue. The rules for validation of this qualifier are specified at Store-and-forward runtime validator.

## Component calling a web service

Figure 1. Flow of asynchronous request processing from an SCA module to an target service when the
store-and-forward feature is used

<!-- image -->

1. A component calls the target web service by way of the web service import.Because this is an
asynchronous call, requests are put on the queue by the calling component, where they are picked up
by the import.
2. The import detects that the service is down and retries the operation.As shown in Figure 1, the destination queue cannot be
reached and, therefore, the service cannot pick up the asynchronous requests for
processing.
3. If the service is unavailable, a failed event is created. If subsequent retries fail, the import
generates a service unavailable exception.When the service unavailable exception is generated, a
failed event is created and the recovery service checks the configured policy to determine whether
this exception means that the service is down.
4. If it is determined that the service is down, the asynchronous requests are placed in the
store-and-forward queue.
5. Additional asynchronous requests intended for the service are stopped before they can reach the
import and are stored until the service becomes available.Storing the asynchronous requests
prevents additional failures from occurring.
The size of the queue is configurable. Make sure
you specify a size that is large enough to accommodate the asynchronous requests. If the queue is
not large enough, the event store will overflow, causing failed events to be generated.
When
configuring the size of the queue, estimate how long the service might be down and consider the rate
of arrival of asynchronous requests.

Once the service becomes available again, you will have failed events in the failed event manager
that need to be resubmitted for processing. This does not happen automatically. Use the failed event
manager to resubmit the events that triggered storing in the first place. These events will be
tagged with an Activated Store event qualifier. Then, open the widget in Business Space, locate the
service control point that triggered the store, and select Forward.

If event sequencing and store-and-forward processing are specified on the same operation or
interface, the failed event that triggered the store must be resubmitted before any sequenced failed
events behind it can be forwarded.

## SCA module calling multiple target services

The same sequence of steps occurs when multiple target services are called from a single SCA
module, but with one notable exception - if one of the target services called by the component
becomes unavailable, all asynchronous requests are stopped before they reach an import and stored
for future processing. The store-and-forward qualifier is specified on the component's
interface.

Figure 2 shows two asynchronous
requests flowing from one SCA module to multiple target services. One of the target services is
unavailable, but the other is available. Subsequent asynchronous requests intended for both the
first target service and the second are stopped before they reach the import and stored for future
processing.

Figure 2. Flow of asynchronous request processing from one SCA module to multiple target services when
the store-and-forward feature is used

<!-- image -->

## Unsupported scenario - Long-running process calling a target service synchronously

Figure 3 shows a long
running process calling a target service synchronously. Even if a store-and-forward qualifier is
enabled a long running process' interface, store-and-forward qualifier will not take effect.

Figure 3. Long running process calling a target service is not a supported store-and-forward
scenario

<!-- image -->

- Behavior of store-and-forward feature after server restart, application stoppage, or application uninstallation

If the store-and-forward feature is activated for a component in an application and the server is restarted, or if the application is stopped or uninstalled, the store-and-forward feature will behave in one of the following ways.
- Store-and-forward in a clustered environment

In clustered environments, when one service control point is stopped or started, the rest of the service control points for that component (across the members of the cluster) also starts or stops.
- Store-and-forward runtime validator

When an application with a store-and-forward qualifier is deployed to the server, a runtime validator confirms that the qualifier is specified correctly. If there are any errors during validation, the installation of the application is stopped. If there are any warnings, they are displayed in the log file and the installation of the application is allowed to continue.