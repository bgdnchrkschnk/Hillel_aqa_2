import itertools


browser = ["Chrome", "Firefox", "Safari"]
os = ["Windows", "Linux"]
api_version = ["v1", "v2", "v3"]

# exhausting testing
all_combinations = itertools.product(browser, os, api_version)

# for items in all_combinations:
#     print(items)

# cycle - циклити значення в ітераторі
api_versions = ["v1", "v2", "v3"]
# api_versions_iterator = iter(api_versions)
api_versions_iterator = itertools.cycle(api_versions)
print(next(api_versions_iterator))
print(next(api_versions_iterator))
print(next(api_versions_iterator))
print(next(api_versions_iterator))