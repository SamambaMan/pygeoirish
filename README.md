# pygeocoder

## Development Process

Well, first of all, downloaded all the data sets included in the task, hoping to get a better grasp of the available data and, therefore, aditional information to fulfill the task.

After some visual analysis of the address_for_task.csv file, could find usual problems related to user inputed data, misspelings, field positioning, exceeding commas and so on.

Before coding, decided to do some simple regex searches, to get some idea of how hard would it be to complete de task using simple text operations, in random samples.

Simple examples like 

```"Lackagh Beg, Turloughmore, galway"```

, would turn into regexps 

```galway,.+Lackagh Beg``` 

and, voilá, a single result 

```16543,GALWAY,Gaillimh,GALWAY,,Td,Bf,N,,62903,LACKAGH BEG,Leacach Beag,,,141115,235495,541079,735522,,,Fiontar,,```

But of course it wouldn`t be that easy.

Using Google Maps as some sort of benchmark (and also to get more familiar with the irish addressing and geography), the address 'Lackagh Beg, Turloughmore, galway' return is interesting. First, two results indicating a medic facility. But, swapping "Turloughmore" and "Lackagh Beg" returns different locations. Also, even being a "parish", Lackagh Beg won`t show up in the 'parish' file.

So, some data inconsistencies or understanding would need to be addressed in the code.

Also, it was clear that different aproaches would be needed to get a better geocoder, and maybe a non-exact-match would also be interesting.

## Preliminares: garbage removal

A lot of addresses had "road", "lane", some addresses included apostrophes like ```St Mary's Road, Inch, Killarney, kerry``` and also as quotes, like ```'The Glade'```. The double quotes in the beggining and in the end of the file could`t be ignored as well, so my first attempt was to build a simple regular expression to get rid of theese and do some word trimming.

```
    terms = r"ROAD|LANE|SQUARE|'|\""
    term = re.sub(terms, '', term)
```

This proved to be very misleading. As the "road" level of the data isn`t available in the datasets, removing this specificiality indicator would lead to mistakes. ```Moneen Road , Castlebar, mayo``` after word removal and using the previous regexp would return ```32053,MAYO,Maigh Eo,MAYO,,Td,Bf,N,,152544,MONEEN,An Móinín,,,114879,332055,514849,832061,,,Fiontar,,```. seems misleading. Castlebar is an actual local area name, present in the 'Centres of Population' and 'Electoral Districts' files, but not in the 'Townsland' file.

Also, by the data and this logic, this would return two lines:

```
32053,MAYO,Maigh Eo,MAYO,,Td,Bf,N,,152544,MONEEN,An Móinín,,,114879,332055,*514849,832061*,,,Fiontar,, 
(54.23033731886605, -9.30600264016595) - seems wrong, north of Belsallagh
32054,MAYO,Maigh Eo,MAYO,,Td,Bf,N,,152545,MONEEN,An Móinín,,,82055,281030,482031,781048,,,Fiontar,,
(53.76566422249623, -9.789349579835276) - seems wrong, east of Louisburgh
```

A more suitable address would be:

```
1361,MAYO,Maigh Eo,MAYO,,CoP,Ld,N,Town_3,,Castlebar,Caisleán an Bharraigh,,,115298,290258,515267,790273,3,,BF,1158796800000,
(53.85500048844355, -9.287932803493295)
```

Present in the Centres of Population file. It seems that the Townsland file alone wouldn`t be that good.

Coding is now also pointing to some kind of "scoring" and prevalence searches, rather than exact matches alone. Things are getting interesting.

## First attempt - exact matches

The first attempt to geocode was to divide the problem and address first the exact English_Name and County, at least. As the result shows, this show a fine initial result using these two files alone and both together.

Also, a exaustion strategy was used for address matching ie:
```St Mary's Road, Inch, Killarney, kerry``` (using the regexp logic, for explanation purposes)

kerry,.+St Mary s Road - no matches  
kerry,.+,Inch, - one exact match in Centres file  
kerry,.+,Inch, - three matches in Towns file

```
// center file
{ 
   "ITM_E":"465695",
   "ITM_N":"601350",
   "GEO":(52.147656567484894, -9.962484123004614) - inch beach, not ok
},
// towns file
{
   "ITM_E":"508064",
   "ITM_N":"582290",
   "GEO":(51.98504529659472, -9.33847681075523) - seems more precise, in Killarney region
},
{
   "ITM_E":"465707",
   "ITM_N":"598795",
   "GEO":(52.12470660935928, -9.961300199190388) - inch beach, not ok
},
{
   "ITM_E":"495864",
   "ITM_N":"590982",
   "GEO":(52.06099881371589, -9.518674184806464) - seems more precise, in Killarney 
}
```

