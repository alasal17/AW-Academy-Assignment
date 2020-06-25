 AW Academy Assignment
 
Taco fredag
 
Vi alle elsker taco fredag og jeg lagde en applikasjon som er bygd på Python og SQL og som kjøres op terminal vindu på datamaskinen.

For å starte programmet må brukeren navigere til 
Assignment\venv\shoppinglist.py


Package jeg brukte for applikasjonen er:

- sqlite3  	version 1.25.9
- tabulate 	version 0.8.7
- os
- pandas 		version 1.0.3
- csv
- seaborn 		version 0.10.1
- matplotlib	version 3.2.1
		
For å sørge for at alle pakkene følger med anbefaler jeg at brukeren kjøerer pip install Requirements.txt som man finner under assignment/Requirements.txt




 
Step 1: Når man starter applikasjonen Shoppinglist.py blir brukeren spurt om hans budsjett. Budsjettet er en float type.

 
Step 2: Deretter kommer det opp en liste med muligheter på hva brukeren kan gjøre, og blir spurt om hva han vil gjøre. 


Liste over oprasjonen som kan gjøres av brukeren
 
Brukeren vil få opp en liste med hva han vil gjøre. Det hvite listen er oprasjoner som vises i terminalen mens det gule er grafer. 


Mappe struktur

Selve koden ligger under mappen venv/shoppinglist.py

asset innholder flere under mapper. 

csv: 	Mappen inneholder filer som jeg lagde av koden fra dataen 	fra database. Disse filene brukte jeg for å lage grafer. 

PS:  Jeg kunne enkelt brukt dataen direkte fra databasen men  	valgte å gjøre det på den måten for jeg ville lære meg 	hvordan man kan gjøre det. 

database: Er mappen som inneholder selve databasen.

images: I denne mappen lagrer jeg bilder fra grafene. Det er for 	   senere jeg kan bruke disse bildene til dokumentasjoner 	   	   og lignede. 

Logo:	Logo mappen inneholder start og slutt logoen for 	applikasjonen. det er bilder i ASCII

Grafere og beskrivelesen på dem
Prices grafen: 
Denne grafen viser hvor mye vært produkt koster.

Budget grafen:
 
Denne grafen viser hvor mye alt vil koste, hva budgetet er og hvor mye brukeren har igjen etter han/hun. Nedest i rød ser brukeren regnestukket. 