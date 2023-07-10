#!/usr/bin/env python3

# Script to convert Pocket articles into an org file
#
# Output file obtained from https://getpocket.com/export
#
from bs4 import BeautifulSoup
from datetime import datetime

input_file = "ril_export.html"
output_file = "bookmarks.org"

def timestamp_to_date(ts):
    return datetime.fromtimestamp(ts).strftime("%Y/%m/%d")

def main():
    print("Reading %s..." % input_file)
    soup = BeautifulSoup(open(input_file, "r").read(), "html.parser")
    entries = soup.find_all("li")
    print("Found %s entries " % len(entries))
    with open(output_file, "w") as out:
        for entry in entries:
            link = entry.find("a")
            tags = link["tags"]
            org_tags = ":" + ":".join(tags.split(",")) + ":" if tags else ""
            date = timestamp_to_date(int(link["time_added"]))
            out.write("* " + entry.text + " " + org_tags + "\n" + link["href"] + "\n" + date + "\n")
    print("Created %s" % output_file)

if __name__ == "__main__":
    main()
