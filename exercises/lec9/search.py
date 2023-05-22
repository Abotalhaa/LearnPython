"""
Accept user input and search in json file loaded from same dir that convert the following :
# ask user to input search keyword:
# Load sample.json
# handle error read permission.
# collect result of search key nr of appearance
# save result into result.txt
# Keep searching til user enter "#"
# print each result and at the end print all result summary.
"""
import json


def save_results(results):
    try:
        with open('results.txt', 'w') as file:
            file.write(results)
            print("file saved successfully!")
    except IOError as error:
        print(f"Error during saving! {error}")


#
# def load_summary():
#     file = None
#     try:
#         file = open('sum.json', 'r')
#         summary = file.read()
#         return summary
#     except Exception as ex:
#         print(f"Something went wrong: {ex}")
#     finally:
#         if file is not None:
#             file.close()

def load_summary():
    try:
        with open("summary.json", "r") as file:
            return json.load(file)
    except Exception as ex:
        print(f"Something went wrong: {ex}")


summary = load_summary()

results = {}


# Search for the keyword in the JSON file
def search_keyword(keyword):
    count = 0
    for value in summary.values():
        for lines in value:
            if keyword == lines:
                count += 1
    print(f"{keyword} : {count}")
    results[keyword] = count


# Ask the user to input the search keyword
while True:
    keyword = input("Enter search keyword:\n")
    if keyword == "done":
        break
    search_keyword(keyword)

# Save the result into result.txt
print(results)
