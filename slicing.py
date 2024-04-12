temps = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temps2 = temps[7:14]
print(temps2)


temperatures = [72, 75, 78, 100, 79, 100, 80, 81, 100, 82, 83, 100, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]


hundies = [temp for temp in temperatures if temp == 100]
                                                                  #i like inline statements becuase there cleaner
print(hundies)
