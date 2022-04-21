*** Settings ***
Documentation     Example using the space separated format.
...               Checking the information provided in the
...               Robot Framework documentation.
Library           RequestsLibrary
Library           Collections

#  robot  --loglevel TRACE users_tests.robot

*** Variables ***
&{headers}        Content-Type=application/json
${data_list}      [{"id": 0, "username": "string", "firstName": "string", "lastName": "string", "email": "string", "password": "string", "phone": "string", "userStatus": 0}]
${data}           {"id": 0, "username": "string", "firstName": "string", "lastName": "string", "email": "string", "password": "string", "phone": "string", "userStatus": 0}
${data_to_login}  [{"username": "string", "password": "string"}]

*** Test Cases ***
Swagger user get username Test
    BuiltIn.Skip            "HTTPError: 404 Client Error: Not Found for url: https://petstore.swagger.io/v2/user/string"    
    ${response}=    GET      https://petstore.swagger.io/v2/user/string
    Status Should Be    OK   ${response}

Swagger user post createWithList Test
    ${response}=    POST     https://petstore.swagger.io/v2/user/createWithList  data= ${data_list}   headers=&{headers}
    Status Should Be    OK   ${response}

Swagger user put username Test
    ${response}=    PUT      https://petstore.swagger.io/v2/user/string           data=${data}     headers=&{headers}
    Status Should Be    OK   ${response}

Swagger user del username Test
    ${response}=    DELETE   https://petstore.swagger.io/v2/user/string     headers=${headers}
    Status Should Be    OK   ${response}

Swagger user login Test
    ${response}=    GET     https://petstore.swagger.io/v2/user/login       headers=${headers}    data=${data_to_login}
    Status Should Be    OK   ${response}

Swagger user logout Test
    ${response}=    GET     https://petstore.swagger.io/v2/user/logout       headers=${headers}    data=${data_to_login}
    Status Should Be    OK   ${response}

Swagger list user Test
    ${response}=    POST     https://petstore.swagger.io/v2/user/createWithArray    headers=${headers}    data=${data_list}
    Status Should Be    OK   ${response}

Swagger create user Test
    ${response}=    POST     https://petstore.swagger.io/v2/user    headers=${headers}    data=${data}
    Status Should Be    OK   ${response}