This seems odd... none of the options was safisfactory or clear in the sense that ambiguous results couldn`t be debugged in this manner. Anyway, I decided to folow this strategy, write some code and see what data could tell me.



### Results by count of matches per address


Centres_of_Population_-_OSi_National_Placenames_Gazetteer.csv
```
| Number of matches | Matches count |
|-------------------|---------------|
|  1                |  2386         | 
|  0                |  549          |
|  2                |  11           |

```

Townlands_-_OSi_National_Placenames_Gazetteer.csv
```
| Number of matches | Matches count |
|  0                |  255          |
|  1                |  2194         |
|  2                |  259          |
|  3                |  106          |
|  4                |  57           |
|  5                |  23           |
|  6                |  14           |
|  7                |  14           |
|  8                |  10           |
|  9                |  2            |
|  11               |  5            |
|  12               |  1            |
|  14               |  3            |
|  16               |  1            |
|  18               |  2            |
```

Both files 
```
| Number of matches | Matches count |
|  1                |  1524         |
|  2                |  991          | 
|  3                |  144          | 
|  0                |  123          | 
|  4                |  81           | 
|  5                |  24           | 
|  7                |  20           | 
|  6                |  14           | 
|  8                |  6            | 
|  9                |  6            | 
|  11               |  5            | 
|  19               |  2            | 
|  14               |  2            | 
|  12               |  1            | 
|  10               |  1            | 
|  16               |  1            | 
|  15               |  1            |
```

It has some significant exact match counts, but this seems to be a low quality result. LOTS of ambiguous results, hard to debug address by address

### Inverse exaustion strategy

Address has a priority, from the higher to the lower. I should subset things so from the right to left i might be able to match an address in a better maner. This is the logic induced by the test itself and I actualy have no idea why I didn`t tried this in the first place.

Centres_of_Population_-_OSi_National_Placenames_Gazetteer.csv
```
| Number of matches | Matches count |
|  1                |  2390         |
|  0                |  549          |
|  2                |  7            |
```


Townlands_-_OSi_National_Placenames_Gazetteer.csv
```
| Number of matches | Matches count |
|  1                |  2295         |         
|  0                |  255          | 
|  2                |  239          | 
|  3                |  88           | 
|  5                |  24           | 
|  4                |  22           | 
|  6                |  11           | 
|  7                |  4            | 
|  8                |  4            | 
|  10               |  2            | 
|  11               |  2            |
```

This seems much better! Not only the number of missing addresses didn`t changed (somewhat expected), but the matching distribution is much more concentrated in the lower colision count area, with lower colision counts across the board.

Does it have qualitative improovements?

### Quality sampling
(since I don't have a referential truth, I'll be doing samples for quality testing)

The example used before, ```St Mary's Road, Inch, Killarney, kerry```, now returns a single match: (52.0598838888526, -9.510994337173333) - right in the Killarney town!

In the Centre file, I get the (52.06912685827831, -9.516470173379325) point, not the centroid of the town, but may this be enough for this task?

Does this behaviour repeats?

Townlands_-_OSi_National_Placenames_Gazetteer.csv
```
Kinnoghty, Ardara, donegal - 'ARDARA', 'DONEGAL' - (54.76760667129787, -8.410494207506323) - weird, Kinnoghty and Adara are different towns. I`ll stick with this result

Bride street, Loughrea, galway - 'LOUGHREA', 'GALWAY' - ok (little to the west of the bridge itself)

Rinnamona, Kilnaboy, clare - 'RINNAMONA', 'CLARE' - (52.98570980016141, -9.04662537946135) - seems ok but interesting, "Kilnaboy" seems to be "Killinaboy" misspelled, I`ll consider a lucky guess

Cloghers,, Tralee, kerry - 'TRALEE', 'KERRY' - (52.2679974240826, -9.713377780766468) - seems ok, even being "Cloghers" an actual place
```

