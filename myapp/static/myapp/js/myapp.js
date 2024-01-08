// This is a javascript code for Question answers for sawaljawa page

function showAnswer(questionNumber, selectedOption) {
    // You can replace this with your logic to determine the correct answer
    const correctAnswer = "Option C";
    
    // Display the answer based on the selected option
    const answerElement = document.getElementById(`answer${questionNumber}`);
    answerElement.style.display = 'block';
    answerElement.innerText = selectedOption === correctAnswer
      ? 'Correct! Well done.'
      : 'Incorrect. Please try again.';
  }