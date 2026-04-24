'''
TASK:
Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. Simon is no exclusion to this
rule. His favorite units in the game are all types of dragons – black, red, gold, azure, etc. He likes them so much that
he gives them names and keeps logs of their stats: damage, health, and armor. The process of aggregating all the data is
quite tedious, so he would like to have a program doing it. Since he is no programmer, it's your task to help him.
You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats
(damage, health, and armor). Type is preserved as in the order of input, but dragons are sorted alphabetically by their
name. For each type, you should also print the average damage, health, and armor of the dragons. For each dragon, print
his own stats.
There may be missing stats in the input, though. If a stat is missing you should assign it default values. Default values
 are as follows: health 250, damage 45, and armor 10. Missing stat will be marked as "null".
The input is in the following format "{type} {name} {damage} {health} {armor}".
The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. Any of the integers may
be assigned a "null" value. See the examples below for a better understanding of your task.
If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are considered
equal if they match by both name and type.
'''