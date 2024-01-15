# dns-ping
Ping like tool for DNS


```
./dns-bench.py asdf.com -s 1.1.1.1 -n 0.5 -t MX 
asdf.com. 292 IN MX 10 mx10.asdf.com.    dns_seq=35889 time=0.0426s
asdf.com. 292 IN MX 10 mx10.asdf.com.    dns_seq=64551 time=0.03688s
asdf.com. 291 IN MX 10 mx10.asdf.com.    dns_seq=30070 time=0.05855s
asdf.com. 291 IN MX 10 mx10.asdf.com.    dns_seq=57240 time=0.03662s
^C
--- asdf.com DNS statistics ---
4 queries performed for asdf.com
rtt min/avg/max/mdev 0.0366/0.0437/0.0586s
```