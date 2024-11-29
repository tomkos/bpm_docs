<!-- image -->

# Custom mediation

This example describes an instance of when this could occur.

My Airways have created a new service that is used to calculate the number of regular meals and
vegetarian meals required for a flight.

Customers are asked to select meals as a step in the flight booking process. This information
will be requested for processing as a batch process to determine the number of regular and
vegetarian meals required for a flight.

The following XML shows how the business object FlightInfo can contain a
number of SeatBooking records. Each SeatBooking has a
details field which is either a SeatBookingDetails object (normal customers)
or a FrequentFlyerDetails object (frequent flyer customers). Each contains
the customer's meal preference, but in different named fields, mealType
and mealPreference. In this case, a Custom mediation is used to provide more
flexibility to transform this message body.

```
...
<FlightInfo>
	<SeatBooking>
		<type>Economy</type>
		<details xsi:type="ns0:SeatBookingDetails">
			<mealType>regular</mealType>
			<otherDetails>...</otherDetails>
		</details>
	</SeatBooking>
	<SeatBooking>
		<type>Economy</type>
		<details xsi:type="ns0:FrequentFlyerDetails">
			<customerNumber>44906</customerNumber
			<seatPreference>Aisle</seatPreference>
			<mealPreference>regular</mealPreference>
			<milesTotal>490020</milesTotal>
			<dateJoined>2009-11-09-09+00:00</dateJoined>
			<lastUpdate>2010-02-11+00:00</lastUpdate>
		</details>
	</SeatBooking>
	<SeatBooking>
		<type>Business</type>
		<details xsi:type="ns0:SeatBookingDetails">
			<mealType>vegetarian</mealType>
			<otherDetails>...</otherDetails>
		</details>
	</SeatBooking>
	...
</FlightInfo>
...
```

1. It produces a new output SMO
2. It calls another Java™ class to calculate the total
meals
3. It sets the total meals into the SMO body

<!-- image -->

Figure 1. Hover pane showing the message type and structure

<!-- image -->

```
BOFactory boFactory = (BOFactory) ServiceManager.INSTANCE.
		locateService ("com/ibm/websphere/bo/BOFactory");
	DataObject newBody = boFactory.
		createByMessage ("http://Airline/GalleyFulfilment", "getMealTotalsResponseMsg");
```

```
smo.setBody (newBody);
	out.fire (smo);
```

Though this code has created a SMO with the correctly typed body object, it has not been
populated. The SMO body is a DataObject whose immediate child elements are defined in the set of
parts defined in the WSDL message for the operation.

Figure 1 shows the body structure of the
SMO. The expanded view shows that the SMO body has a child element called
getMealTotalsResponse. This has a child element
output1 of type MealTotals.

```
BOFactory boFactory = (BOFactory) ServiceManager.
	INSTANCE.locateService ("com/ibm/websphere/bo/BOFactory");
DataObject newBody = boFactory.
	createByMessage ("http://Airline/GalleyFulfilment", "getMealTotalsResponseMsg");

DataObject mealTotals = MealCalculator.getMealTotals (smo.getDataObject 
	("/body/getMealTotals/input1"));
DataObject totalsResponse = newBody.createDataObject ("getMealTotalsResponse");

totalsResponse.setDataObject ("output1", mealTotals);

smo.setBody(newBody);
out.fire (smo);
```

Figure 2. Hoverpane showing the body structure of the SMO

<!-- image -->