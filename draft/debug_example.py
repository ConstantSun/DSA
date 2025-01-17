import random

def average(d, n):
    avg = d/n
    return avg

def running_average(numbers):
    avgs = []
    total = 0
    for i, num in enumerate(numbers):
        total += num
        current_avg = average(total, i+1)
        avgs.append(current_avg)
    return avgs

def highest_running_average(numbers):
    averages = running_average(numbers)
    return max(averages)

def generate_numbers(n):
    return random.sample(range(1,300), n)

if __name__ == "__main__":
    nums = generate_numbers(100)
    print("Numbers: ", nums)
    print("Running average: ", running_average(nums))
    print("Highest average: ", highest_running_average)
