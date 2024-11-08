all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]
def filter_colors(color):
    return color["sexy"]

def generate_li(color):
    return f"<li>{color['label']}</li>"

sexy_colors=list(filter(filter_colors,all_colors))
html=list(map(generate_li,sexy_colors))
print(html)

# Your code here
# def filter_colors(color):
#     return color["sexy"] == True

# filtered_colors=list(filter(filter_colors,all_colors))

# def color_only(color):
#     return color["label"]

# sexy_colors=list(map(color_only,filtered_colors))

# def generate_li(color):
#     return f"<li>{color}</li>"

# html_list = list(map(generate_li,sexy_colors))

# print(html_list)
