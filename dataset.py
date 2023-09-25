from torch.utils.data import DataLoader, IterableDataset
import os
import json

def main():
    data = []
    text = []
    current = os.getcwd()
    for dir in os.listdir(f"{current}/data"):
        for file in os.listdir(f"{current}/data/{dir}"):
            file = f"{current}/data/{dir}/{file}"
            #print(f"{current}/data/{dir}/{file}")
            data.append(file)
            with open(file, encoding="UTF-8") as f:
                s = f.read().replace('\n', '')
                d = json.loads(s)
                #print(d)
                for x in d:
                    for i in x:
                        #print((x))
                        if type(x[i]) is dict:
                            if 'text' in x[i].keys():
                                t = x[i]['text']
                                text.append(t)
                        #print((x[i]))
    print(text)

main()