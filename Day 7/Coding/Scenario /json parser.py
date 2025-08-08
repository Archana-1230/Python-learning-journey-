#JSON Parser
data = {
    "user": {
        "name": "John Doe",
        "contact": {"email": "john@example.com", "phone": "1234567890"}
    }
}

print("Email:", data["user"]["contact"]["email"])

#Output:Email: john@example.com
