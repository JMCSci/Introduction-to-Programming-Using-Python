''' Chapter 5.9 '''

tuition = 10000;
PERCENT_INCREASE = 0.05;
totalCost = 0;
totalCostFourYears = 0;
tuitionTenYears = 0;

for i in range(1,14):
    tuition += tuition * PERCENT_INCREASE;
    if(i == 9):
        totalCostFourYears = tuitionTenYears = tuition;
    if(i > 9):
        totalCostFourYears += tuition;
          
print("The tuition in ten years is",tuitionTenYears);
print("The total cost of four years of tuition starting in Year 10 is", \
      totalCostFourYears);