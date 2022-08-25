import os


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever


r_path = '/persist_datasets/custom_datasets/img/val/'

count = 0
selected_files = []
for root, dirnames, fnames in os.walk(r_path):
    # for dirname in dirnames:
    #     print(dirname)
    #     print(os.path.join(root, dirname))

    # print("These are the filenames:")
    if 'bdd100k' in root or 'mapillaryvistas' in root:
        continue

    for fname in fnames:
        if '.png' in fname:
            count = count + 1
            abs_path = os.path.join(root, fname)
            print(remove_prefix(abs_path, r_path)[:-4])
            selected_files.append(remove_prefix(abs_path, r_path)[:-4])
            # print((abs_path)[:-4])
            # selected_files.append(abs_path[:-4])

            # if count >= 1000:
            #     break

print(count)

with open(r_path + "/small_val_w.txt", 'w') as f:
    for i in selected_files:
        f.write(i + '\n')
