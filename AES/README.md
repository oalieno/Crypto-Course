# AES

You can look at the [course material](/AES/AES.pdf) first before diving into the challenges.

## Challenges

There are four practice challenges in this section.

1. [ECB Mode / Cut & Paste](/AES/Cut-Paste)
2. [ECB Mode / Prepend Oracle Attack](/AES/Prepend-Oracle)
3. [CBC Mode / Padding Oracle Attack](/AES/Padding-Oracle)
4. [GCM Mode / Forbidden Attack](/AES/Forbidden)

Each challenge contains a target server `server.py` and a solution script `solve.py`.
You can use the following command to start up the server.

```bash
socat TCP-LISTEN:20000,fork EXEC:./server.py
```

Try to do it yourself before seeing the solution.

