# Length Extension Attack

* `server.py` : target server
* `solve.py` : solution script
* `flag` : the flag
* `salt` : the salt

You can use the following command to start up the server.

```bash
socat TCP-LISTEN:20000,fork EXEC:./server.py
```