Centres_of_Population_-_OSi_National_Placenames_Gazetteer.csv
```
Kinnoghty, Ardara, donegal - 'ARDARA', 'DONEGAL' - (54.767143516617594, -8.409292976990828) - same

Bride street, Loughrea, galway - 'LOUGHREA', 'GALWAY' - (53.19891462999855, -8.566092571000857 - ok, very close to the centroid

Rinnamona, Kilnaboy, clare - missing (oh, this gives me ideas...)

Cloghers,, Tralee, kerry - 'TRALEE', 'KERRY' - (52.271311210322835, -9.699921608767777) - ok, also close to the centroid

```


<hr>
By now I could just stick to the test and geocode things by county in case of colision or missing, but this is fun and i`ll keep exploring data
<hr>

### The missing ones

I decided to tag along with the Centres file. The points provided in he file are not in the actual centroid, but is inside the shape of the town, seems to be enough for this specific task (this is a complete assumption, I know that).

That said, it`s time to focus on the second main group, the non-match group. The last example shown that mispelings may be envolved in the issue, so a direct comparison may not be enough.

It`s time for Levenshtein! (probably needing to calculate Levenshtein distance not to misspell it too)
https://en.wikipedia.org/wiki/Levenshtein_distance

Ill try not to compare strings directly, but instead I`ll do a Levenshtein distance comparison by increasing factors (distance < N_factor then equals).

L_FACTOR = 2
| Number of matches | Matches count |
|  1                |  2557         |
|  0                |  383          |
|  2                |  6            |

L_FACTOR = 3
```
| Number of matches | Matches count |
|  1                |  2625         |
|  0                |  302          |
|  2                |  19           |
```

A factor of 3 when searching for missing addresses seems a sweetspot.
Our missing finaly showed up, in a more precise location, right above Killinaboy in google maps (like most of the others Kilnaboy entries):

```
Rinnamona, Kilnaboy, clare - ('KILNABOY', 'CLARE') - 52.97108098824808, -9.087304097748559 - bullseye
```

I can`t get realy excited by now. This introduces a serious problems: probably all the new collisions in the number of matches 2 may be colisions due to closely writen words, and that revealed to be true. Some cases are:

BALLYNORA - Ballymore  
CARRIGART - Carrigans - Carrickart (both at 2 of distance)  

And, most important of all! The example case of the test, ```Johnstown, Bennekerry, Co Carlow``` is missing!

This needs to be adressed in a different manner. 


### Time to gather more data

Since Centers seemed to be a more precise file and Towns seemed to have more colisions, i`ll try to find matches as the follow list of precedence:

exact match - Centres  
exact match - Towns  
Levenshtein - Centres  
Levenshtein - Towns  

In this specific order, to try better results.

```
| Number of matches | Matches count |
|  1                |  2847         |  
|  2                |  47           |  
|  0                |  21           |  
|  3                |  10           |  
|  5                |  5            |  
|  7                |  4            |  
|  4                |  3            |  
|  11               |  3            |  
|  6                |  2            |  
|  8                |  2            |  
|  10               |  1            |  
|  9                |  1            |
```

This seems to be an imrpovement in acuracy (needs to be better tested!), with the downside of the creation of colision, specialy the higher count ones.

This way I could finaly get a result for the use case of the test! Or did I?

```Johnstown, Bennekerry, Co Carlow``` returns the following match:
```
('BENNEKERRY', 'CARLOW'),
 [{'C': 'CARLOW',
   'E': 'BENNEKERRY',
   'ITM_E': '676256',
   'ITM_N': '675036',
   'GEO': (52.8208923823154, -6.868629103264151)}])
```

This distance is equivalent of 0.00009492 km... but it actualy doesn`t matters. By a mere coincidence, this distance is nigligible only because the centroid of  
303,CARLOW,Ceatharlach,CARLOW,,Td,Bf,N,,10306,JOHNSTOWN,,,,277081,176197,__677015,676236__,,,,,
is close to the one in  
136,CARLOW,Ceatharlach,CARLOW,,Td,Bf,N,,10137,BENNEKERRY,Binn an Choire,,,276322,174997,__676256,675036__,,,Fiontar,,

* I would like to keep this implementation this way. It seems it brings more bennefits rather than disvantages

### Impoving geocoding quality

Levenshtein is proving useful, but it`s also creating some problems.
Tolve some isues, I would like to do some important refactorings:
* Levenshtein should be used to all matches and a distance of 0 must be addressed as an equal exact match
* Levenshtein should order the match colision in ascending order
* Geocoder must detail the precision level, diferentiating Centre, Town and County
