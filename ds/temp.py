def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result
temps = [30,45,67,58,88,90,23,45,67]
print(daily_temperatures(temps))
