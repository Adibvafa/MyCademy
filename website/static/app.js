// import { fromEvent, merge } from 'rxjs';
// import { take } from 'rxjs/operators';


let isQuiz = false;

function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/";
    });
}

function generateResponse(prompt) {
    return new Promise((resolve, reject) => {
        fetch('/generate-response', {
            method: 'POST',
            body: JSON.stringify({ text: prompt })
        })
          .then(response => response.json())
          .then(data => {
            // access the properties of the JSON object
            console.log(data.resp);
    
            // resolve the Promise with property1
            resolve(data.resp);
          })
          .catch(error => {
            // reject the Promise with the error message
            reject(error.message);
          });
      });

    // fetch('/generate-response', {
    //     method: 'POST',
    //     body: JSON.stringify({ text: prompt })
    // }).then(response => response.json())
    // .then(data => {
    //   console.log(data.resp);
    //   return data.resp;
    // });
}

function generateSummary() {
    return new Promise((resolve, reject) => {
        fetch('/generate-summary', {
            method: 'POST'
        })
          .then(response => response.json())
          .then(data => {
            // access the properties of the JSON object
            console.log(data.resp);
    
            // resolve the Promise with property1
            resolve(data.resp);
          })
          .catch(error => {
            // reject the Promise with the error message
            reject(error.message);
          });
      });

    // fetch('/generate-response', {
    //     method: 'POST',
    //     body: JSON.stringify({ text: prompt })
    // }).then(response => response.json())
    // .then(data => {
    //   console.log(data.resp);
    //   return data.resp;
    // });
}

function generateQuiz() {
    return new Promise((resolve, reject) => {
        fetch('/generate-quiz', {
            method: 'POST'
        })
          .then(response => response.json())
          .then(data => {
            // access the properties of the JSON object
            // console.log(data.resp);
    
            // resolve the Promise with property1
            resolve(data);
          })
          .catch(error => {
            // reject the Promise with the error message
            reject(error.message);
          });
      });

    // fetch('/generate-response', {
    //     method: 'POST',
    //     body: JSON.stringify({ text: prompt })
    // }).then(response => response.json())
    // .then(data => {
    //   console.log(data.resp);
    //   return data.resp;
    // });
}

const textInput = document.querySelector('#message-input');
const submitButton = document.querySelector('#message-submit');
const genSummaryButton = document.querySelector('#gen-summary');
const genQuizButton = document.querySelector('#gen-quiz');

textInput.addEventListener('keydown', inpHandler);
function inpHandler(e) {
    if (e.key === 'Enter' && isQuiz === false) {
        addUserMessage();
    }
}

// textInput.addEventListener('keydown', inpHandler2);
// function inpHandler2(e) {
//     if (e.key !== 'Enter' && isQuiz === false) {
//         textInput.addEventListener('keydown', inpHandler);
//         submitButton.addEventListener('click', btnHandler);
//         console.log('added');
//     }
// }

submitButton.addEventListener('click', btnHandler);
function btnHandler() {
    if (isQuiz === false) {
        addUserMessage();
    }
}

genSummaryButton.addEventListener('click', function() {
    addSummary();
});

genQuizButton.addEventListener('click', function() {
    isQuiz = true;
    console.log(isQuiz);

    textInput.removeEventListener('keydown', inpHandler);
    submitButton.removeEventListener('click', btnHandler);
    addQuiz();
    isQuiz = false;
    console.log(isQuiz)
    // textInput.addEventListener('keydown', inpHandler);
    // submitButton.addEventListener('click', btnHandler);
});

