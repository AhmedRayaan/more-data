def generate_url(numbers):
    base_url = "https://www.youtube.com/watch?v=Ywm3P0MxAvQ"
    # Assuming the numbers are provided as a list
    # Joining the numbers with "-" to form the path in the URL
    path = "-".join(map(str, numbers))
    return base_url + path

numbers_input = input("Enter a set of numbers separated by spaces: ")
# Splitting the input string into a list of numbers
numbers = list(map(int, numbers_input.split()))
url = generate_url(numbers)
print("Generated URL:", url)

