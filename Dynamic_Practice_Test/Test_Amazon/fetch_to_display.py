def fetchItemsToDisplay(items, sortParameter, sortOrder, itemPerPage, pageNumber):
	items.sort(key=lambda x: int(x[sortParameter]) if sortParameter > 0 else x[sortParameter], reverse=sortOrder==1)
	return [n for n,_,_ in items[pageNumber*itemPerPage: (1+pageNumber)*itemPerPage]]

print(fetchItemsToDisplay([["p1", "1", "2"], ["p2", "2", "1"]], 0, 0, 1,0))


from typing import Dict, List, Tuple
def fetch_results_to_display(sort_column: int, sort_order: int, results_per_page: int, page_index: int, results: Dict[str, Tuple[int, int]]) -> List[str]:
    ordered = [(name, rel, price) for name, (rel, price) in results.items()]
    ordered.sort(key=lambda x: x[sort_column], reverse=sort_order == 1) # sort by sort_column and reverse order if needed
    start_index = results_per_page * page_index # find the start index of the first result on the target page
    return [name for name, _, _ in ordered[start_index:start_index + results_per_page]] # return only the name of each result on the page
sort_column = int(input())
sort_order = int(input())
results_per_page = int(input())
page_index = int(input())
results_length = int(input())
results = {
    n: (int(r), int(p))
    for _ in range(results_length)
    for n, r, p in [input().split()]
    }
res = fetch_results_to_display(sort_column, sort_order, results_per_page, page_index, results)
print(' '.join(res))
