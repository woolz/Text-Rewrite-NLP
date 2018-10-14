from text_rewrite import TextRewrite


sentences = ['My machine is so bad and dramatic', 'I have one dog and two cars', 'This season is so weak.']
for sentence in sentences:
    new_sentence = TextRewrite(sentence).work() 
    print(sentence + " -> " + new_sentence)
