''' Chapter 5.3 '''

KILOGRAMS_TO_POUNDS = 2.2;
i = 1;

print("Kilograms    Pounds");

while(i < 200):
    conversion = i * KILOGRAMS_TO_POUNDS;
    print(format(i, ">2.0f"), format(conversion, ">16.1f"));
    i += 2;