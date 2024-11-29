# Drill-down trees

Drill-down trees are supported by the following chart views: Area chart SDS, Bar chart, Donut chart, Line chart, Multi purpose chart, Pie chart, Step chart.

## Set up the drill-down tree

1. Under Configuration > Behavior, select Enable Menu, then specify the service flow for the
Data Service. If a service flow does not exist, click
New to create one.
2. In the service flow, add the input and output variables for the drill down tree, similar to the
following example:
3. Create the hierarchical data structure for the drill-down tree. In the implementation of the
server script, enter the XML that creates the hierarchical data structure for the drill-down
tree.The following code snippet is provided as an example. Make your drill-down tree as
complex as you need by branching off into multiple data
sets.<drilldown-spec>
	<drilldown name="Type">
		<js-query description="Quantity Sold by Product Type (Clothing/Appliance/Garden)">
			<script>
				<![CDATA[
				var data = [["CLOTHING", 1093], ["APPLIANCES", 174], ["GARDENING", 98], ["FURNITURE", 342], ["PHARMACY", 422]];
				
				//Example of accessing local variables instead of using the "populateDataSeries" convenience method
				tw.local.dataSeries.dataPoints = new tw.object.listOf.DataPoint();
				for(var i = 0; i < data.length; i++)
				{
					tw.local.dataSeries.dataPoints[i] = new tw.object.DataPoint();
					tw.local.dataSeries.dataPoints[i].label = data[i][0];
					tw.local.dataSeries.dataPoints[i].value = data[i][1];
				}
				]]>
			</script>
		</js-query>
		<drilldown name="Brand" cond-field="../@name" cond-operator="eq" cond-value="CLOTHING">
			<js-query description="Quantity Sold of Clothing Products by Brand">
				<script>
					<![CDATA[
					var data = [["Brand1", 363], ["Brand2", 556], ["Brand3", 174]];
					populateDataSeries(data);
					]]>
				</script>
			</js-query>
			<drilldown name="Gender">
				<js-query description="Quantity Sold of Clothing products by Brand, Gender">
					<in>
						<field var="brand" ref="../@value"/>
					</in>
					<script>
						<![CDATA[
						var data = [];
						if(brand == "Brand1")
						{
							data = [["M", 363]];
						}
						else if(brand == "Brand2")
						{
							data = [["M", 382], ["F", 174]];
						}
						else if(brand == "Brand3")
						{
							data = [["M", 174]];
						}
						
						populateDataSeries(data);
						]]>
					</script>
				</js-query>
				<drilldown name="Kind">
					<js-query description="Quantity Sold of Clothing products by Gender, Brand and for specific Kind">
						<in>
							<field var="brand" ref="../../@value"/>
							<field var="gender" ref="../@value"/>
						</in>
						<script>
							<![CDATA[
							var data = [];
							if(gender == "M")
							{
								if(brand == "Brand1")
								{
									data = [["SHIRT", 251], ["PANTS", 112]];
								}
								else if(brand == "Brand2")
								{
									data = [["SOCKS", 168], ["SHIRT", 214]];
								}
								else if(brand == "Brand3")
								{
									data = [["TIE", 174]];
								}
							}
							else if(gender == "F")
							{
								if(brand == "Brand2")
								{
									data = [["SHIRT", 86], ["PANTS", 65], ["DRESS", 23]];
								}
							}
							
							populateDataSeries(data);
							]]>
						</script>
					</js-query>
				</drilldown>
			</drilldown>
			<drilldown name="Kind">
				<js-query description="Quantity Sold of Clothing products by Kind and for specific Brand">
					<in>
						<field var="brand" ref="../@value"/>
					</in>
					<script>
						<![CDATA[
						var data = [];
						if(brand == "Brand1")
						{
							data = [["SHIRT", 251], ["PANTS", 112]];
						}
						else if(brand == "Brand2")
						{
							data = [["SOCKS", 168], ["SHIRT", 300], ["PANTS", 65], ["DRESS", 23]];
						}
						else if(brand == "Brand3")
						{
							data = [["TIE", 174]];
						}
						
						populateDataSeries(data);
						]]>
					</script>
				</js-query>
			</drilldown>
		</drilldown>
		<drilldown name="Brand" cond-field="../@name" cond-operator="eq" cond-value="APPLIANCES">
			<js-query description="Quantity Sold of Appliances by Brand">
				<script>
					<![CDATA[
					var data = [["Brand6", 35], ["Brand5", 49], ["Brand7", 17], ["Brand8", 22], ["Brand9", 22], ["Brand4", 29]];
					populateDataSeries(data);
					]]>
				</script>
			</js-query>
		</drilldown>
	</drilldown>
</drilldown-spec>

## Populate the drill-down tree with data

```
<![CDATA[var data = [["Brand1", 363], ["Brand2", 556], ["Brand3",174]];
  populateDataSeries(data);
  ]]>
```

```
<![CDATA[var data = [["CLOTHING", 1093], ["APPLIANCES", 174]];
    tw.local.dataSeries.dataPoints = new tw.object.listOf.DataPoint();

    for(var i = 0; i < data.length; i++){
        tw.local.dataSeries.dataPoints[i] = new tw.object.DataPoint();
        tw.local.dataSeries.dataPoints[i].label = data[i][0];
        tw.local.dataSeries.dataPoints[i].value = data[i][1];
    }
    ]]>
```