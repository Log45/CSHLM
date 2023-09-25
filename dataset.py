from torch.utils.data import DataLoader, IterableDataset
import os
import json

def totxt():
    text = []
    current = os.getcwd()
    for dir in os.listdir(f"{current}/data/JSON"):
        for file in os.listdir(f"{current}/data/JSON/{dir}"):
            file = f"{current}/data/JSON/{dir}/{file}"
            with open(file, encoding="UTF-8") as f:
                s = f.read().replace('\n', '')
                d = json.loads(s)
                #print(d)
                for x in d:
                    for i in x:
                        if type(x[i]) is dict:
                            if 'text' in x[i].keys():
                                t = x[i]['text']
                                text.append(t)
    print(text)
    messages = ""
    for s in text:
        messages = f"{messages}{s}\n"

    with open("data/messages.txt", encoding="UTF-8") as f:
        f.write(messages)

if __name__ == "__main__":
    totxt()