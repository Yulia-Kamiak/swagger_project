*** Settings ***
Documentation     Example using the space separated format.
...               Checking the information provided in the
...               Robot Framework documentation.
Suite setup       Setup Pet Tests
Library           RequestsLibrary
Library           Collections
Library           BuiltIn

#  robot  --loglevel TRACE pet_tests.robot

*** Variables ***
&{headers}        Content-Type=application/json


*** Keywords ***
Setup Pet Tests
    ${order_id} =  evaluate  random.randint(1,5)  random
    set suite variable    ${order_id}  ${order_id}
    ${data_pet} =  evaluate  {"id": ${order_id}, "category": {"id": ${order_id}, "name": "string"},
    "name": "doggie", "photoUrls": ["string"], "tags": [{"id": ${order_id}, "name": "string" }], "status": "available"}
    set suite variable  ${data_pet}  ${data_pet}

*** Test Cases ***
Swagger add new pet Test
    ${response}=    POST      https://petstore.swagger.io/v2/pet     json=${data_pet}       headers=&{headers}
    Status Should Be    OK   ${response}

Swagger update pet Test
    ${response}=    PUT      https://petstore.swagger.io/v2/pet     json=${data_pet}       headers=&{headers}
    Status Should Be    OK   ${response}

Swagger find pet Test
    ${response}=    GET      https://petstore.swagger.io/v2/pet/findByStatus
    Status Should Be    OK   ${response}

Swagger find pet by id Test
    ${response}=       GET      https://petstore.swagger.io/v2/pet/${order_id}
    Status Should Be    OK   ${response}

Swagger update pet by form Test
    ${response}=       POST      https://petstore.swagger.io/v2/pet/${order_id}
    Status Should Be    OK   ${response}

Swagger delete pet Test
    ${response}=       DELETE      https://petstore.swagger.io/v2/pet/${order_id}
    Status Should Be    OK   ${response}

Swagger update image Test
    ${file} =  Get File For Streaming Upload  ./data/f2637562392edd24809a100a0211e6f8-symbols-design-logo-icon-design.jpg
    ${files} =  create dictionary  file=${file}
    ${headers} =  create dictionary  Content-Type=multipart/form-data  accept=application/json
    ${response}=       POST      https://petstore.swagger.io/v2/pet/${order_id}/uploadImage  files=${files}
    Status Should Be    OK   ${response}
