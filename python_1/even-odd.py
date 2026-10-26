# ==========================================
# Program: Even or Odd Number Detector
# ==========================================

# 1. FUNCTION: A reusable block of code that does one specific job
def even_odd(number):
    # The '%' symbol (modulo) finds the remainder of a division.
    # If you divide a number by 2 and the remainder is 0, it is even!
    if number % 2 == 0:
        return True       # DATA TYPE 1: Boolean (True)
    else:
        return False      # DATA TYPE 1: Boolean (False)

# 2. VARIABLES & DATA TYPES
# DATA TYPE 2: Integers (whole numbers) stored inside a list variable
mr_beast = [89, 16, 19, 904, 47730]

# 3. LOOP: This 'for' loop goes through our list of numbers one by one
for every_num in mr_beast:
    
    # We pass the current number into our function to test it
    check_result = even_odd(every_num)
    
    # Using an 'if' statement to read our Boolean result
    if check_result == True:
        # DATA TYPE 3: String (text surrounded by quotes)
        message = "Even"
    else:
        message = "Odd"
        
    # Print the final message to the screen
    print(f"The number {every_num} is {message}!")
