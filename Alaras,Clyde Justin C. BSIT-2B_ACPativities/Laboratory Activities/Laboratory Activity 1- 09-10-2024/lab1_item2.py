
char1, char2 = input("Enter two space-separated characters: ").split()

greater_char = max(char1, char2)


print("---------------------------------------------")
print(f"The character with greater value is: {greater_char}")
print("---------------------------------------------")

# Optional: Show the ASCII values using ord()
print("Showing ASCII Values:")
print(f"{char1} : {ord(char1)}")
print(f"{char2} : {ord(char2)}")