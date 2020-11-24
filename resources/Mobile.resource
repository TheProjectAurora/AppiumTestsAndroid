* Settings *
Library     WikipediaAppiumLibrary

* Keywords *
Launch Wikipedia Mobile App
    Launch mobile app
    Go to home page

Login to Wikipedia
    Login   ${VALID_USERNAME}   ${VALID_PASSWORD}

Logout From Wikipedia
    Logout

Search For An Article
    [Documentation]     Searches for an article with a given list of keywords
    ...                 Selects the first article that is listed as a search result
    [Arguments]     ${search term}
    Search  ${search term}

Add Article To Reading List
    [Arguments]     ${search term}
    Bookmark article    ${search term} List

Clear search field
    Clear search

Go back to from article page to home page
    [Documentation]  Assumes that we are in an article page
    Press back button   # to search page
    Press back button   # to home page

Go to "My lists" tab
    [Documentation]  Assumes being at main page
    Select my lists tab

Remove List from "My Lists"
    [Documentation]     Assumes being at "My Lists" page
    [Arguments]     ${partial list name}
    Remove list     ${partial list name}

Go to "Explore" tab
    [Documentation]     Assumes the tab menu is shown
    Select explore tab