<!-- image -->

# Example: Append the result of two or more input arrays into
an output array

<!-- image -->

<!-- image -->

Both agencies are owned by the
same company, which wants to inform all their clients of upcoming
deals. To create a combined list of all members who should receive
flyers for an upcoming promotion, combine all gold client members
and all silver client members from Star Travel with all clients of
the Cheap Travels agency.

To achieve this scenario, create
an Append transform between the input array
elements goldStar\_client and silverStar\_client in TravelAgencyA and
the output array element client in TravelAgencyB .

First,
create an XML map with TravelAgencyA as the input business object
and TravelAgencyB as the output business object. Then create an Append
transform with  goldStar\_client  and silverStar\_client as
the input elements, and client as the output
element.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Notice
that you cannot expand the arrays here to create a mapping. This is
because the mapping must be created in the nested For each transform.
(The For each transform gives the same warning
indication as before in which some nested transforms do no yet exist).
 Edit the For each transform to define the
mapping from gold star clients to general clients.  In this example,
we will simply move firstname and lastname information.
The rewardPoints information is not used in
the example.

<!-- image -->

<!-- image -->

There is no need to change
the Move transform at this nested level since
it performs the required result of copying the silver star client
information over to the target which is of the same complex type.
 Move up one nested mapping level once more. The warning on the Append
transform has now gone away. The Append transform
is complete.

<!-- image -->

```
<?xml version="1.0" encoding="UTF-8"?>
<ns0:TravelAgencyA xmlns:ns0="http://FindTravelDestinationAp" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <goldStar\_client>
    <firstname>John</firstname>
    <lastname>Smith</lastname>
    <rewardPoints>10476</rewardPoints>
  </goldStar\_client>
  <goldStar\_client>
    <firstname>Kathy</firstname>
    <lastname>Jennings</lastname>
    <rewardPoints>14872</rewardPoints>
  </goldStar\_client>
  <goldStar\_client>
    <firstname>Bill</firstname>
    <lastname>Cunningham</lastname>
    <rewardPoints>3413</rewardPoints>
  </goldStar\_client>
  <silverStar\_client>
    <firstname>Robert</firstname>
    <lastname>Meyers</lastname>
  </silverStar\_client>
  <silverStar\_client>
    <firstname>Sue</firstname>
    <lastname>Berton</lastname>
  </silverStar\_client>
</ns0:TravelAgencyA>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<io:TravelAgencyB xmlns:io="http://FindTravelDestinationAp" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <client>
    <firstname>John</firstname>
    <lastname>Smith</lastname>
  </client>
  <client>
    <firstname>Kathy</firstname>
    <lastname>Jennings</lastname>
  </client>
  <client>
    <firstname>Bill</firstname>
    <lastname>Cunningham</lastname>
  </client>
  <client xmlns:ns0="http://FindTravelDestinationAp">
    <firstname>Robert</firstname>
    <lastname>Meyers</lastname>
  </client>
  <client xmlns:ns0="http://FindTravelDestinationAp">
    <firstname>Sue</firstname>
    <lastname>Berton</lastname>
  </client>
</io:TravelAgencyB>
```

The resulting output shows
that gold star and silver star clients have been appended together.
The order of the output is all the gold star clients and then all
the silver star clients.

<!-- image -->

<!-- image -->

```
<?xml version="1.0" encoding="UTF-8"?>
<io:TravelAgencyB xmlns:io="http://FindTravelDestinationAp" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <client xmlns:ns0="http://FindTravelDestinationAp">
    <firstname>Robert</firstname>
    <lastname>Meyers</lastname>
  </client>
  <client xmlns:ns0="http://FindTravelDestinationAp">
    <firstname>Sue</firstname>
    <lastname>Berton</lastname>
  </client>
  <client>
    <firstname>John</firstname>
    <lastname>Smith</lastname>
  </client>
  <client>
    <firstname>Kathy</firstname>
    <lastname>Jennings</lastname>
  </client>
  <client>
    <firstname>Bill</firstname>
    <lastname>Cunningham</lastname>
  </client>
</io:TravelAgencyB>
```

Although this example only
focused on array element inputs, Append transforms
can be used whenever their are multiple inputs that need to be mapped
to an array target.  Therefore, the Append transform
can also be used when multiple non-array elements target an output
array element.