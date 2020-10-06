# Auto fill Google form for Gonzaga CPSC 224 ACrandal Attendance
# Author: Zach Burnaby
# Date: 2020-10-05
import requests


def main():

    # All 4 attributes in the google form
    data = {
        # What is your name?
        "entry.2008377626": "Zach Burnaby",
        # What is your GUID?
        "entry.2133964104": "27492315",
        # Temporally, are you filling this out during lecture, or when you're reviewing the slides later?
        "entry.857791487": "During lecture",
        # Are you attending class or engaging with the materials remotely?
        "entry.2068559486": "Remote (online) / Later Reviewing of Slides"
    }

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
        # requests.post(form_url, data=data)
        print("Form Submitted.")
    except:
        print("Error Occured!")


if __name__ == "__main__":
    main()
