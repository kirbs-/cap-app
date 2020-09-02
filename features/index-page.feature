Feature: index page

    Scenario: Uploaded files exist on index page
        Given these uploaded files exist
            | file_name |
            | foo.csv   |
            | bar.csv   |
        When a user navigates to home page
        Then user should see "bar.csv"

    Scenario: Clicking "Upload" button prompts upload dialog
        Given a user navigates to home page
        When user clicks "Upload" button
        Then user should see "Select a file to upload"

    Scenario: Clicking "Upload" button on upload dialog uploads selected file
        Given a user navigates to home page
        When user clicks "Upload" button
        and user selects "example.csv" in file browser
        and user clicks upload form "Upload" button
        Then user should see "example.csv"
        and user should not see upload dialog

    Scenario: user downloads file
        Given a user navigates to home page
        and "example.csv" exists
        When user clicks "Download" icon
        Then user should see download dialog

    