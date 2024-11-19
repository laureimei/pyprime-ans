def Unit2_add1to10():
    total = 0  # Initialize the total sum
    count = 1  # Start counting from 1

    # While loop to add numbers from 1 to 10
    while count <= 10:  # The condition must eventually be false
        total += count  # Add the current number to total
        count += 1  # Move to the next number (this is crucial to avoid an infinite loop)

    print(total)  # Print the final total


# Call the function to see the result
Unit2_add1to10()  # This will print 55
