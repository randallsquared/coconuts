
I'm going to take some notes as I go.

The sample has a zero, while the second example doesn't (lowest is 248).

    $ grep '^0' flight_paths.txt
    $ grep '^.. ' flight_paths.txt
    $ grep '^... ' flight_paths.txt
    496 720 896
    787 1140 1765
    654 1029 1500
    422 841 1676
    248 761 2052
    458 697 956
    909 1450 1623
    901 967 330

I was about to check for duplicate starts, but it doesn't matter since they could have differing end points; no reason to try to simplify, that way.  

Additionally: 
* there's no guarantee that multiple jet streams don't end on the end, so I have to check every possible.  
* there's no guarantee that the lowest cost path will have an end at the End (the lowest cost set of streams might, for example, end five before the end.  This means I can't work backward from the last stream, since even though I'll probably end up using that stream, I might not).

The only shortcutting I could do is to stop when the current cost is higher than the previous low record.

My approach will be this.  

 save the default cost
 pull all the paths into something rough to begin with where I can sort by the starts 
  list of tuples, I guess
 find the largest end


 lowest cost path list from this start needs default, start, end, path list, all paths
  if the start is the end, or if all paths is empty:
   return path list
  
  current = []
  for each entry in all paths
   l = lowest(default, entry[0], end, path list, all paths[entry position])
   if costof(default, start, end, l) < costof(default, start, end, current)
    current = l
  return path list + current


costof(default, start, end, path list)
 returns int
  
  

Later:

Well, that didn't work well, since python's recursion limit is 1000.  :)

With some creative caching of the totals to trim some trees, I might be able to get this to work anyway, but it wouldn't scale to a million in any case, so I need to do this with iteration.

Using itertools, I've written a version that I believe will get the right answer, eventually (and does on the sample data).  Unfortunately, I'm not yet sure how long it takes on the 5000 line flight data, since it's STILL RUNNING.   I'm pretty sure that a good solution shouldn't continue running for minutes, so I need to look into doing it more efficiently.

 

