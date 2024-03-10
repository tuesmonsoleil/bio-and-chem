while (true) {
  const userInput = prompt("請輸入題目和答案 : \n");

  // 使用正則表達式查找 sn、option 和 answer
  const snRegex = /"sn":\s*(\d+)/;
  const optionRegex = /"option":\s*(\[.*?\])/;
  const answerRegex = /"answer":\s*(\[.*?\])/;

  // 獲取問題編號
  const qnStr = userInput.match(snRegex)[1];

  // 獲取選項
  const optionStr = userInput.match(optionRegex)[1];
  const separator = optionStr.includes("},{") ? "},{" : ",\\\\";
  const options = optionStr.slice(1, -1).split(separator).map(option => option.trim());

  // 獲取正確答案索引
  const answerStr = userInput.match(answerRegex)[1];
  const correctAnswerIndices = answerStr.slice(1, -1).split(",").map(index => parseInt(index.trim()));
  const correctAnswers = correctAnswerIndices.map(index => options[index]);

  console.log(`correct_answers for question number ${qnStr} : ${correctAnswers}`);
}