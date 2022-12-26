

let userMap = new Map();

userMap.set("client", getUserData);
userMap.set("professional", getProfessionalData);

const signup = document.querySelector("#signup");

signup.addEventListener("submit", function(event) {

    event.preventDefault();

    let isValid = validateData(currentSection);

    if (!isValid) return
    
    const userType = signup.querySelector('input[name="userType"]:checked').value;

    const data = userMap.get(userType)();
    const action = "/users/registrar/"

    for (const [key, value] of data) {
        console.log(`${key}: ${value}\n`);
    }

    sendData( {action, data } )
});

function getUserData() {

    let formData = new FormData()
    
    formData.append('name', signup.querySelector('input[name="userName"]').value);
    formData.append('email', signup.querySelector('input[name="userEmail"]').value);
    formData.append('CPF', signup.querySelector('input[name="userCPF"]').value);
    formData.append('number', signup.querySelector('input[name="userNumber"]').value);
    formData.append('password', signup.querySelector('input[name="userPassword"]').value);

    return formData
}

function getProfessionalData() {

    const formData = getUserData();

    formData.append('professional_type', signup.querySelector('input[name="professionalType"]:checked').value );
    formData.append('professional_code', signup.querySelector('input[name="professionalCode"]').value );

    return formData
}

function sendData( options ) {
    fetch(options.action, {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrfmiddlewaretoken"),
        },
        body: options.data
      })
      .then(data => {
        console.log(data);
      });
}

function getCookie(name) {
    return signup.querySelector(`input[name="${name}"]`).value;
}