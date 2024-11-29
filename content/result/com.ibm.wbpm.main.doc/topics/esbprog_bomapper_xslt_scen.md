<!-- image -->

# Example scenarios

In order for customers to book flights with Personal Holidays, the flight availability must be
checked against a fictitious airline company, My Airways, flight schedule. The interface for
the Personal Holidays booking system is generic and not airline specific. The Personal Holidays
booking system represents information differently to the My Airways booking system. The differences
are shown in the following XML.

```
<flightBooking>
	<departFrom>London</departFrom>
	<goingTo>Paris</goingTo>
	<departDate>29/10/2010</departDate>
	<returnDate>12/11/2010</returnDate>
	<adults>2</adults>
	<children>0</children>
</flightBooking>
```

```
<flightBooking>
	<countryOfDeparture>UK</countryOfDeparture>
	<from>London</from>
	<to>Paris</to>
	<depart>29/10/2010</depart>
	<return>12/11/2010</return>
	<flightClass>2</flightClass>
	<adult>2</adult>
	<children>0</children>
</flightBooking>
```

## Mapping message structures

Figure 1. Message Structure mapping using a Mapping mediation primitive within a mediation flow component

<!-- image -->

When a Mapping mediation
primitive is created, a mapping file associated with the primitive is created or selected that
describes the transformation between the source and the target business objects. This is shown in
Figure 2
. The image also shows
the way the values in the source message are used to populate the target message.

Figure 2. Message Structure mapping within Integration Designer

<!-- image -->

## Service enrichment

Personal Holidays must determine the country of departure dynamically from within the mediation
module.

The countryOfDeparture field does not exist within the Personal Holidays
flight booking message structure. A Database Lookup mediation primitive is used to establish the
country of departure in any given instance. The Database Lookup mediation primitive populates the
country of departure into the transient context. In this example, the company use a BO Mapper
mediation primitive to transform the transient context and body into the new required message
structure. This is shown in Figure 3.

Figure 3. Service enrichment using a BO mapper within a mediation flow component

<!-- image -->

## Data field level

- The XML mapping editor provides built-in string, date/time, math and boolean functions, and
allows you to call out to Java™ code that can use the DOM API
in order to compose XPath expressions, or call out to other XSL templates. XML maps also provide the
ability to look up values from external files or other sources, based upon a key taken from the
message being transformed.
- The BO Map editor provides string extraction and link functions, and allows you to call Java that can use the BO (SDO) API. From a BO Map, you can also
use the relationship transforms to manage sets of correlated data.

Figure 4.  Format date function

<!-- image -->

Figure 5.  The configuration of the format date transformation

<!-- image -->

Figure 6.  Custom transformation in a BO map

<!-- image -->

Figure 7. 
Java code in the Properties view

<!-- image -->

In Figure 7
 the
java.text.DateFormat class is used to format the incoming
Date object to produce a formatted string using the built in
SimpleDateFormat.SHORT format. This corresponds to dd-mm-yyyy or yyyy-mm-dd.
By using a Java snippet, you can access the source and target
data fields as local variables. These are described in the generated comments produced by the
editor. From a custom Java snippet, it is also possible to
invoke code from other Java classes that are contained in the
module or in an associated library project.