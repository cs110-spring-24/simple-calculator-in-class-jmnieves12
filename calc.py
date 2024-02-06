
num1 = int(input("Enter your num 1: "))
op = input("Enter your operator: ")
num2 = int(input("Enter your num 2: "))

if op == "+":
	total = num1 + num2
	print(f"{num1} + {num2} = {total}")

if op == "-":
	total = num1 - num2
	print(f"{num1} - {num2} = {total}")

if op == "*":
	total = num1 * num2
	print(f"{num1} * {num2} = {total}")

if op == "/":
	total = num1 / num2
	print(f"{num1} / {num2} = {total}")

if op == "**":
	total = num1 ** num2
	print(f"{num1} ** {num2} = {total}")

if op == "//":
	total = num1 // num2
	print(f"{num1} // {num2} = {total}")

if op == "%":
	total = num1 % num2
	print(f"{num1} % {num2} = {total}")