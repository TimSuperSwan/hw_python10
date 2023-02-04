def import_words(words):
    with open('calculation.txt', 'a') as file:
        file.write(f'{words} ')
    file.close
# abc = ['id: ','first name: ','second name: ','phone number: ','comments: ']

def import_data(abc):
    for i in range(len(abc)):
        import_words(f'{abc[i]}')
    with open('calculation.txt', 'a') as file:
            file.write('\n')
    file.close