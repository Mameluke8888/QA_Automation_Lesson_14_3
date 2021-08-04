Feature: browsing products


  Scenario Outline: User can browse different products
    Given user opens Brainbucket home page in a browser
    When user moves to "<section>" in navigation bar
    And user clicks on "<option>" of a dropdown menu
    Then page with all "<product>" is open


    Examples: Products
    |section      |option             |product      |
    |Desktops     |Macs               |Mac desktops |
    |Desktops     |PC                 |PC desktops  |
    |Phones & PDAs|Phones             |Phones       |
    |Components   |Show All Components|Components   |



