*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  hyvanimi
    Set Password  hyvasana10
    Set Password Confirmation  hyvasana10
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  hy
    Set Password  hyvasana10
    Set Password Confirmation  hyvasana10
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long.


Register With Valid Username And Too Short Password
    Set Username  hyvanimi
    Set Password  hyva
    Set Password Confirmation  hyva
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long.


Register With Valid Username And Invalid Password
    Set Username  hyvanimi
    Set Password  hyvasana
    Set Password Confirmation  hyvasana
    Submit Registration
    Registration Should Fail With Message  Password must include at least one non-letter character.


Register With Nonmatching Password And Password Confirmation
    Set Username  yvanimi
    Set Password  hyvanimi10
    Set Password Confirmation  vaaranimi10
    Submit Registration
    Registration Should Fail With Message  Password and confirmation must match.


Register With Username That Is Already In Use
    Set Username  hyvanimi
    Set Password  hyvasana10
    Set Password Confirmation  hyvasana10
    Submit Registration
    Registration Should Succeed
    Set Username  hyvanimi
    Set Password  toinennimi10
    Set Password Confirmation  toinennimi10
    Submit Registration
    Registration Should Fail With Message  Username is already taken.


Login After Successful Registration
    Register New User  uusinimi  uusisana11
    Logout
    Go To Login Page
    Set Username  uusinimi
    Set Password  uusisana11
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Attempt Registration  jokunimi  j
    Go To Login Page
    Set Username  jokunimi
    Set Password  j
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page