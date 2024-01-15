#!/usr/bin/python
# Stefan Grosser 2024

import argparse
from dns.resolver import Resolver
import time


def perform_dns_query(resolver, domain, type="A"):
    try:
        start_time = time.time()
        r = resolver.resolve(domain, type)
        end_time = time.time()
        return end_time - start_time, r
    except Exception as e:
        return None, e


def main():
    parser = argparse.ArgumentParser(description="DNS Query Ping Like Tool")
    parser.add_argument("-n", "--interval", type=float, default=1.0, help="Interval between queries in seconds")
    parser.add_argument("-t", "--type", type=str, default="A", help="Type of Query A, MX, AAAA... ", choices=["A", "AAAA", "MX", "TXT", "SOA"])
    parser.add_argument("-s", "--server", type=str, default=None, help="Server to use, default System DNS")
    parser.add_argument("-v", "--verbose", type=int, default=0, help="make it verbose")
    parser.add_argument("-l", "--lifetime", type=int, default=5, help="DNS LifeTime(out)")
    parser.add_argument("domain", type=str, help="The domain to query", default="example.com")
    args = parser.parse_args()

    total_time = 0
    query_count = 0
    min_time = float("inf")
    max_time = float("-inf")
    resolver = Resolver()
    resolver.timeout = args.lifetime
    resolver.lifetime = args.lifetime
    if args.server:
        resolver.nameservers = [args.server]

    try:
        while True:
            query_time, r = perform_dns_query(resolver, args.domain, args.type)

            if query_time is not None:
                query_count += 1
                total_time += query_time
                min_time = min(min_time, query_time)
                max_time = max(max_time, query_time)
                average_time = total_time / query_count
                responses = len(r.response.answer[0].items)

                if responses == 1:
                    print("{} dns_seq={} time={:.4f}s".format(str(r.response.answer[0]), r.response.id, query_time))
                elif (responses) > 1:
                    print("{} dns_seq={} time={:.4f}s".format(responses, r.response.id, query_time))
                    if args.verbose:
                        print(r.response.answer[0])
            else:
                print(r)

            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\n--- {} DNS statistics ---".format(args.domain))
        if query_count > 0:
            print("{} queries performed for {}".format(query_count, args.domain))
            print("rtt min/avg/max {:.4f}/{:.4f}/{:.4f}s".format(min_time, total_time / query_count, max_time))
        else:
            print("No successful queries were performed.")


if __name__ == "__main__":
    main()
