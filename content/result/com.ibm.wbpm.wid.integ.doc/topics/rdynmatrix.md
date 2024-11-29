<!-- image -->

# Message routing when dynamic endpoint property is set

| "Use dynamic endpoint" set on callout or service invoke   |  URI exists in /headers/SMOHeader/Target/address or in /headers/SMOHeader/AlternateTarget   | Import is wired to callout's associated reference   | Runtime behavior                                        |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| Yes                                                       | Yes                                                                                         | Yes                                                 | message routed to URI in target address element         |
| Yes                                                       | Yes                                                                                         | No                                                  | message routed to URI in target address element         |
| Yes                                                       | No                                                                                          | Yes                                                 | message routed to static endpoint address of the import |
| Yes                                                       | No                                                                                          | No                                                  | unwired reference exception                             |