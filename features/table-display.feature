Feature: CSV analytics

    Scenario: Clicking show details displays CSV file contents
        Given "example.csv" exists
        When user clicks "Display" icon
        Then user should see "guid"

    Scenario: Clicking stats aggregates data by year
        Given "example.csv" exists
        When user clicks "Stats" icon
        Then user should see "1911" 