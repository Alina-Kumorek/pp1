# The website http://api.nbp.pl contains data on exchange rates published by the National Bank of Poland.
# The service provides data in json or xml formats.
# Display the last ten Euro exchange rates in json format in the browser window. Save the data to the euro.json file.
# Then write a program that displays the data from the euro.json file in the following format:

#     Date            Buying Rate     Selling Rate
#     ============================================
#     2019-10-25      3.8150          3.9820
#     ...             ...             ...

import json

with open("euro.json") as f:
    data = json.load(f)

rates = data["rates"]

heading = "Date\t\t\tBuying Rate\tSelling Rate\n===================================================="
print(heading)

for i in rates:
    print(i["effectiveDate"], i["bid"], i["ask"], sep="\t\t")