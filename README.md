#Problem

Problemet jag vill försöka lösa är att klassificera i fall en svamp är giftig eller ej. Eftersom jag 
måste dela in dem i två kategorier är detta ett klassifieringsproblem. 

#Data

• Är det komplett?
• Har du null-värden?

Nej datasetet inte helt är komplett. Jag har använt isNull funktionen för att leta efter tomma värden.
Det finns inte några nullvärden i datasetet. Det finns dock ett par kolumner där teckenet "?" avnänds.
I dokumentationen på kaggle står det att "?" = missing vilket betyder att vi saknar dessa helt.
Dessa värden utgör ändå en stor del i den kolumnen men det kanske inte är kritiskt. Jag kan 
kanske utesluta den kolumnen ifall den inte är viktig för att klassificera. Man kan också byta ut 
dem mot ett annat vanligt förekommande värde eller ta bort de tomma raderna.

```
Kolumn stalk_root unika värden:
stalk_root
b             3776
?             2480
e             1120
c              556
r              192
stalk-root       1
Name: count, dtype: int64
```

• Har du extrema värden?

I vissa av kolumnerna har jag ganska stor skilnad i mina värden. T.ex i cap_surface:

```
y              3244
s              2556
f              2320
g                 4
```

Här är g = grooves väldigt ovanligt jämfört med de andra värdena. Jag hade förväntat mig
detta då det finns vissa svampar med ovanliga attribut som ofta är sällsynta jämfört med de
som delar de mer dominerande attributen. Jag tror inte detta kommer vara ett stort problem 
men man kanske vill ta bort viss data som delar flera ovanliga attribut? 

• Vilka datatyper har datat?

Alla kolumner är objekt. Vi arbetar med strängar och har inga numreriska värden.
• Vilka fält i ditt data vill du använda dig av?

Jag kommer börja med att inkludera alla fält för den första modellen. Sedan kommer jag göra 
research för att se om det finns några tydliga kopplingar mellan atribut och ifall en svamp 
är giftig. Jag kommer även kolla om vissa attribut är vanligt förekommande för giftiga svampar
i datasetet då detta skulle indikera på att detta är viktigare data för att klassificera. T.ex
om formen på hatten hos giftiga svampar ofta är samma kan vi anta att detta är en viktig kolumn
att ha med när vi tränar modellen.

• Hur kan du konvertera alla fält du vill använda till ett numeriskt format?

Jag kan använda one-hot encoding för de kolumner där datan inte har en naturlig ording, 
vilket är alla kolumner i det här datasetet. Vissa värden mappar jag själv.

När jag bygger modelllen kommer jag köra supervised learning. Jag behöver inte köra unsupervised 
då jag redan har labels. Reinforcement passar inte här då vi inte har någon miljö där vi kan 
belöna/bestraffa val. Jag kommer prova bygga min model med beslutsträd men även prova regrission då det 
kan finnas tydlig separation i datan. Jag kommer börja med att använda scikit-learn som en första modell.

 



