I calculated the chances of winning a bet, and the bet was based on the chance to reach the step 60 or more of the empire state building based on the outcome of the roll of a dice. 
Solution Process:
I simulated multiple random walks (precisely 500 simulations), where in each walk the dice was rolled 100 times. Depending on the outcome of the dice the person will go up or down the steps of the empire state building. 
Details of the Rule ans steps:
1. If the dice shows digit <=2 then the person will go one step down, but the person should not go below step zero. 
2. If the dice shows digit <= 5 but >2, then the person will go one step up. 
3. If the dice shows digit = 6, then the dice is rolled again then the person will go up the steps equal to the number shown on the dice in another throw. 
4. There is a 0.1% chance that the person is clumsy and will fall from the empire state building while climbing up the steps, in that case the person has to start again from zero step. 
5. I saved the result of all the 100 walks in a list, and the 500 simulations of all the 100 random walks was saved in a list of lists. 
6. To find the end point of the 500 simulations, I changed the list of lists to an array, transposed it and calculated the number of time the end points has value more than or equal to 60. 
7. Visualized the distribution of the 500 end points using histograms. 
8. Finally, I divided the result with 500 to get the chance of 78.4% that the person will reach on the step 60 or more of the empire state building.
