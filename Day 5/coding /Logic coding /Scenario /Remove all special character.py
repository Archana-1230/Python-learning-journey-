"""You’re building a chat app. You need to remove emojis and unwanted symbols from user messages.
"""
import re
text = input("Enter chat message: ")
cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print("Cleaned message:", cleaned)
"""
input:
Enter chat message: Hey!! 😊 How's it going??? 💬🔥
output:Cleaned message: Hello JohnDoe123 Are you coming
"""