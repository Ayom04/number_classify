# Number Classification API

## Overview

The **Number Classification API** allows users to input a number and retrieve mathematical properties about it, including whether it is prime, perfect, or an Armstrong number. It also provides a fun fact about the number using the **Numbers API**.

## Features

- checks if a number is prime
- checks if a number is perfect
- checks if a number is an Armstrong number
- calculates the digit sum of a number
- fetches a fun fact about the number
- caches error information for invalid inputs.

## Technology Stack

- **FastAPI** (Python Web Framework)
- **Requests** (For fetching fun facts)

## API Endpoints

### **Classify a Number**

#### **Request**

`GET /api/classify-number?number=<integer>`

#### **Query Parameters**

| Parameter | Type   | Required | Description            |
| --------- | ------ | -------- | ---------------------- |
| `number`  | string | Yes      | The number to classify |

#### **Successful Response (200 OK)**

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### **Error Response (400 Bad Request - Invalid Input)**

```json
{
  "number": "hg",
  "error": true
}
```

## Installation & Setup

### **1. Clone the Repository**

```sh
git clone <repo_url>
cd number-classification-api
```

### **2. Create a Virtual Environment (Optional)**

```sh
python -m venv venv
source venv/bin/activate  # On mac or linux
```

### **3. Install Dependencies**

```sh
pip install fastapi uvicorn requests
```

### **4. Run the API Server**

```sh
uvicorn main:app --reload
```

### **5. Access the API**

- Open your browser or use Postman to test: `http://127.0.0.1:8000/api/classify-number?number=371`
