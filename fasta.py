#单
import requests

def get_fasta_from_uniprot(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to retrieve data"

# 示例使用一个UniProt ID
uniprot_id = 'P12345'  # 你可以将这个ID替换成你需要的ID
fasta_sequence = get_fasta_from_uniprot(uniprot_id)
print(fasta_sequence)


#多
import requests

def get_fasta_from_uniprot(uniprot_id):
    url = f"https://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def download_fasta_sequences(uniprot_ids):
    fasta_sequences = {}
    for uniprot_id in uniprot_ids:
        fasta = get_fasta_from_uniprot(uniprot_id)
        if fasta:
            fasta_sequences[uniprot_id] = fasta
        else:
            print(f"Failed to retrieve data for {uniprot_id}")
    return fasta_sequences

# 示例使用一个列表的UniProt IDs
uniprot_ids = ['P12345', 'Q8N7X0', 'O14920']  # 你可以在这个列表中添加你需要的IDs
fasta_sequences = download_fasta_sequences(uniprot_ids)

# 打印或者处理每个蛋白的序列
for uniprot_id, fasta in fasta_sequences.items():
    print(f"ID: {uniprot_id}\nSequence:\n{fasta}\n")