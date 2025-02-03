from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


class ClasifyNumber:
    def __init__(self, number):
        self.number = number

    def is_prime(self) -> bool:
        """_summary_
        Check if a number is prime.

        Args:
            n (int): _description_

        Returns:
            bool: _description_

        1. Get the number, n.
        2. if it's 1 or less than 1, return False
        3. loop through the numbers from 2 to n+1, 
        4. if any number divides n without a remainder, return False
        5. return True
        To optimize performance and reduce the number of iterations, we can loop through the numbers from 2 to the square root of n.
        """
        if self.number <= 1:
            return False

        for i in range(2, int(self.number**0.5)+1):
            if self.number % i == 0:
                return False

        return True

    def is_armstrong(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        1. Convert the number to a string
        2. Convert each digit in the string to an integer and store in a list
        3. Calculate the sum of each digit raised to the power of the length of the list
        4. if the sum is equal to the original number, return True
        5. return False

        """
        digits = [int(d) for d in str(self.number)]
        return sum(d ** len(digits) for d in digits) == self.number

    def get_properties(self) -> list:
        """_summary_

        Returns:
            list: _description_

        1. Check if the number is an armstrong number
        2. Check if the number is odd or even
        3. return a list of the properties that are True

        """
        properties = ["armstrong" if self.is_armstrong(
        ) else "", "odd" if self.number % 2 != 0 else "even"]
        return [p for p in properties if p]

    def is_perfect(self) -> bool:
        """_summary_
        Check if a number is perfect.

        Args:
            n (int): _description_

        Returns:
            bool: _description_

        1. Get the number, n.
        2. if it's 1 or less than 1, return False
        3. initialize a variable, sum_divisors, to 1
        4. loop through the numbers from 2 to n//2+1
        5. if any number divides n without a remainder, add it to sum_divisors
        6. if sum_divisors is equal to n, return True
        7. return False
        """
        if self.number <= 1:
            return False

        sum_divisors = 1
        for i in range(2, self.number//2+1):
            if self.number % i == 0:
                sum_divisors += i

        return sum_divisors == self.number

    def digit_sum(self) -> int:
        """_summary_
        Calculates the sum of digits of a given number.

        Args:
            n (int): _description_

        Returns:
            int: _description_

        1. find the absolute value of n
        2. convert n to a list of digits
        3. return the sum of the digits in the list
        """
        number = abs(self.number)
        number_list = [int(digit) for digit in str(number)]
        return sum(number_list)

    def fun_fact(self) -> str:
        """_summary_

        Returns:
            str: _description_

        1. Make a get request to the numbersapi.com API with the number and the math endpoint
        2. return the response text if the status code is 200, else return "No fun fact for you"
        """
        response = requests.get(f"http://numbersapi.com/{self.number}/math")
        return response.text if response.status_code == 200 else "No fun fact for you"

    def classify(self):
        return {
            "number": self.number,
            "is_prime": self.is_prime(),
            "properties": self.get_properties(),
            "is_perfect": self.is_perfect(),
            "digit_sum": self.digit_sum(),
            "fun_fact": self.fun_fact()
        }


@app.get("/api/classify-number")
def get_number_classes(number: str):
    if not number.isdigit():
        return {
            "number": number,
            "error": True
        }

    num = int(number)
    classifier = ClasifyNumber(num)
    return classifier.classify()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
