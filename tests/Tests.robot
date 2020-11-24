* Settings *
Resource            Tests_resource.resource
Resource            ${EXECDIR}${/}resources${/}Mobile.resource
Suite Setup         Run Keywords       Launch Wikipedia Mobile App
...                 Login To Wikipedia
Suite Teardown      Logout From Wikipedia

* Test Cases *
Add Several Articles To My Lists
    [Template]      Add Article to My Lists
    ${SEARCH_TERM_ONE}
    ${SEARCH_TERM_TWO}

Remove Several Articles From My Lists
    [Template]      Remove Article from My Lists
    ${SEARCH_TERM_ONE}
    ${SEARCH_TERM_TWO}

* Keywords *
Add Article to My Lists
    [Documentation]     Assumes being at the main page of wikipedia app @ explore tab
    [Arguments]     ${search term}
    Search For An Article           ${search term}  # picks the first article page
    Add Article To Reading List     ${search term}  # adds the article to a new reading list
    Go back to from article page to home page

Remove Article from My Lists
    [Documentation]     Assumes being at the main page of wikipedia app @ explore tab
    [Arguments]     ${partial list name}
    Go to "My lists" tab
    Remove List from "My Lists"     ${partial list name}
    Go to "Explore" tab
