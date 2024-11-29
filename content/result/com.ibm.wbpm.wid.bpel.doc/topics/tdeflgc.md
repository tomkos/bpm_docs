<!-- image -->

# Defining BPEL process logic

- The building blocks of the BPEL process editor

Compose your own BPEL process using a combination of the building blocks listed in this topic.
- Adding an interface or a reference to a business state machine

Interfaces point to the operations that the business state machine accepts and responds to. References define the interfaces that the business state machine uses to invoke other components.
- Adding a variable to a business state machine

Variables store the data that are used by a business state machine.
- Adding an activity to a BPEL process

Activities are the individual business tasks within the process that compose the larger business goal.
- Dealing with faults in your BPEL process

There are a number of ways of dealing with potential faults in your BPEL process.
- XPath for BPEL processes

The XPath standard is well-suited for creating simple data-driven expressions. You can use the XPath standard in some areas of your BPEL processes. For example, you can use XPath to select parts of a BPEL variable or to iterate through the members of an array within a business object.
- Working with micropatterns

When you create a Business Process Execution Language (BPEL) process, you might notice that you have a recurring need for the same function. You can use a micropattern to create a reusable subprocess from a main process.
- Defining transactional behavior

BPEL processes run as part of transactions. The navigation of a BPEL process can span multiple transactions in the case of long-running processes, or happen as part of one transaction in the case of microflows.
- Defining timer-driven behavior in a BPEL process

You can set timer values in a number of places in the business process editor, and for several different activities or elements. Timer values can be configured to trigger processing or expiration after a specific period of time has either elapsed or been reached.
- Enabling SCA events to be emitted

You must enable Service Component Architecture (SCA) events to be emitted if you generate a monitor model that monitors SCA events.
- Locked activities

When a BPEL process is imported from IBM® WebSphere® Business Modeler some of the items in the business flow will be locked. This locking is designed to ensure interoperability between IBM WebSphere Business Modeler and IBM Integration Designer. If you unlock and modify any of the locked items then your process might no longer be compatible with IBM WebSphere Business Modeler. When you try to feed the changes that you have made in IBM Integration Designer back into IBM WebSphere Business Modeler problems can occur. Therefore it is recommended that you do not unlock locked activities.
- Calling other BPEL processes

You can model parts of your business model as subprocesses. Calling one BPEL process from another is discussed.
- Calling business services

Call a business service from your BPEL process using an invoke activity.