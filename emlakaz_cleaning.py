import json

f = open("data.json")

data = json.load(f)

f.close()

for line in data:
	if line['house_price_azn'] == None:
		data.remove(line)
		continue

	#else:
	if line["date"] != None:
		date_split = line['date'].split(".")
		date_split.reverse()
		line["Date"] = "-".join(date_split)
		del line["date"]

	if line['map_coordinates'] != None:
		clean_coords = line['map_coordinates'].replace("(", "").replace(")", "").split(",")
		line["Lat"] = clean_coords[0]
		line["Lng"] = clean_coords[1]
		del line["map_coordinates"]

	if line.get("house_data_labels") is not None and line.get("house_data") is not None:
		for label, value in zip(line['house_data_labels'], line['house_data']):
			if label == "Əmlakın növü":
				line['Type of property'] = value
			if label == "Sahə":
				line['Area'] = value
			if label == "Otaqların sayı":
				line['Number of rooms'] = value
			if label == "Yerləşdiyi mərtəbə":
				line['Floor number'] = value
			if label == "Mərtəbə sayı":
				line['Number of floors'] = value
			if label == "Təmiri":
				line['State'] = value
			if label == "'Sənədin tipi":
				line['Type of Property Deed'] = value
	del line["house_data_labels"]
	del line["house_data"]

	
	line["location"] = line["title"][1][13:]
	print(line)