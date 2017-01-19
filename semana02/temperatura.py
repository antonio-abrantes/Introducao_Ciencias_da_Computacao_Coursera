import locale
tempF = float(input())

tempC = (tempF - 32) / 1.8

print("Teperatura em Celsius:", locale.format("%.2f", tempC)+"º")