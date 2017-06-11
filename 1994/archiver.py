from collections import Counter
import yaml

def append_in_counter(counter, new_el):
    for ind, el in enumerate(counter):
        if el[1] > new_el[1]:
            counter = counter[:ind] + [new_el] + counter[ind:]
            return counter
    return counter + [new_el]


def huffman_coding(letters_items):
    """
    :param letters_items: 
    :return: tree_of_codding = {
                                'edges': edges, dict[parent + code] = child
                                'root': root, str
                                }
    """
    if len(letters_items) < 2:
        return {letters_items[0]: '0'}

    letters_items.sort(key=lambda x: x[1])

    letters = [i[0] for i in letters_items]
    letters_codding ={}
    edges = []
    edges_dict = {}

    while len(letters_items) > 1:
        first = letters_items.pop(0)
        second = letters_items.pop(0)
        parent = (first[0]+second[0], first[1]+second[1])
        letters_items = append_in_counter(letters_items, parent)
        edges.append((parent[0], first[0], '0'))
        edges.append((parent[0], second[0], '1'))
        edges_dict[(parent[0], '0')] = first[0]
        edges_dict[(parent[0], '1')] = second[0]

    root = letters_items[0][0]
    prefixes = {letters_items[0][0]: ''}

    for parent, child, code in edges[::-1]:
        if child in letters:
            letters_codding[child] = prefixes[parent] + code
        else:
            prefixes[child] = prefixes[parent] + code

    json_tree = {"root": root, "edges": edges_dict}
    with open('tree_of_codes.txt', 'w') as e:
        yaml.dump(json_tree, e)

    return letters_codding


def encode_file():
    texts = []
    nums = []
    with open('input.txt', 'r') as f:
        for line in f:
            num, text = line.split(' ', 1)
            texts.append(text.split('\n')[0])
            nums.append(num)

    letters_items = list(Counter(''.join(texts)).items())
    letters_coding = huffman_coding(letters_items)

    with open('output.txt', 'a') as g:
        for text,num in zip(texts, nums):
            codding_text = ''.join([letters_coding[i] for i in text])
            g.write(num + ' ' + codding_text + '\n')

def main():
    num = input()

    with open('output.txt', 'r') as g:
        for line in g:
            n, code = line[:-len('\n')].split(' ', 1)
            if n == num:
                break

    with open('tree_of_codes.txt', 'r') as f:
        tree_of_codes = yaml.load(f)

    edges = tree_of_codes["edges"]
    root = tree_of_codes["root"]
    # import ipdb;ipdb.set_trace()
    vertex = root
    decode_text = ""
    for symbol in code:
        vertex = edges[(vertex, symbol)]
        if len(vertex) == 1:
            decode_text += vertex
            vertex = root
        # else:

    print(decode_text)


def test_huffman_coding():
    wiki_dict = [('а', 15), ('б', 7), ('в', 6), ('г', 6), ('д', 5)]
    res = huffman_coding(wiki_dict)
    print(res)

# encode_file()
main()