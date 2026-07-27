import json

config_file = {"model_name": "resnet50", "epochs": 20, "batch_size": 32, "learning_rate": 0.001}

with open("config_file.jason","w") as json_file:
    json.dump(config_file,json_file,indent=4)

#reading from jason file
if __name__ == "__main__":
    with open("config_file.jason","r") as json_file:
        loaded_jason_file = json.load(json_file)
    print(loaded_jason_file["model_name"])