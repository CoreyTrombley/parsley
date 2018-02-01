## Parsley
Parsley is a small sample of how to build an API using Django Rest Framework.


<!--## Build status-->
<!--Build status of continus integration i.e. travis, appveyor etc. Ex. - -->

<!--[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)-->
<!--[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)-->

<!--## Code style-->
<!--If you're using any code style like xo, standard etc. That will help others while contributing to your project. Ex. --->

<!--[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)-->
 
## Screenshots
Include logo/demo screenshot etc.
![root api](/images/Screen Shot 2018-02-01 at 11.52.19 AM.png)
![patient api](/images/Screen Shot 2018-02-01 at 11.54.13 AM.png)

## Tech/framework used

<b>Built with</b>
- [Python3](https://www.djangoproject.com/)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)

<!--## Features-->
<!--What makes your project stand out?-->

## Code Example

#### View Patients:

Request:

`http://localhost:8000/patients/`

Response:

```
[
    {
        "url": "http://localhost:8000/patients/1/",
        "first_name": "Radric",
        "middle_name": "Delantic",
        "last_name": "Davis",
        "phones": [
            {
                "type": "mobile",
                "number": "5554443333"
            },
            {
                "type": "office",
                "number": "1112223333"
            }
        ],
        "email": "guwop@fakehost.test",
        "dob": "1980-02-12",
        "age": 37,
        "gender": "male",
        "status": "active",
        "terms_accepted": true,
        "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
        "address": {
            "line_1": "123 Main St",
            "line_2": "Apt 10",
            "city": "Atlanta",
            "state": "GA",
            "zip": "30363"
        }
    }
]
```

#### Create a new patient:

Request:

`http://localhost:8000/patients/`

Body:

```
{
  "first_name": "Radric",
  "middle_name": "Delantic",
  "last_name": "Davis",
  "phones": [
    {
      "type": "mobile",
      "number": "5554443333"
    },
    {
      "type": "office",
      "number": "1112223333"
    }
  ],
  "email": "guwop@fakehost.test",
  "dob": "1980-02-12",
  "age": 37,
  "gender": "male",
  "status": "active",
  "terms_accepted": true,
  "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
  "address": {
    "line_1": "123 Main St",
    "line_2": "Apt 10",
    "city": "Atlanta",
    "state": "GA",
    "zip": "30363"
  }
}
```

Response:

```
{
  "url": "http://localhost:8000/patients/1/",
  "first_name": "Radric",
  "middle_name": "Delantic",
  "last_name": "Davis",
  "phones": [
    {
      "type": "mobile",
      "number": "5554443333"
    },
    {
      "type": "office",
      "number": "1112223333"
    }
  ],
  "email": "guwop@fakehost.test",
  "dob": "1980-02-12",
  "age": 37,
  "gender": "male",
  "status": "active",
  "terms_accepted": true,
  "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
  "address": {
    "line_1": "123 Main St",
    "line_2": "Apt 10",
    "city": "Atlanta",
    "state": "GA",
    "zip": "30363"
  }
}
```

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

### PreReqs

- Install Docker
  - make sure docker is running

### Steps:

1. Clone this Repo
  - SSH: `git clone git@github.com:CoreyTrombley/parsley.git`
  - HTTPS: `git clone https://github.com/CoreyTrombley/parsley.git`
2. Run `docker-compose --build`
  - this will download and start everything you need
> **NOTE:** On initial build the migrations will most likely try to fire before the DB is created, why i'm not sure, but you can simply just kill the compose by running `docker-compose down` in a different terminal window or using `control+c` in the same terminal and restart.
3. Restart if needed due to migrations failing



## API Reference


**Create Patient**
----
  Returns json data about a the newly created patient.

* **URL**

  /patients/

* **Method:**

  `POST`

*  **URL Params**

  None

* **Data Params**

  * **Body** <br />
  **Content:**
  ```
  {
    "first_name": "Radric",
    "middle_name": "Delantic",
    "last_name": "Davis",
    "phones": [
      {
        "type": "mobile",
        "number": "5554443333"
      },
      {
        "type": "office",
        "number": "1112223333"
      }
    ],
    "email": "guwop@fakehost.test",
    "dob": "1980-02-12",
    "age": 37,
    "gender": "male",
    "status": "active",
    "terms_accepted": true,
    "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
    "address": {
      "line_1": "123 Main St",
      "line_2": "Apt 10",
      "city": "Atlanta",
      "state": "GA",
      "zip": "30363"
    }
  }
  ```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    ```
    {
      "url": "http://localhost:8000/patients/1/",
      "first_name": "Radric",
      "middle_name": "Delantic",
      "last_name": "Davis",
      "phones": [
        {
          "type": "mobile",
          "number": "5554443333"
        },
        {
          "type": "office",
          "number": "1112223333"
        }
      ],
      "email": "guwop@fakehost.test",
      "dob": "1980-02-12",
      "age": 37,
      "gender": "male",
      "status": "active",
      "terms_accepted": true,
      "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
      "address": {
        "line_1": "123 Main St",
        "line_2": "Apt 10",
        "city": "Atlanta",
        "state": "GA",
        "zip": "30363"
      }
    }
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    fetch('/patients/', {
      dataType: "json",
      method: "POST",
      body: body,
    })
    .then(resp => resp.json())
    .then(json => console.log(json));
  ```


**List Patients**
----
  Returns json data about a list of patients.

* **URL**

  /patients/

* **Method:**

  `GET`

*  **URL Params**

  None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    ```
    [
      {
        "url": "http://localhost:8000/patients/1/",
        "first_name": "Radric",
        "middle_name": "Delantic",
        "last_name": "Davis",
        "phones": [
          {
            "type": "mobile",
            "number": "5554443333"
          },
          {
            "type": "office",
            "number": "1112223333"
          }
        ],
        "email": "guwop@fakehost.test",
        "dob": "1980-02-12",
        "age": 37,
        "gender": "male",
        "status": "active",
        "terms_accepted": true,
        "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
        "address": {
          "line_1": "123 Main St",
          "line_2": "Apt 10",
          "city": "Atlanta",
          "state": "GA",
          "zip": "30363"
        }
      }
    ]
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    fetch('/patients/', {
      dataType: "json",
      method: "GET",
    })
    .then(resp => resp.json())
    .then(json => console.log(json));
  ```

**Show User**
----
  Returns json data about a single patient.

* **URL**

  /patients/:id

* **Method:**

  `GET`

*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    ```
    {
      "url": "http://localhost:8000/patients/1/",
      "first_name": "Radric",
      "middle_name": "Delantic",
      "last_name": "Davis",
      "phones": [
        {
          "type": "mobile",
          "number": "5554443333"
        },
        {
          "type": "office",
          "number": "1112223333"
        }
      ],
      "email": "guwop@fakehost.test",
      "dob": "1980-02-12",
      "age": 37,
      "gender": "male",
      "status": "active",
      "terms_accepted": true,
      "terms_accepted_at": "2018-02-01T16:53:53.610314Z",
      "address": {
        "line_1": "123 Main St",
        "line_2": "Apt 10",
        "city": "Atlanta",
        "state": "GA",
        "zip": "30363"
      }
    } 
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ "detail": "Not found." }`

* **Sample Call:**

  ```javascript
    fetch(`/patients/${id}/`, {
      dataType: "json",
      method: "GET",
    })
    .then(resp => resp.json())
    .then(json => console.log(json));
  ```

<!--## Tests-->
<!--Describe and show how to run the tests with code examples.-->

<!--## How to use?-->
<!--If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.-->

<!--## Contribute-->

<!--Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus.-->

<!--## Credits-->
<!--Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project. -->

<!--#### Anything else that seems useful-->

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [CoreyTrombley](https://github.com/CoreyTrombley/)
