 AW Academy Assignment
 
Taco fredag
 
Vi alle elsker taco fredag og jeg lagde en applikasjon som er bygd p� Python og SQL og som kj�res op terminal vindu p� datamaskinen.

For � starte programmet m� brukeren navigere til 
Assignment\venv\shoppinglist.py


Package jeg brukte for applikasjonen er:

- sqlite3  	version 1.25.9
- tabulate 	version 0.8.7
- os
- pandas 		version 1.0.3
- csv
- seaborn 		version 0.10.1
- matplotlib	version 3.2.1
		
For � s�rge for at alle pakkene f�lger med anbefaler jeg at brukeren kj�erer pip install Requirements.txt som man finner under assignment/Requirements.txt




 
Step 1: N�r man starter applikasjonen Shoppinglist.py blir brukeren spurt om hans budsjett. Budsjettet er en float type.

 
Step 2: Deretter kommer det opp en liste med muligheter p� hva brukeren kan gj�re, og blir spurt om hva han vil gj�re. 


Liste over oprasjonen som kan gj�res av brukeren
 
Brukeren vil f� opp en liste med hva han vil gj�re. Det hvite listen er oprasjoner som vises i terminalen mens det gule er grafer. 


Mappe struktur

Selve koden ligger under mappen venv/shoppinglist.py

asset innholder flere under mapper. 

csv: 	Mappen inneholder filer som jeg lagde av koden fra dataen 	fra database. Disse filene brukte jeg for � lage grafer. 

PS:  Jeg kunne enkelt brukt dataen direkte fra databasen men  	valgte � gj�re det p� den m�ten for jeg ville l�re meg 	hvordan man kan gj�re det. 

database: Er mappen som inneholder selve databasen.

images: I denne mappen lagrer jeg bilder fra grafene. Det er for 	   senere jeg kan bruke disse bildene til dokumentasjoner 	   	   og lignede. 

Logo:	Logo mappen inneholder start og slutt logoen for 	applikasjonen. det er bilder i ASCII

Grafere og beskrivelesen p� dem
Prices grafen: 
Denne grafen viser hvor mye v�rt produkt koster.

Budget grafen:
 
Denne grafen viser hvor mye alt vil koste, hva budgetet er og hvor mye brukeren har igjen etter han/hun. Nedest i r�d ser brukeren regnestukket. 