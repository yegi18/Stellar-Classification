# Stellar-Classification
•	The data set had 6 columns:
1.	Temperature
2.	Luminosity
3.	Radius
4.	Absolute magnitude
5.	Star type
6.	Star colour
7.	Spectral class
•	The temperature is determined by the wavelength of the incoming light using black body radiation
•	Hence, the raw input from the telescope which include the position, brightness and colour of the star is used to quantitatively derive the temperature, luminosity, Radius and absolute magnitude 
•	The model is a supervised learning one used to predict the star type.
•	The star types:
1.	Brown Dwarf (0)
2.	Red Dwarf (1)
3.	White Dwarf (2)
4.	Main Sequence (3)
5.	Super Giant (4)
6.	Hyper Giant (5)

•	The star type classification primarily depends on the Temperature, Absolute magnitude, Luminosity and Radius.
•	From observation, Brown Dwarfs have less radius and Hyper Giant has a higher radius. In fact, the radius increases as you go from the 1st star type to the last one.
•	The model uses the Random Forest algorithm for classification.
•	75% of the data was used for training and the 25% as testing data set.
•	The number of trees or estimators were increased by multiples of 10 to arrive at a value of 100 so that the error was minimum and the model could potentially give the same accuracy for larger data sets.
•	The model gave close to 100% accuracy for the given training data set.


•	A supervised learning model to predict the spectral class of the star.
•	The spectral class is a classification-based value of the surface temperature of the star. 
•	The classes are O (0), B (1), A (2), F (3), G (4), K (5), M (6)
•	From observation of the data set, the star surface temperature decreases in the above-mentioned order, with stars of high temperatures in the range of 20,000-30,000 K given O class and stars with lower surface temperature in the range of 1000-3000 K given M class.
•	The model uses Random Forest algorithm for classification.
•	As is with the star type, 75% of the data is used for training and the 25% for testing.
•	The number of estimators was 100 and the model gave close to 100% accuracy.
