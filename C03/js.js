const thingsToType = [
    "The quick brown fox jumps over the lazy dog.",
    "Rest in peace my granny she got hit by a bazooka, Yeah, I think about her every time I hit the hookah. Kaboom KABLOV, KabOOM..",
    "Kim Jong Un is a master of goon, Me and P Diddy had a sneaky sneaky-link, He showed me his super big ding-a-ling, Jeffery Epstein touched me when I was a teen",
    "I, the reviewer of this task is GAYYY!!!, Yes you said it right you are gayy.... Why are u gay?",
    "Hitler has only got one ball.. Goring has two but very small.. Himmler is rather sim'lar.. But poor old Goebbels has no balls at all.."
];

const box1 = document.getElementById('text-display');
const box2 = document.getElementById('text-input');
const s1 = document.getElementById('wpm');
const s2 = document.getElementById('accuracy');
const s3 = document.getElementById('timer');
const s4 = document.getElementById('mistakes');
const btn = document.getElementById('restart-btn');

let t = 60; 
let sec = 0;
let oopsies = 0;
let go = false;
let clock = null;

function doEverything() {
    clearInterval(clock);
    t = 60;
    sec = 0;
    oopsies = 0;
    go = false;
    
    s3.textContent = t;
    s1.textContent = 0;
    s2.textContent = 100;
    s4.textContent = 0;
    box2.value = "";
    box2.disabled = false;

    const randomStringTextWhatever = thingsToType[Math.floor(Math.random() * thingsToType.length)];
    box1.innerHTML = '';
    
    randomStringTextWhatever.split('').forEach(letter => {
        const span = document.createElement('span');
        span.classList.add('char');
        span.innerText = letter;
        box1.appendChild(span);
    });

    box1.childNodes[0].classList.add('current');
}

box2.addEventListener('input', () => {
    const list = box1.querySelectorAll('.char');
    const userString = box2.value;
    const userLetters = userString.split('');

    if (!go && userString.length > 0) {
        go = true;
        clock = setInterval(() => {
            if (t > 0) {
                t--;
                sec++;
                s3.textContent = t;
                
                const len = box2.value.length;
                const badCount = parseInt(s4.textContent);
                mathMagic(len, badCount);
            } else {
                stopEverything();
            }
        }, 1000);
    }

    let badOnes = 0;

    list.forEach((spanThingy, idx) => {
        const userLetter = userLetters[idx];

        spanThingy.classList.remove('correct', 'incorrect', 'current');

        if (userLetter == null) {
            if (idx === userLetters.length) {
                spanThingy.classList.add('current');
            }
        } else if (userLetter === spanThingy.innerText) {
            spanThingy.classList.add('correct');
        } else {
            spanThingy.classList.add('incorrect');
            badOnes++;
        }
    });

    mathMagic(userLetters.length, badOnes);

    if (userLetters.length === list.length) {
        stopEverything();
    }
});

function mathMagic(a, b) {
    if (a === 0) return;

    let score = ((a - b) / a) * 100;
    s2.textContent = Math.max(0, Math.round(score));
    s4.textContent = b;

    let min = sec / 60;
    if (min > 0) {
        let speed = (a / 5) / min;
        s1.textContent = Math.round(speed);
    }
}

function stopEverything() {
    clearInterval(clock);
    box2.disabled = true;
    go = false;
    box1.querySelector('.current')?.classList.remove('current');
}

btn.addEventListener('click', doEverything);
window.onload = doEverything;
