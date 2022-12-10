# Create a dictionary describing a mobile phone. Use at least 6 key-value pairs of data. Use different value types.
# Then, using 'for' loop, display the contents of the dictionary. To read a key and value, use the items() method.

smartphone = {
    "marka": "Xiaomi",
    "model": "Mi 9 SE",
    "system": "Android",
    "przekatna": 5.0,
    "RAM": 6,
    "pamięć": 128
    }

for k, v in smartphone.items():
    print(f"{k}: {v}")