let client = [
    {
        current: 'client',
        next: 'info'
    },
];
let professional = [
    {
        current: 'professional',
        next: 'info'
    },
    {
        current: 'info',
        next: 'professionalType'
    },

];

let admin = [
    {
        current: 'admin',
        next: 'info'
    },
];

const keyframeShake = [
    { transform: 'skewY(-4deg)'},
    { transform: 'skewY(4deg)'},
    { transform: 'skewY(-4deg)'},
    { transform: 'skewY(4deg)'},
    { transform: 'skewY(0)'  },
    { transform: 'skewY(0)'  }
];
const shakeTiming = {
    duration: 350,
    iterations: 1,
}


let sectionFlow = [];
let currentSection = document.getElementById('userType');


const clientMap = new Map(client.map(i => [i.current, i.next]));
const professionalMap = new Map(professional.map(i => [i.current, i.next]));
const adminMap = new Map(admin.map(i => [i.current, i.next]));

const flowMap = new Map([['professional', professionalMap], ['client', clientMap], ['admin', adminMap]]);

const flowChoice = document.querySelectorAll('.options .choice');

let flow;

flowChoice.forEach((element) => {
    element.addEventListener('click', (e) => {
        let id;

        let input = element.querySelector('.choice__input');

        if (element.classList.contains('flow-choice')){
            flow = input.value;
            step = input.value;
        } else {
            step = input.getAttribute('data-next-step-key')
        }
        id = flowMap.get(flow).get(step);
        nextSection(id);
    })
});


const [back, forward] = document.querySelectorAll('.actions > button');

back.addEventListener('click', () => {
    if (sectionFlow.length < 1) return
    let lastSectionVisited = sectionFlow.pop();
    nextSection(lastSectionVisited, true);
});


forward.addEventListener('click', () => {

    let isValid = validateData(currentSection);

    if (!isValid) {
        forward.animate(keyframeShake,shakeTiming)
        return 
    };
    

    let nextSectionID = flowMap.get(flow).get(currentSection.id);

    if (nextSectionID) {
        nextSection(nextSectionID);
    }

    
});


main()

/* functions */

function main() {
    changeState(currentSection, {
        old: "section--inactive",
        new: "section--active"
    })
    checkActionsVisibility(currentSection)
}


function nextSection(nextSectionID, ...props) {
    
    const previous = document.querySelector('.section--active');
    currentSection = document.getElementById(nextSectionID);
    

    const [isComingBack] = props;
    if (! isComingBack === true) {
        sectionFlow.push(previous.id);
    }

    console.log(nextSectionID, flow);
    if ((nextSectionID === "professionalType" && flow === "professional") || 
        (nextSectionID === "info" && flow !== "professional")) {
        changeState(document.querySelector('.info'), {
            old: "inactive",
            new: "active"
        });
    } else {
        changeState(document.querySelector('.info'), {
            new: "inactive",
            old: "active"
        });
    }

    checkActionsVisibility( currentSection )
    
    changeState(previous, {
        new: "section--inactive",
        old: "section--active"
    });

    changeState(currentSection, {
        old: "section--inactive",
        new: "section--active"
    });
}

function changeState(section, state) {
    if (section.classList.contains(state.old)) {
        section.classList.replace(state.old, state.new);
        return
    } 
    section.classList.add(state.new);
}


function validateData(element) {

    let inputs = Array.from(element.querySelectorAll('input:not(.option)'));
    let options = element.querySelectorAll('.options');

    if (options.length >  0) {
        for (let i = 0; i < options.length; i++) {
            if (!options[i].getAttribute('data-required')) continue;

            let inputGroup = options[i].querySelectorAll('.option');

            if (inputGroup.length < 1) continue;

            if (checkCheckboxOptions(inputGroup) === false) return false;
        }
        
    }
    
    const password2 = element.querySelector("#userPasswordConfirmation");

    if (password2) {
        const password1 = element.querySelector("#userPassword");

        if (password1.value !== password2.value) {
            let c = element.querySelector(`.forms-control[for="${password2.id}"]`);
            changeState(c, {
                old: "inactive",
                new: "active"
            });
        }
    }

    if (inputs.length > 0) {
        for (let i = 0; i < inputs.length; i++) {
            
            let isValid =  true;

            const value  = inputs[i].value,
            isRequired = inputs[i].getAttribute('required'),
            pattern = inputs[i].getAttribute("pattern"),
            type = inputs[i].getAttribute('type');

            if(!isRequired) continue;

            if (! (type === "checkbox" || type === "radio") ){
                isValid = validateField(value, {isRequired, pattern});
            }
            
            if (type === "checkbox" || type === "radio") {
                isValid = (inputs[i].checked && isRequired); 
            }

            
            let formControl = element.querySelector(`.forms-control[for="${inputs[i].id}"]`);
            
            if (!isValid) {
                changeState(formControl, {
                    old: "inactive",
                    new: "active"
                });
                return false  
            } else {
                changeState(formControl, {
                    new: "inactive",
                    old: "active"
                });
            }
        }
    }

    return true;
}


function checkCheckboxOptions(inputGroup) { 
    let ret = false;
    inputGroup.forEach( (e) => {
        if ( e.checked ) ret = true;
    })
    return ret
}


function validateField(value, ...options) {

    let isValid = true;
    let pattern = options[0].pattern;
    let isRequired = options[0].isRequired;
    if (pattern) {

        pattern = pattern.slice(1, pattern.length - 2);

        let regxp = new RegExp(pattern);

        isValid = regxp.test(value)
    }

    if (isRequired && !value) isValid = false;

    return isValid;
}

function changeActionsValues(previousSection) {
    let backButton = document.querySelector('.actions__back');
    backButton.setAttribute("data-section", previousSection.id);
}


function checkActionsVisibility(section) {
    try {
        if (!flowMap.get(flow).get(section.id)) {
            changeState(forward, {
                new: "actions__forward--inactive",
                old: "actions__forward--active"
            });
        } else {
            changeState(forward, {
                old: "actions__forward--inactive",
                new: "actions__forward--active"
            });
        }
    } catch (error) {
        changeState(forward, {
            new: "actions__forward--inactive",
            old: "actions__forward--active"
        });
    }
    

    if (sectionFlow.length < 1) {
        changeState(back, {
            new: "actions__back--inactive",
            old: "actions__back--active"
        });
    } else {
        changeState(back, {
            old: "actions__back--inactive",
            new: "actions__back--active"
        });
    }

    if (back.classList.contains("actions__back--inactive") && forward.classList.contains("actions__forward--active") ) {
        document.querySelector(".actions").style.justifyContent = "end"
    } else {
        document.querySelector(".actions").style.justifyContent = "space-between"
    }
}