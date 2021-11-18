import csv
import re

phone_pattern = r"(\+7|8)?\s?[\(]?(\d{3})[\)]?[-\s]?(\d{3})[-\s]?(\d{2})[-]?" \
                r"(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
phone_sub = r"+7(\2)\3-\4-\5 \6\7"


def parse_phonebook(contacts_list):
    contacts_list_temp = list()
    for i in contacts_list:
        name = ' '.join(i[:3]).split(' ')
        name_info = [name[0], name[1], name[2], i[3], i[4]]
        phone_number = [re.sub(phone_pattern, phone_sub, i[5]), i[6]]
        result = name_info + phone_number
        contacts_list_temp.append(result)
    return delete_duplicates(contacts_list_temp)


def delete_duplicates(contacts):
    duplicates_to_delete = []
    for i in range(len(contacts)-1):
        for j in range(i+1, len(contacts)):
            if contacts[i][:2] == contacts[j][:2]:
                contacts[j][2] = contacts[i][2] or contacts[j][2]
                contacts[j][3] = contacts[i][3] or contacts[j][3]
                contacts[j][4] = contacts[i][4] or contacts[j][4]
                contacts[j][5] = contacts[i][5] or contacts[j][5]
                contacts[j][6] = contacts[i][6] or contacts[j][6]
                duplicates_to_delete.append(contacts[i])
    for i in duplicates_to_delete:
        contacts.remove(i)
    return contacts


with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


with open("phonebook.csv", "w", newline='', encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(parse_phonebook(contacts_list))
