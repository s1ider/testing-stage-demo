Feature: Buy ticket

    Background:
        Given I am on 'Registration' page

    Scenario: Validate empty mandatory fields
        When Submit form
        Then Validation error is displayed for input 'Email'
        Then Validation error is displayed for input 'Фамилия'
        Then Validation error is displayed for input 'Имя'
        Then Validation error is displayed for input 'Телефон'

    Scenario: Validate promo code
        When Submit form:
            | label    | value                |
            | Фамилия  | Robot                |
            | Имя      | Bobot                |
            | Email    | r2d2@bcdtriptech.com |
            | Телефон  | 1234567890           |
            | Промокод | 12345                |
        Then Validation error is displayed for input 'Промокод'

    Scenario: Buy a ticket
        When Submit form:
            | label    | value                |
            | Фамилия  | Robot                |
            | Имя      | Bobot                |
            | Email    | r2d2@bcdtriptech.com |
            | Телефон  | 1234567890           |
            # | Промокод | 12345                |
        Then 'Checkout' page should be displayed

