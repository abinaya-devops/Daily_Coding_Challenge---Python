
def sort(emails):
    def get_sort_key(email):
        parts = email.split("@")
        username = parts[0].lower()
        domain = parts[1].lower()
        return (domain, username)

    return sorted(emails, key=get_sort_key)
  
