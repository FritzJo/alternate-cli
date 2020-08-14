# Alternate-cli
A small cli for the german online shop Alternate.de

## Features
* list current deals
* search by product id

## Examples
### Deals
```bash
> python alternate.py deals

788618: DeLonghi ECAM 22.110.SB, Vollautomat silber - 299.0€
1350522: DeLonghi Dedica Style EC 685.R, Espressomaschine rot - 134.9€
1350523: DeLonghi Dedica Style EC 685.M, Espressomaschine silber - 134.9€
1415541: Tefal Pro Express Care GV 9070, Dampfbügelstation weiß/türkis - 159.9€
1534690: Transcend 430S 512 GB, SSD SATA 6 GB/s, M.2 2242 - 76.9€
1588163: AKRacing Core EX-Wide SE, Gaming-Stuhl schwarz/carbon - 299.0€
1591313: Jack Wolfskin MOAB JAM 24, Rucksack blau, 24 Liter - 49.9€
1591856: WD Black P50 Game Drive 2 TB, Externe SSD schwarz, USB-C 3.2 (10 Gbit/s) - 389.0€
1592404: Corsair Harpoon RGB Wireless, Gaming-Maus schwarz - 29.99€
1603501: Hisense RS741N4AC2, Side-by-Side edelstahl - 549.0€
1620452: BIG Bobby-Car-Classic Peppa Pig , Rutscher pink - 32.99€
```

#### Search
```bash
> python alternate.py search cpu

1647381: AMD Ryzen™ 9 3900XT, Prozessor boxed - 499.0€
1647382: AMD Ryzen™ 7 3800XT, Prozessor boxed - 389.0€
1647380: AMD Ryzen™ 5 3600XT, Prozessor boxed - 244.9€
1553392: AMD Ryzen™ 5 3600, Prozessor boxed - 185.9€
1553396: AMD Ryzen™ 7 3700X, Prozessor boxed - 289.0€
1553398: AMD Ryzen™ 9 3900X, Prozessor boxed - 429.0€
1553391: AMD Ryzen™ 3 3200G, Prozessor boxed - 99.9€

```
