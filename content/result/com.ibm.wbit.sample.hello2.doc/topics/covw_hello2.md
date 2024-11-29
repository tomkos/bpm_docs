<!-- image -->

# Overview

In this sample you create an SCA import component for
invoking the module from Hello World Part 1, a human task component
to prompt for the name information, and a business process component
that invokes the first two components. This sample gives you an introduction
to some of the capabilities (activities) of a business process and
provides an introduction to the other core tools that supplement the
business object, interface and mediation flow tools introduced in
the Hello World Part 1 sample.

In Hello World Part 1, you built a mediation module that provides an interface to an existing web
service. In Hello World Part 2, you will build a business process that uses this interface.

At a conceptual level, the Hello World Part 2 sample application is composed of the following
elements:

- A module named HelloWorldProcess that contains a business process that is
also named HelloWorldProcess
- A human task component named HelloWorldTask
- An import named HelloWorldImport.

These elements are shown in the following figure:

A human task is a unit of work performed by a person. In this sample, the
HelloWorldProcess business process assigns a task for completion by a person -- you!

The HelloWorldProcess business process is a long-running process, which means that it can come to
a complete stop while waiting for input or instructions. The most common form of this interruption
would be a human interaction or decision, but it could also be the result of calling a long-running
asynchronous service.

In the sample, the business process receives text input indicating gender and then sends this
text to a To-do human task that displays it while prompting for user name information. You will find
and claim the human task in the supplied web-based user interface (that is used for working with
human tasks) and then you will provide the requested name information. When you are finished with
the task, you complete it to send the response back to the business process. The business process
subsequently decides on an appropriate title string based on the gender input text. It then sends
the title and name information to the service implemented by the module from the Hello World Part 1
sample, which results in a concatenated name prefixed by the word "Hello". This result is written to
the console using a small snippet of visual Java code and it is returned to the waiting caller of
the process.

<!-- image -->