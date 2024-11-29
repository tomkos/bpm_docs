<!-- image -->

# Resolving modeling errors in generalized flow activities

## About this task

The generalized flow activity allows mixing of cycles
and parallelism within the same flow. Standard BPEL is based on building
blocks represented by structured activities. Sound modeling is ensured
by separating cycles and parallelism into different structured activities.
Therefore generalized flow activities allow the possibility of errors
that cannot occur in standard BPEL implementations.

Definition
of region. A region is a part of the BPEL process containing
activities and links. An area in the process model that has a single
entry link and a single exit link is called a SESE-regions (Single
Entry - Single Exit).

Figure 1. An example of a generalized flow with multiple
SESE-regions.

<!-- image -->

Figure 2. An example of a generalized flow
with multiple SESE-regions.

<!-- image -->

Each
activity with one incoming link and one outgoing link is a simple
SESE region. In this example RegionA4 and RegionA6 are
SESE regions. There are three additional regions of interest. First
there is RegionA3 consisting of Activity3 and the LoopBack
link forming a cycle. Second there is the InnerRegion consisting
of Activity2, Activitiy5, RegionA3, RegionA4 and all links connecting
those activities and regions. And third, there is the OuterRegion consisting
of Activity1, Activity7, the InnerRegion, RegionA6 and all
links connecting those activities and regions.

Types of regions.
A region can be categorized into four types - cyclic region, parallel
region, neutral region and unsound region. This categorization is
made upon the directly enclosed gateways and the contained graph structure.

Cyclic
regions A cyclic region contains one or more cycles and the following
gateway types: Split, Merge and converging Inclusive OR. RegionA3 is
an example of a cyclic region.

Parallel regions. A parallel
region can contain the following gateway types: Fork, Join, and diverging
as well as converging Inclusive OR gateways. Note that the categorization
is made upon the directly enclosed gateways, regions that are nested
within a region do not contribute to the categorization. For the OuterRegion only
the Fork gateway of Activitiy1 and the Join gateway at Activity7 define
the region type. The Split and Merge gateways contained in the InnerRegion and RegionA3 do
not contribute to the categorization of the OuterRegion. The OuterRegion in
the previous example is a parallel region. Parallel regions do not contain
cycles, although they may contain nested regions which do contain
cycles.

- no gateways, or
- only converging Inclusive OR gateways, or
- Split, Merge and converging Inclusive OR gateways without a cycle

Unsound
regions Unsound regions contain a mixture of exclusive gateways
(Split and Merge) and parallel gateways (Fork, Join, diverging Inclusive
OR). A process model containing unsound regions is categorized cannot
be run in the runtime environment. Examples of unsound regions are
shown below.

Types of unsound process models There are
three possible types of unsound model - deadlock, lack of
synchronization, and cycles in parallel regions.

Figure 3. A
generalized flow with a deadlock.

<!-- image -->

Lack
of synchronization occurs in a process model when an activity
with a merge gateway is run multiple times although it should be run
only once. This happens when multiple incoming links are followed. Figure 4 is
an example of a process model with lack of synchronization

Figure 4. A generalized flow model with a lack of synchronization.

<!-- image -->

Figure 5. A generalized flow with a cycle in a parallel region

<!-- image -->

If you find modeling problems in your generalized
flow activities follow the steps below to resolve these issues.

## Procedure

1 To resolve a deadlock or a lack of synchronization. An unsound region contains in most cases either a deadlockor lack of synchronization. The following error is reportedfor the deadlock example (Figure 3 ): Oneregion of generalized flow GeneralizedFlow isnot mappable . All activities belonging to the unsound regionare listed in the error message so you that you can locate the problem.By looking at the gateways inside that region the type of unsoundprocess model can be determined. By changing the gateway type forone or more gateways or by re-structuring the region, the error canbe resolved. In our example (Figure 3 ) possiblesolutions are: This is not a complete list of solutions, and other may be moreappropriate for resolution of your deadlock.

An unsound region contains in most cases either a deadlock
or lack of synchronization.

The following error is reported
for the deadlock example (Figure 3): One
region of generalized flow GeneralizedFlow is
not mappable.

All activities belonging to the unsound region
are listed in the error message so you that you can locate the problem.
By looking at the gateways inside that region the type of unsound
process model can be determined. By changing the gateway type for
one or more gateways or by re-structuring the region, the error can
be resolved.

    - If Activity4 needs to run after either Activity2 or Activity3
have been processed (determined by the split gateway), the join gateway
needs to be changed to a merge or an Inclusive OR gateway.
    - If Activity4 needs to run after both Activity2 and Activity3
have been processed, the Split gateway needs to be changed to a Fork
gateway.
    - If Activity4 needs to run only when Activity2 have been
processed, the link between Activity3 and Activitiy4 needs to be removed.
    - If Activitiy4 needs to run only when Activity3 have been
processed, the link between Activity2 and Activity4 needs to be removed.
2 To resolve a cycle in a parallel region. Forthe example (Figure 5 )you would see three error messages, one for each red cross in thefigure. For example: The link or activity Activity2 is participatingin a parallel region which contains a cycle . Such a message shouldalert you that you have a cycle in a parallel region. For theexample (Figure 5 )possible solutions include: This is not a complete list of solutions, and others may be moreappropriate for resolution of your cycle in a parallel region.

For
the example (Figure 5)
you would see three error messages, one for each red cross in the
figure. For example: The link or activity Activity2 is participating
in a parallel region which contains a cycle. Such a message should
alert you that you have a cycle in a parallel region.

- Change the converging gateway at Activitiy2 to a Merge and the
diverging gateway at Activity5 to a Split.
- Remove Link 5, connecting Activity5 with Activity2.