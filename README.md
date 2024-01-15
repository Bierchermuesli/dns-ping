# dns-ping
Ping like tool for DNS


requires `python3-dnspython` or from pip `dnspython``


```

## Example 1
- use 0.1s intervall

./dns-ping.py asdf.com -n 0.1 
!!!!!!!!!!!!!!!!!!!^C
--- asdf.com DNS statistics ---
19 successfull 0 failed
rtt min/avg/max 0.0009/0.0020/0.0027s

```

```
## Example 2
 - verbose level 1 
 - asking 1.1.1.1 instead of system resolver
 - default interval 1sec, 5sec timeout

./dns-ping.py asdf.com -v -s 1.1.1.1
asdf.com. 154 IN A 205.196.223.8         dns_seq=55554 time=0.001171s
asdf.com. 153 IN A 205.196.223.8         dns_seq=43123 time=0.003033s
asdf.com. 152 IN A 205.196.223.8         dns_seq=50335 time=0.002679s
^C
--- asdf.com DNS statistics ---
3 successfull 0 failed
rtt min/avg/max 0.0012/0.0023/0.0030s
```

## Example 3
 - verbose level 3 (prints multiple records - if any)
 - query NS type
 - do 10 queries and exit

```
./dns-ping.py asdf.com -c 10 -n 0.1 -vvv -t NS
3 Records dns_seq=35063  time=0.1479s
asdf.com. 3600 IN NS ns3.dreamhost.com.
asdf.com. 3600 IN NS ns2.dreamhost.com.
asdf.com. 3600 IN NS ns1.dreamhost.com.
....

--- asdf.com DNS statistics ---
10 successfull 0 failed
rtt min/avg/max 0.0017/0.0184/0.1479s

```
