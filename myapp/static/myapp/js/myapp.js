// This is a javascript code for Question answers for sawaljawa page

// function showAnswer(questionNumber, selectedOption) {
//     // You can replace this with your logic to determine the correct answer
//     const correctAnswer = "Option C";
    
//     // Display the answer based on the selected option
//     const answerElement = document.getElementById(`answer${questionNumber}`);
//     answerElement.style.display = 'block';
//     answerElement.innerText = selectedOption === correctAnswer
//       ? 'Correct! Well done.'
//       : 'Incorrect. Please try again.';
//   }

function optASelected(anchor, correctAnswer,description) {
  let anchorValue = anchor.innerHTML;
  let isCorrect = anchorValue == correctAnswer;

  anchor.classList.toggle('correct-answer', isCorrect);
  anchor.classList.toggle('wrong-answer', !isCorrect);

  anchor.closest('div').querySelector('.AnswerDescription').innerHTML ="<span style='color:green;  font-weight:bold;'> Explaination: </span>" + correctAnswer + " is the Correct Answer !! <br> <br>" + description;
  }  
//  ---------------------------------------------------------
function optBSelected(anchor, correctAnswer,description) {
  let anchorValue = anchor.innerHTML;
  let isCorrect = anchorValue == correctAnswer;

  anchor.classList.toggle('correct-answer', isCorrect);
  anchor.classList.toggle('wrong-answer', !isCorrect);

  anchor.closest('div').querySelector('.AnswerDescription').innerHTML = "<span style='color:green;  font-weight:bold;'> Explaination: </span>" + correctAnswer + " is the Correct Answer !! <br> <br>" + description;
  }  

function optCSelected(anchor, correctAnswer,description) {
  let anchorValue = anchor.innerHTML;
  let isCorrect = anchorValue == correctAnswer;

  anchor.classList.toggle('correct-answer', isCorrect);
  anchor.classList.toggle('wrong-answer', !isCorrect);

  anchor.closest('div').querySelector('.AnswerDescription').innerHTML = "<span style='color:green;  font-weight:bold;'> Explaination: </span>" + correctAnswer + " is the Correct Answer !! <br> <br>" + description;
  }  

function optDSelected(anchor, correctAnswer,description) {
  let anchorValue = anchor.innerHTML;
  let isCorrect = anchorValue == correctAnswer;

  anchor.classList.toggle('correct-answer', isCorrect);
  anchor.classList.toggle('wrong-answer', !isCorrect);
  
  anchor.closest('div').querySelector('.AnswerDescription').innerHTML = "<span style='color:green;  font-weight:bold;'> Explaination: </span>" + correctAnswer + " is the Correct Answer !! <br> <br>" + description;
  }       