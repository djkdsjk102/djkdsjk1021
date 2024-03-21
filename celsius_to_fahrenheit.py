def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius.
        
    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

# 获取用户输入的摄氏度
celsius = float(input("Enter temperature in Celsius: "))

# 调用 celsius_to_fahrenheit 函数转换摄氏度为华氏度
fahrenheit = celsius_to_fahrenheit(celsius)

# 打印转换后的华氏度
print(f"Temperature in Fahrenheit: {fahrenheit}°F")
