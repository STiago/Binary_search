Binary_search Copyright (C) 2013 María Victoria Santiago Alcalá. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see.

# Binary_search

[Binary search](https://stiago.github.io/binary_search) is a search algorithm that finds the position of a target value within a sorted array.Binary search compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful or the remaining half is empty.

Binary search runs in at worst logarithmic time, making O(log n) comparisons, where n is the number of elements in the array, the O is Big O notation, and log is the logarithm. 

More information about Binary search algorithm [here](https://en.wikipedia.org/wiki/Binary_search_algorithm).

How to run the program: ./binary_search.py

    ```env/bin/python binary_search.py```

How to run the tests: ./test.py

   ```env/bin/python test.py```


Before running this program and its tests:

  - Execute the following commands: virtualenv env; env/bin/pip install -r requirements.txt

![Binary search](https://github.com/STiago/Pictures/blob/master/bs.png)

####

_Code_ licensed by **GNU GENERAL PUBLIC LICENSE Version 3**.

_Text_ licensed by **Creative Commons Attribution-ShareAlike 4.0 International**.

<p align="center">
<a href="http://www.gnu.org/licenses/gpl-3.0.html">
<img alt="GPL-3.0" src="https://dl.dropboxusercontent.com/s/t0ylvis7f1stcu7/GPL-3.0.png">
</a>
<a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">
<img alt="CC-BY-SA-4.0" src="https://dl.dropboxusercontent.com/s/sb421l5usayaigo/CC-BY-SA-4.0.png">
</a>
</p>
