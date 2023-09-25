from torch.utils.data import DataLoader, IterableDataset
import os
import bisect
import json

class JsonDataset(IterableDataset):
    def __init__(self, files):
        self.files = files

    def __iter__(self):
        for json_file in self.files:
            with open(json_file) as f:
                for sample_line in f:
                    sample = json.loads(sample_line)
                    print(sample['text'])
                    yield sample['text']

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

    #dataset = JsonDataset(data)
    #dataloader = DataLoader(dataset, batch_size=32)
    #print(dataset, "\n", dataloader)

main()