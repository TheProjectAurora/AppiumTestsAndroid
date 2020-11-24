* Variables *

&{LOCATORS}         skipButton=org.wikipedia:id/fragment_onboarding_skip_button  # by id
...                 moreOption=//*[@text="More"]
...                 loginMenuOption=//*[@text="LOG IN / JOIN WIKIPEDIA"]
...                 createAnAccountLoginOption=org.wikipedia:id/create_account_login_button   # by id
...                 usernameField=//android.widget.EditText[@text="Username"]
...                 passwordField=//android.widget.EditText[@text="Password"]
...                 loginButton=org.wikipedia:id/login_button     # by id
...                 logoutOption=//*[@text="LOG OUT"]
...                 searchElementNonEditable=//android.widget.TextView[@text="Search Wikipedia"]  # by xpath
...                 searchElementEditable=org.wikipedia:id/search_src_text    # by id
...                 clearSearchFieldButton=org.wikipedia:id/search_close_btn  # by id
...                 genericSearchResultItem=//android.widget.TextView[@text="%s"]    # can also use [contains(@text"%s")]
...                 bookmarkArticleOption=org.wikipedia:id/article_menu_bookmark  # by id
...                 createNewBookmark=//android.widget.TextView[@text="Create new"]  # by xpath
...                 nameOfBookmarkList=org.wikipedia:id/text_input  # by id
...                 okButton=//android.widget.Button[@text="OK"]    # by xpath
...                 gotItButton=//android.widget.Button[@text="GOT IT"]     # by xpath
...                 cancelButton=//android.widget.Button[@text="CANCEL"]  # by xpath
...                 backButtonOne=//android.widget.ImageButton[@content-desc="Navigate up"]   # by xpath
...                 backButtonTwo=//android.widget.ImageButton    # by xpath
...                 myListsTab=//*[@text="My lists"]  # by xpath
...                 genericListItem=//android.widget.TextView[contains(@text,"%s")]    # by xpath
...                 listMenu=org.wikipedia:id/item_overflow_menu  # by id
...                 deleteListOption=//android.widget.TextView[@text="Delete list"]  # by xpath
...                 exploreTab=//*[@text="Explore"]  # by xpath

${SEARCH_TERM_ONE}   Appium
${SEARCH_TERM_TWO}   Lorem ipsum