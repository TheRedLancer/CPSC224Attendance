# Auto fill Google form for Gonzaga CPSC 224 ACrandal Attendance
# Author: Zach Burnaby
# Date: 2020-10-05
#
# Required file: "id.txt" with Student id number
# Required packages: requests
import requests


def get_id(id_file):
    # Student ID is hidden in a local file
    with open(id_file, "r") as file:
        id = file.read()
    return id


def main():

    # All 4 attributes in the google form
    data = {
        # What is your name?
        "entry.2008377626": "Zach Burnaby",
        # What is your GUID?
        "entry.2133964104": get_id("id.txt"),
        # Temporally, are you filling this out during lecture, or when you're reviewing the slides later? Other option: "At another time"
        "entry.857791487": "During lecture",
        # Are you attending class or engaging with the materials remotely? Other option: "In person"
        "entry.2068559486": "Remote (online) / Later Reviewing of Slides"

    }
    print(data)

    # Base attendance link without class day on end
    attendance_link = "http://bit.ly/CPSC224-F20-AT"

    # Get and write class day from file
    class_day_file = "class_day.txt"
    with open(class_day_file, "r") as file:
        class_day = file.read()
    print("Class Day:", class_day)

    with open(class_day_file, "w") as file:
        file.write(str(int(class_day) + 1))

    # Put together full bit.ly link
    short_link = attendance_link + class_day

    print("Short Link:", short_link)

    # Get the full google forms URL after bit.ly redirection
    with requests.get(short_link) as response:
        html = response.url

    # Clean google forms URL
    form_root = html[0: html.index("?")]
    form_url = form_root[0: -8] + "formResponse"
    print("Google Form Link:", form_url)

    # Send POST request with form data
    try:
        requests.post(form_url, data=data)
        print("Form Submitted.")
    except:
        print("Error Occured!")


if __name__ == "__main__":
    main()
