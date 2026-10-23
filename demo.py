"""Explicit offline demonstration; run from this repository root."""
import json

places = [{'name': 'Demo Hills', 'budget': 3000, 'days': 2}, {'name': 'Demo Coast', 'budget': 7000, 'days': 4}]
request = {'budget': 4000, 'days': 3}
matches = [place for place in places if place['budget'] <= request['budget'] and place['days'] <= request['days']]
assert len(matches) == 1
result = {'mode': 'synthetic travel suggestions; no live routes or prices', 'request': request, 'matches': matches}

print(json.dumps(result, indent=2, sort_keys=True))
