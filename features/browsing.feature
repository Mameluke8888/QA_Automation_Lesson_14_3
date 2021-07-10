Feature: browsing products


  Scenario Outline: User can browse different products
    Given user opens home page in a browser
    When user clicks on "<Section>" in navigation bar
    And user clicks on "<Option>" of a dropdown menu
    Then page with all "<Product>" is open


    Examples: Products
    |Section    |Option             |Product
    |Desktops   |Macs               |Mac desktops
    |Desktops   |PC                 |PC desktops
    |Phones&PDAs|Phones             |Phones
    |Components |Show All Components|Components



