price = 62;

if price >= 80:
    print("That's way too expensive...");
elif price <= 40:
    print("That is too cheap, the quality will not be good.");
else:
    print("Heck yeah! Go ahead and buy the dang thing!");


temperature = 40;
forecast = "rainy";

# Using and operator
if temperature <= 90 and temperature >= 50 and forecast != "rainy":
    print("Go outside!");
elif temperature <= 90 and temperature >= 50 and forecast == "rainy":
    print("Take an umbrella!");
else:
    print("Maybe just stay home...")