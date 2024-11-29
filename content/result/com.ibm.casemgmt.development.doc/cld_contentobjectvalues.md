# Setting values to case content object properties for Add Case,
Split Case, and Case Details

You can dynamically set case content object properties, to which you bind UI views in your
Add Case, Split Case, and Case
Details human service pages, just like any other client-side human service variable that
you add to your page. The following information shows the format for the various case property
types.

While you author the custom client-side human service page in Workflow Designer, you can set the
value of a case content object property as part of the bound view's on Load event
or by other view that calls the view's setXXX method.

| Data type   | Data                      | By using                                                         |
|-------------|---------------------------|------------------------------------------------------------------|
| String      | var data = "Test String"; | this.setText("Hello!"); or me.setData("World!");                 |
| Integer     | var data = 10;            | this.setValue(100); or me.setData(150);                          |
| Float       | var data = 12.5;          | this.setValue(3.14); or me.setData(6.28);                        |
| Boolean     | var data = true;          | this.setChecked(true); or me.setData(false);                     |
| Datetime    | var data = new Date();    | this.setDate(new Date()); or me.setData(new Date(2018, 11, 24)); |

| Data type   | Data                                                                                               | By using                                                          |
|-------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| String      | var data = ["Test String","Second String"]                                                         | var data = [“Hello”,”World!”]; me.setData(data);                  |
| Integer     | var data = [10,20];                                                                                | var data = [10,20]; me.setData(data);                             |
| Float       | var data = [12.5,24.5];                                                                            | var data = [3.14,6.28]; me.setData(data);                         |
| Boolean     | var data = [true,false,false];                                                                     | var data = [true,true]; me.setData(data);                         |
| Datetime    | var data = new Date() [multiple data, for example, new Date(2018, 11, 24),new Date(2018, 11, 25)]; | var data = [new Date(),new Date(2018, 11, 24)]; me.setData(data); |

| Business object members   | Type    | Cardinality properties   |
|---------------------------|---------|--------------------------|
| Name                      | String  | Single cardinality       |
| Age                       | Integer | Single cardinality       |
| Phone Numbers             | Integer | Multi cardinality        |

| Data type   | Data                                                                                                                                                                                                                                         | By using          |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Object      | var data = [{"Name": {"displayName": "Name","value": "Joe"},"Age": {"displayName": "Age","value": 45},"PhoneNumbers": {"displayName": "Phone Numbers","value": {"listAllSelectedIndices": [],"items": [1234567890, 2468024680],"te":"I"}}}]; | me.setData(data); |

- Add Case: The value that you set overrides any default value that is set in
the property.
- Case Details or Split Case: The value that you set
overrides any previous value that you might have set while adding the case.