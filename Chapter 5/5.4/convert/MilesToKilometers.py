''' Chapter 5.4 '''


MILES_TO_KILOMETERS = 1.609;

print("Miles", format("Kilometers", ">18s"));

for i in range(1, 11):
    conversion = i * MILES_TO_KILOMETERS;
    print(format(i, "<2.0f"), (format(conversion, ">17.3f")));
    
