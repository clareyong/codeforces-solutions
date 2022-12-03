pages = int(input())
pages_read = list(map(int, input().split()))

days_tracker = []
for i, page_read in enumerate(pages_read):
    pages -= page_read
    days_tracker.append(i)
    print(pages)
    if pages == 0:
        break
print(days_tracker)