function addUserMessage() {
    const messagesDisplay = document.querySelector('#messages-display');
    let prompt = textInput.value
    if (prompt !== '') {
        let ul = document.createElement('ul');
        ul.classList.add('messages')
        let new_li = document.createElement('li');
        new_li.classList.add('user-message');
        new_li.innerText = prompt;
        ul.appendChild(new_li)

        let newMessageHolder = document.createElement('div');
        newMessageHolder.classList.add('message-holder');
        newMessageHolder.classList.add('user-colour');
        newMessageHolder.appendChild(ul);
        messagesDisplay.appendChild(newMessageHolder);

        ul = document.createElement('ul');
        ul.classList.add('messages');
        new_li = document.createElement('li');
        new_li.classList.add('computer-message');
        new_li.innerText = "Generating response...";
        ul.appendChild(new_li);

        newMessageHolder = document.createElement('div');
        newMessageHolder.classList.add('message-holder');
        newMessageHolder.classList.add('computer-colour');
        newMessageHolder.appendChild(ul);
        messagesDisplay.appendChild(newMessageHolder);

        generateResponse(prompt).then(resp => {
            console.log(`property1 is: ${resp}`);
            // new_li = document.createElement('li');
            // new_li.classList.add('computer-message');
            // new_li.innerText = resp;
            // ul.appendChild(new_li)

            ul = document.createElement('ul');
            ul.classList.add('messages')
            new_li = document.createElement('li');
            new_li.classList.add('computer-message');
            new_li.innerText = resp;
            ul.appendChild(new_li)

            newMessageHolder = document.createElement('div');
            newMessageHolder.classList.add('message-holder');
            newMessageHolder.classList.add('computer-colour');
            newMessageHolder.appendChild(ul);
            messagesDisplay.appendChild(newMessageHolder);

            messagesDisplay.scrollTop = messagesDisplay.scrollHeight;
        });
    }
    textInput.value = '';
}

function addSummary() {
    const messagesDisplay = document.querySelector('#messages-display');

    let ul = document.createElement('ul');
    ul.classList.add('messages');
    let new_li_2 = document.createElement('li');
    new_li_2.classList.add('computer-message');
    new_li_2.innerText = "Generating summary...";
    ul.appendChild(new_li_2);

    let newMessageHolder = document.createElement('div');
    newMessageHolder.classList.add('message-holder');
    newMessageHolder.classList.add('computer-colour');
    newMessageHolder.appendChild(ul);
    messagesDisplay.appendChild(newMessageHolder);

    messagesDisplay.scrollTop = messagesDisplay.scrollHeight;

    generateSummary().then(resp => {
        console.log(`property1 is: ${resp}`);
        
        ul = document.createElement('ul');
        ul.classList.add('messages')
        new_li_2 = document.createElement('li');
        new_li_2.classList.add('computer-message');
        new_li_2.innerText = "Summary: " + resp;
        ul.appendChild(new_li_2);

        newMessageHolder = document.createElement('div');
        newMessageHolder.classList.add('message-holder');
        newMessageHolder.classList.add('computer-colour');
        newMessageHolder.appendChild(ul);
        messagesDisplay.appendChild(newMessageHolder);


        messagesDisplay.scrollTop = messagesDisplay.scrollHeight;
    });
}

function addQuiz() {
    const messagesDisplay = document.querySelector('#messages-display');
    let ul = document.createElement('ul');
    ul.classList.add('messages');
    let new_li_3 = document.createElement('li');
    new_li_3.classList.add('computer-message');
    new_li_3.innerText = "Generating question...";
    ul.appendChild(new_li_3);

    let newMessageHolder = document.createElement('div');
    newMessageHolder.classList.add('message-holder');
    newMessageHolder.classList.add('computer-colour');
    newMessageHolder.appendChild(ul);
    messagesDisplay.appendChild(newMessageHolder);

    messagesDisplay.scrollTop = messagesDisplay.scrollHeight;
    
    generateQuiz().then(resp => {
        console.log(`property1 is: ${resp.question}`);
        ul = document.createElement('ul');
        ul.classList.add('messages');
        new_li_3 = document.createElement('li');
        new_li_3.classList.add('computer-message');
        new_li_3.innerText = "Question: " + resp["question"] + ` (from paragraph ${resp["reference"]})`;
        ul.appendChild(new_li_3);

        newMessageHolder = document.createElement('div');
        newMessageHolder.classList.add('message-holder');
        newMessageHolder.classList.add('computer-colour');
        newMessageHolder.appendChild(ul);
        messagesDisplay.appendChild(newMessageHolder);

        messagesDisplay.scrollTop = messagesDisplay.scrollHeight;
        
        waitForSubmit().then(userInput => {
            ul = document.createElement('ul');
            ul.classList.add('messages');
            new_li_3 = document.createElement('li');
            new_li_3.classList.add('user-message');
            new_li_3.innerText = userInput;
            ul.appendChild(new_li_3);
            newMessageHolder = document.createElement('div');
            newMessageHolder.classList.add('message-holder');
            newMessageHolder.classList.add('user-colour');
            newMessageHolder.appendChild(ul);
            messagesDisplay.appendChild(newMessageHolder);
            
            ul = document.createElement('ul');
            ul.classList.add('messages');
            new_li_3 = document.createElement('li');
            new_li_3.classList.add('computer-message');
            new_li_3.innerText = "Answer: " + resp["answer"];
            ul.appendChild(new_li_3);
            newMessageHolder = document.createElement('div');
            newMessageHolder.classList.add('message-holder');
            newMessageHolder.classList.add('computer-colour');
            newMessageHolder.appendChild(ul);
            messagesDisplay.appendChild(newMessageHolder);

            messagesDisplay.scrollTop = messagesDisplay.scrollHeight;
        });
    });
    
    
    // for (let i = 1; i <= 3; i++) {
        //     console.log(`Input ${i}:`);
        //     waitForSubmit().then(userInput => {
            //       console.log(`User input ${i}: ${userInput}`);
            //     });
            // }  
}

