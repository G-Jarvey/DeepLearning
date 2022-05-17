import json
from tqdm import tqdm
lccc_data_path = './raw_data/duconv_train.txt'
lccc_prepared_data = './data/duconv_data.txt'
write_file = open(lccc_prepared_data, 'a', encoding='utf-8')
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，！＂《》「🔫」—∩😳•﹏•´▽ﾉ【】（）、。：；’‘……￥·"""

dicts = {i: '' for i in punctuation}
punc_table = str.maketrans(dicts)
lis = []
with open(lccc_data_path, encoding='utf-8') as f:
    for line in tqdm(f.readlines()):  # 每一行是一组
        sentences = json.loads(line)
        # print(sentences['conversation'])
        for sentence in sentences['conversation']:
            sentence = sentence.replace(" ", "")
            write_file.write(sentence)
            write_file.write('\n')
        write_file.write('\n')

write_file.close()