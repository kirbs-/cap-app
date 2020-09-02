Feature: CSV analytics

    Scenario: Clicking show details displays CSV file contents
        Given "example.csv" exists
        When a user clicks "Show Details" link
        Then user should see "guid"

    Scenario: Clicking stats aggregates data by year
        Given "example.csv" exists
        When a user clicks "Stats" link
        Then user should see "something" 