function handleSubmit() {
    console.log('Waiting for user input...');
    waitForSubmit().then(userInput => {
    console.log(`User input received: ${userInput}`);
    });
}      

// function handleSubmit() {
//     console.log('Waiting for user input...');
  
//     // call waitForSubmit() three times in a for loop
//     for (let i = 1; i <= 3; i++) {
//       console.log(`Input ${i}:`);
//       waitForSubmit().then(userInput => {
//         console.log(`User input ${i}: ${userInput}`);
//       });
//     }
//   }


//   const textbox = document.getElementById('my-textbox');
//   const submitButton = document.getElementById('my-submit-button');
  
function waitForSubmit() {
    return new Promise(resolve => {
        const handleInput = event => {
        // prevent the form from submitting and refreshing the page
        event.preventDefault();

        
        // resolve the Promise with the textbox value
        resolve(textInput.value);
        
        textInput.value = '';
        // remove the event listeners to prevent multiple resolves
        textInput.removeEventListener('keydown', handleInput2);
        submitButton.removeEventListener('click', handleInput);

        textInput.addEventListener('keydown', inpHandler);
        submitButton.addEventListener('click', btnHandler);
        console.log("hello")
    };
  
        // listen for the Enter key press
        textInput.addEventListener('keydown', handleInput2);
        function handleInput2(e) {
            if (e.key === 'Enter') {
                handleInput(e);
            }
        }
  
        // listen for the click of the submit button
        submitButton.addEventListener('click', handleInput);
    });
}
  
//   function handleSubmit() {
//     console.log('Waiting for user input...');
//     waitForSubmit().then(userInput => {
//       console.log(`User input received: ${userInput}`);
//     });
//   }
  
//   submitButton.addEventListener('click', handleSubmit);


// // Create an observable
// const observable = new rxjs.Observable((subscriber) => {
//     // Subscribe to the keydown event
//     const keydownSubscription = fromEvent(textInput, 'keydown').subscribe((event) => {
//       if (event.key === 'Enter' && isQuiz === false) {
//         subscriber.next('keydown');
//       }
//     });
    
//     // Subscribe to the click event
//     const clickSubscription = fromEvent(submitButton, 'click').subscribe(() => {
//       if (isQuiz === false) {
//         subscriber.next('click');
//       }
//     });
    
//     // Return the unsubscribe function
//     return () => {
//       keydownSubscription.unsubscribe();
//       clickSubscription.unsubscribe();
//     };
//   });
  
//   // Subscribe to the observable
//   const subscription = observable.subscribe((value) => {
//     if (value === 'keydown' || value === 'click') {
//       addUserMessage();
//       subscription.unsubscribe(); // Unsubscribe from the observable
//     }
//   });
  