Day 10 – Python Learning (November 7, 2026)

🐍 Challenge: Weekday Finder

Problem Statement

Given a date string in the format "YYYY-MM-DD", return the corresponding day of the week.

💻 Python Solution

from datetime import datetime

def get_weekday(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    weekday = date.strftime("%A")
    return weekday

📚 Concepts Practiced

1. datetime Module: Used Python's built-in datetime module to work with dates and times.
2. strptime(): Converted a date string into a datetime object.
3. strftime(): Extracted the full weekday name from a date.
4. Date Formatting:
   - "%Y" – Four-digit year
   - "%m" – Two-digit month
   - "%d" – Two-digit day
   - "%A" – Full weekday name
5. return: Returned the calculated weekday from the function.

🧠 What I Learned

- A date inside quotation marks is initially treated as a string.
- "strptime()" converts a string into a datetime object.
- "strftime()" formats a date into the required string representation.
- The difference between "strptime()" and "strftime()".
- How to use Python's built-in modules to solve date-related problems.

🔍 Debugging Experience

Initially, I found the datetime module and its methods confusing.

I learned the concepts step by step and understood how string-to-date conversion and weekday extraction work.

After understanding the logic, I independently wrote the solution and submitted it to freeCodeCamp.

🎯 Result

Status: Completed – All 5/5 Tests Passed!

Successfully completed the Weekday Finder challenge by understanding and implementing Python datetime concepts.

🚀 Next Goal

Continue practicing Python problem-solving challenges and improve logical thinking and coding confidence.

Platform: freeCodeCamp
Language: Python
Challenge: Weekday Finder
