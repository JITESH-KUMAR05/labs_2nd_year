# bPay = int(input("Enter salary or basic pay: "))

# salary = (bPay + (bPay*0.8)+(bPay*0.3-(bPay*0.12)))

# print("Your salary is: ", salary)
# for i in range(0,-2,-1):
    # print(i)
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours}:{minutes}:{remaining_seconds}"

# Example usage
input_seconds = 25300
output = convert_seconds(input_seconds)
print(output)  # Output: 7:1:40