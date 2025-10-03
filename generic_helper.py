import re
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/",session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    return ""

def  get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])

if __name__ == "__main__":
    # print(get_str_from_food_dict({"samosa":2,"pizzas":1}))
    print(extract_session_id("projects/hesi-chatbot-for-food-del-uckq/agent/sessions/872bbc15-7768-872c-aaef-c2f52c9097fa/contexts/ongoing-order"))