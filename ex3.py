# 1.编写程序，实现输入下面的结果：（宽度为30）
print('{0:*^30}'.format('学生管理系统'))

print('{:*<30}'.format('学生管理系统'))

print('{:*>30}'.format('学生管理系统'))

print('{:@>30}'.format('学生管理系统'))


# 2.用户输入一个句子（只包含字母和空格），将句子中的单词反转，并输出
# 例如：输入：I like world
# 输出：world like I
# def reverse_words(sentence):
#     words = sentence.split()
#     reversed_words = reversed(words)
#     reversed_sentence = ' '.join(reversed_words)
#     return reversed_sentence
#
# sentence = input('请输入一个句子：')
#
# reversed_sentence = reverse_words(sentence)
# print('输出：', reversed_sentence)