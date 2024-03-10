while True:
   user_input = input("請輸入題目和答案 : \n") # search for question number 
   qn_start = user_input.find('sn') + 7
   qn_end = user_input.find('sn') + 8
   qn_str = user_input[qn_start:qn_end]
   # print(f'qn_str: {qn_str}')
   
   # search for answer
   answer_start = user_input.find('answer') + 9
   answer_end = user_input.find(',"sn":') - 13
   answer_str = user_input[answer_start:answer_end]
   # print(f'answer: {answer_str}')
   
   # search for option
   option_start = user_input.find('"option":[') + 14
   option_end = user_input.find(']', option_start) - 1
   option_str = user_input[option_start:option_end]
   
   # split each option
   separator = '},{' if '},{' in option_str else ',\\'
   options = option_str.split(separator)
   options = [option.strip() for option in options]
   
   # output each option and its index
   # for i, option in enumerate(options):
   #     print(f'{i} : {option}')
   
   # output the index of the correct option
   correct_answer_indices = [int(index.strip()) for index in answer_str.strip('[]').split(',')]
   correct_answers = [options[index] for index in correct_answer_indices]
   print(f'correct_answers for question number {qn_str} : {correct_answers}')