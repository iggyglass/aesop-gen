const adjProb = 50; // Percentage (out of 100) that an adjective will be applied
const proProb = 1; // Percentage (out of 100) that a pronoun will be applied

var titleEl = document.getElementById("title");
var moralEl = document.getElementById("moral");

function generate() {
    titleEl.innerHTML = generateTitle();
    moralEl.innerHTML = getMoral();
}

function generateTitle() {
    let len = Math.floor(Math.random() * 3);

    if (len == 0) {
        return `The ${getAdjective()}${getNoun()}`;
    } else if (len == 1) {
        return `The ${getAdjective()}${getNoun()} and ${getPronoun()}${getAdjective()}${getNoun()}`;
    } else {
        return `The ${getAdjective()}${getNoun()}, ${getPronoun()}${getAdjective()}${getNoun()}, and ${getPronoun()}${getAdjective()}${getNoun()}`;
    }
}

function getMoral() {
    return data["morals"][Math.floor(Math.random() * data["morals"].length)];
}

function getNoun() {
    return data["nouns"][Math.floor(Math.random() * data["nouns"].length)];
}

function getAdjective() {
    return Math.floor(Math.random() * 100) <= adjProb ? data["adjectives"][Math.floor(Math.random() * data["adjectives"].length)] + " " : "";
}

function getPronoun() {
    return Math.floor(Math.random() * 100) <= proProb ? data["pronouns"][Math.floor(Math.random() * data["pronouns"].length)] + " " : "the ";
}

generate();