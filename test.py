import time

def print_overwrite(message, line_number):
    # Move the cursor to the beginning of the line
    print(f"\r\033[K", end="")
    # Print the new message
    print(message, end="")
    # Move the cursor back to the original line
    print(f"\033[F" * line_number, end="")

# Number of lines in the output
num_lines = 5

for i in range(10):
    for j in range(num_lines):
        message = f"Processing item {i} on line {j}"
        print_overwrite(message, line_number=j)
        time.sleep(0.5)  # Simulate some processing time

print("\nProcessing complete!")  # Move to a new line after the loop finishes
