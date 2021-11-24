import dataframe
import pandas as pd


path = "data/"



original_data = pd.read_csv('/media/ocean/大白菜U盘/GAN_study/Length_512_lab_test_37_v2/train_sequences.csv', sep="\t")
columns = ["Label", "EC number", "cluster", "sequence"]
group_by_col = "cluster"

map_data = ["EC number", "sequence"]

id_to_character, character_to_id = dataframe.get_id_character_mapping(original_data, map_data)


dataframe.save_as_tfrecords_multithreaded(path, original_data, columns)