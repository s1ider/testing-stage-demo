Feature: Landing page

    Scenario Outline: Check tickets prices
        Given I am on 'Home' page
        When Click on 'Купить билет' link
        When Buy a ticket #<option>
        Then 'Registration' page should be displayed
        Then Price should be '<price>'

    Examples:
        | option | price |
        | 1      | 2150  |
        | 2      | 2150  |
        | 3      | 3700  |
