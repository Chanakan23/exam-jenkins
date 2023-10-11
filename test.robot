***Settings***
Library           RequestsLibrary

***Test Cases***
is_leap_year
    ${response}=    Get    http://127.0.0.1:5000/is_leap_year/1600
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal As Strings    ${response.content}    True
    ${response}=    Get    http://127.0.0.1:5000/is_leap_year/2001
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal As Strings    ${response.content}    False
    ${response}=    Get    http://127.0.0.1:5000/is_leap_year/2400
    Should Be Equal As Integers    ${response.status_code}    200
    Should Be Equal As Strings    ${response.content}    True
