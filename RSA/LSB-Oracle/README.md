# LSB Oracle Attack

* `server.py` : target server
* `solve.py` : solution script using the first method described in the slide
* `solve2.py` : solution script using the second method described in the slide
* `flag` : the flag

You can use the following command to start up the server.

```bash
socat TCP-LISTEN:20000,fork EXEC:./server.py
```

