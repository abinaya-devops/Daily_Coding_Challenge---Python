Day 02 — Python Learning 🐍

🎯 What I Practiced

Today, I completed the Email Sorter challenge on freeCodeCamp's Daily Coding Challenge.

I practised solving the problem step by step, understanding each concept before writing the code.

📚 Concepts Practiced

- Python functions and parameters
- String methods: "split()" and "lower()"
- List indexing: "parts[0]" and "parts[1]"
- Tuples for multiple sorting criteria
- The "sorted()" function
- Custom sorting using the "key" parameter
- Case-insensitive comparisons
- Preserving original email address casing

🧠 What I Learned

I learned how to separate an email address into its username and domain using "split("@")".

I understood that "parts[0]" represents the username and "parts[1]" represents the domain.

I used "lower()" to compare email addresses without considering uppercase and lowercase differences.

I also learned how to return a tuple containing "(domain, username)" so that emails are sorted by domain first and username second.

Using "sorted(emails, key=get_sort_key)" helped me understand how Python can sort a list using a custom sorting function while preserving the original email addresses.

🐛 Learning and Problem-Solving Experience

Initially, I found it challenging to understand why a helper function was needed inside the main function and how the "key" parameter worked.

I practised each concept with small questions and examples before putting the code together.

This step-by-step approach helped me understand the sorting logic instead of simply copying the solution.

💻 Solution

def sort(emails):
    def get_sort_key(email):
        parts = email.split("@")
        username = parts[0].lower()
        domain = parts[1].lower()
        return (domain, username)

    return sorted(emails, key=get_sort_key)

✅ Result

- Completed the Email Sorter challenge successfully.
- Passed all test cases on freeCodeCamp.
- Saved the solution, README notes, and screenshot in GitHub.

🌱 Next Goal

Continue practising Python coding challenges, strengthen my understanding of functions and sorting, and improve my problem-solving skills through hands-on practice.
