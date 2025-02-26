# Dictionary Comprehension - User Data Processing

users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,"Chicago")]

print({name: age for name, age, city in users if age > 18})