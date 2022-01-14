#First basic project
#First adult
age = 28
sex = 0
bmi = 26.2
child = 3
smoker = 0

#Calculating insurance
insuranceCost = 250*age - 128*sex + 370*bmi + 425*child + 24000*smoker - 12500

#outputting the insurance cost
print("This person's insurance cost is " + str(int(insuranceCost)) + "\n")

#updating age
age += 4

#updating cost
newInsuranceCost = 250*age - 128*sex + 370*bmi + 425*child + 24000*smoker - 12500

#insurance change from age
insuranceChange = newInsuranceCost - insuranceCost


#print the change in the insurance costs
print("The change in insurance after aging 4 years is $" + str(int(insuranceChange)) + "\n")

#updating bmi
age = 28
bmi += 3.1

#updating cost
newInsuranceCost = 250*age - 128*sex + 370*bmi + 425*child + 24000*smoker - 12500
insuranceChange = newInsuranceCost - insuranceCost

print("The change in insurance after increasing bmi by 3.1 is $" + str(int(insuranceChange)) + "\n")

#male vs. female
bmi = 26.2
sex = 1
newInsuranceCost = 250*age - 128*sex + 370*bmi + 425*child + 24000*smoker - 12500
insuranceChange = newInsuranceCost - insuranceCost

print("The change in cost between male and female is $" + str(insuranceChange) + "\n")