import json
from collections import defaultdict

DATAPOINTS = ["delivery_currency", "delivery_amount", "delivery_rounding",
              "return_currency", "return_amount", "return_rounding"]


def read_json():
    """The function is used to read the isda data provided as part of the test

    Returns:
        list: list of dictionary values which contains the text and the datapoints as keys.
    """
    
    with open("isda_data.json","r" ) as f_p:
        list_isda_data = json.load(f_p)

    return list_isda_data



def fetch_json(chunk, type_):
    words = chunk.split()
    json = {}
    for i, word in enumerate(words): 
        if word.lower() == "provided":
            break
        if (len(word) == 3) and (word.upper() == word): 
            json["%s_currency" % type_] = word 
        elif word.replace(",", "").isdigit(): 
            json["%s_amount" % type_] = word 
        elif word == "rounded": 
            if words[i+1] == "up": 
                rounding = "up" 
            elif words[i+1] == "down": 
                rounding = "down" 
            else: 
                rounding = "nearest" 
            json["%s_rounding" % type_] = rounding
    return json



def extracter(text): 
    json = {}
    for chunk in text:
        if "Delivery" in chunk:
            json.update(fetch_json(chunk, "delivery"))
        elif "Return" in chunk:
            json.update(fetch_json(chunk, "return"))
            
    keys = ["amount", "currency", "rounding"]
    types = ["delivery", "return"]
    
    for key in keys:
        data_point1 = "%s_%s" % (types[0], key)
        data_point2 = "%s_%s" % (types[1], key)
        if data_point1 not in json:
            json[data_point1] = json.get(data_point2)
        elif data_point2 not in json:
            json[data_point2] = json.get(data_point1)
    return json



def extract(input_data):
    """The function is used to build the extraction logic for ISDA datapoint
    extraction from the list of text inputs. Write your code logic in this function.

    Args:
        input_data (list): The input is a list of text or string from which the datapoints need to be extracted

    Returns:
        list: the function returns a list of dictionary values which contains the predictions for the input
              text. Note: The predictions should not be in a misplaced order.
              Example Output:
              [
                  {
                        "delivery_currency": "USD",
                        "delivery_amount": "10,000",
                        "delivery_rounding": "nearest",
                        "return_currency": "USD",
                        "return_amount": "10,000",
                        "return_rounding": "nearest"
                  },
                  ...
              ]
    """

    predicted_output = []
    for json in input_data:
        predicted_output.append(extracter(json.split(";")[0].split("and")))
    return predicted_output

    return predicted_output


def evaluate(input_data, predicted_output):
    """The function computes the accuracy for each of the datapoints
    that are part of the information extraction problem.

    Args:
        input_data (list): The input is a list of dictionary values from the isda json file
        predicted_output (list): This is a list which the information extraction algorithm should extract from the text

    Returns:
        dict: The function returns a dictionary which contains the number of exact between the input and the output
    """

    result = defaultdict(lambda: 0)
    for i, input_instance in enumerate(input_data):
        for key in DATAPOINTS:
            if input_instance[key] == predicted_output[i][key]:
                result[key] += 1

    # compute the accuracy for each datapoint
    for key in DATAPOINTS:
        print(key, 1.0 * result[key] / len(input_data))

    return result


if __name__ == "__main__":
    json_data = read_json()
    text_data = [data['text'] for data in json_data]

    # write your extract logic in the extract function
    predicted_output = extract(text_data)
    result = evaluate(json_data, predicted_output)
