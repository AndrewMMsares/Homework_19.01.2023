# 1.
# with open('file.txt', 'r', encoding='utf-8') as input_file:
#     content = input_file.read()
#     words = content.split()
#
#     filtered_words = [word for word in words if len(word) >= 7]
#
# with open('file.txt', 'w', encoding='utf-8') as output_file:
#     output_file.write(' '.join(filtered_words))
#
# print(filtered_words)

# 2
# with open('file.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     words = content.split()
#     word_count = len(words)
#
# print(f'The number of words in the file: {word_count}')

# 3
# def check_and_replace(file_path, forbidden_word):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         words = content.split()
#
#     count = 0
#     for i in range(len(words)):
#         if words[i].lower() == forbidden_word.lower():
#             words[i] = '*' * len(forbidden_word)
#             count += 1
#
#     result_text = ' '.join(words)
#
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write(result_text)
#
#     return count
#
# file_path = 'file.txt'
# forbidden_word = 'die:'
#
# replacements = check_and_replace(file_path, forbidden_word)
#
# print(f"Number: {replacements} word replacement '{forbidden_word}'.")