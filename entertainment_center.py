import media as md
import fresh_tomatoes

#initiate instance for movies
pfiction = md.Trailer("Pulp Fiction", "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption"
                      , "https://i.imgur.com/3llONDs.png",
                      "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

rDogs = md.Trailer("Reservoir Dogs",
                   "After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.",
                   "https://i0.wp.com/www.la-screenwriter.com/wp-content/uploads/2013/04/reservoir_dogs_1992_8.jpg?resize=682%2C1024",
                   "https://www.youtube.com/watch?v=vayksn4Y93A")

scarface = md.Trailer("Scarface",
                      "In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.",
                      "https://i.imgur.com/Gbt8aKP.jpg",
                      "https://www.youtube.com/watch?v=cv276Wg3e7I")

serpico = md.Trailer("Serpico",
                     "An honest New York cop named Frank Serpico blows the whistle on rampant corruption in the force only to have his comrades turn against him.",
                     "https://i.imgur.com/M8Py9QI.png",
                     "https://www.youtube.com/watch?v=nBJQ1pK372Q")

dknight = md.Trailer("The Dark Knight",
                     "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                     "https://i.imgur.com/oRueeKN.png",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")
#creates a list of movie for the website with the data created above
movies = [pfiction,rDogs,scarface,serpico,dknight]

#launches the website
fresh_tomatoes.open_movies_page(movies)