function Init(list_init) {
    var street = ""
    var list = []
    var len = list_init[0].length
    for (let pas = 0; pas < len; pas++) {
        list.push([list_init[0][pas][0], [], "", list_init[0][pas][1], 0])
    }
    list.push(list_init[1])
    street = "*** 3rd STREET ***"
    displayAction(list, street)
    nextButton = document.getElementById("nextButton");
    previousButton = document.getElementById("previousButton");
    nextStreet = document.getElementById("nextStreet");
    previousStreet = document.getElementById("previousStreet");
    return list
}

// HTML elements
var nextButton = document.getElementById("nextButton");
var previousButton = document.getElementById("previousButton");
var nextStreet = document.getElementById("nextStreet");
var previousStreet = document.getElementById("previousStreet");

// Index of the current action
var currentActionIndex = 0;

// Event for the next action button
nextButton.addEventListener("click", function () {
    currentActionIndex++;
    if (currentActionIndex >= actions.length - 1) {
        currentActionIndex = actions.length - 1;
        nextButton.disabled = true;
        nextButton.classList.add("disabled");
        nextStreet.disabled = true;
        nextStreet.classList.add("disabled");
    }
    if (currentActionIndex > 0) {
        previousButton.disabled = false;
        previousButton.classList.remove("disabled");
        previousStreet.disabled = false;
        previousStreet.classList.remove("disabled");
    }
    if (actions[currentActionIndex][0].slice(-1) == "*") {
        street = actions[currentActionIndex][0]
        update_pot(list)
    }
    if (currentActionIndex - 1 == 0) {
        street = "*** 3rd STREET ***";
    }
    updatelist(list, currentActionIndex)
    displayAction(list, street);

});

// Event for the previous action button
previousButton.addEventListener("click", function () {
    currentActionIndex--;
    if (currentActionIndex <= 0) {
        currentActionIndex = 0;
        previousButton.disabled = true;
        previousButton.classList.add("disabled");
        previousStreet.disabled = true;
        previousStreet.classList.add("disabled");
    }
    else if (currentActionIndex < actions.length - 1) {
        nextButton.disabled = false;
        nextButton.classList.remove("disabled");
        nextStreet.disabled = false;
        nextStreet.classList.remove("disabled");
    }
    if (actions[currentActionIndex][0].slice(-1) == "*") {
        update_pot(list)
        street = actions[currentActionIndex][0]
    }
    list = Init();
    for (let i = 0; i < currentActionIndex; i++) {
        updatelist(list, i)
    }
    updatelist(list, currentActionIndex)
    displayAction(list, street);
    nextButton = document.getElementById("nextButton");
    previousButton = document.getElementById("previousButton");
    nextStreet = document.getElementById("nextStreet");
    previousStreet = document.getElementById("previousStreet");
});
// Event for the next action Street
nextStreet.addEventListener("click", function () {
    currentActionIndex++
    updatelist(list, currentActionIndex)
    if (currentActionIndex >= actions.length - 1) {
        currentActionIndex = actions.length - 1;
        nextStreet.disabled = true;
        nextStreet.classList.add("disabled");
        nextButton.disabled = true;
        nextButton.classList.add("disabled");
    }


    else {
        if (currentActionIndex > 0) {

            previousStreet.disabled = false;
            previousStreet.classList.remove("disabled");
            previousButton.disabled = false;
            previousButton.classList.remove("disabled");
            while (actions[currentActionIndex][0].slice(-1) != "*" && currentActionIndex < actions.length - 1) {
                currentActionIndex++;
                updatelist(list, currentActionIndex)
                if (currentActionIndex >= actions.length - 1) {
                    currentActionIndex = actions.length - 1;
                    updatelist(list, currentActionIndex)
                    nextStreet.disabled = true;
                    nextStreet.classList.add("disabled");
                    nextButton.disabled = true;
                    nextButton.classList.add("disabled");
                }
            }
        }
    }
    updatelist(list, currentActionIndex)
    street = actions[currentActionIndex][0]
    update_pot(list)
    displayAction(list, street);


});

// Event for the previous action Street
previousStreet.addEventListener("click", function () {
    currentActionIndex--;
    if (currentActionIndex <= 0) {
        currentActionIndex = 0;
        previousStreet.disabled = true;
        previousStreet.classList.add("disabled");
        previousButton.disabled = true;
        previousButton.classList.add("disabled");
    }

    else {
        if (currentActionIndex < actions.length - 1) {
            nextStreet.disabled = false;
            nextStreet.classList.remove("disabled");
            nextButton.disabled = false;
            nextButton.classList.remove("disabled");
            while (actions[currentActionIndex][0].slice(-1) != "*" && currentActionIndex > 0) {
                currentActionIndex--;
                if (currentActionIndex <= 0) {
                    currentActionIndex = 0;
                    previousStreet.disabled = true;
                    previousStreet.classList.add("disabled");
                    previousButton.disabled = true;
                    previousButton.classList.add("disabled");
                }
            };

        }
    }
    list = Init();
    for (let i = 0; i < currentActionIndex; i++) {
        updatelist(list, i)
    }
    updatelist(list, currentActionIndex)
    update_pot(list)
    street = actions[currentActionIndex][0]
    displayAction(list, street);

});

// Disable the previous Street at the beginning
previousStreet.disabled = true;
previousStreet.classList.add("disabled");
// Disable the previous Street at the beginning
previousButton.disabled = true;
previousButton.classList.add("disabled");

function update_pot(list) {
    var len_list = list.length - 1;
    for (let i = 0; i < len_list; i++) {
        list[len_list] += list[i][4];
        list[i][3] -= list[i][4];
        list[i][4] = 0;
        if (list[i][2] != 'folds') {
            list[i][2] = "";
        }
    }

}
function updatelist(list, i) {
    var action = actions[i];
    var len_list = list.length - 1

    if (action != null) {
        var name = action[0];
        var done = action[1];

        for (let i = 0; i < len_list; i++) {
            if (list[i][0] == name) {
                list[i][2] = done;
                if (done == 'Dealt') {
                    list[i][1] = action[2];
                }
                else if (done == 'brings') {
                    list[i][4] = action[2];
                }
                else if (done == 'raises') {
                    list[i][4] = action[2];
                }
                else if (done == 'folds' || done == 'checks') {
                }
                else {
                    list[i][4] = list[i][4] + action[2];
                }
            }
        }
    }
}
function displayAction(list, street) {
    var i = 0
    var h = 2
    var actionHtml = "<div class = \"containerplayer\"> ";
    var len = list.length - 1
    for (let pas = 0; pas < 15; pas++) {
        if (pas == 4 || pas == 6 || pas == 8 || pas == 10 || pas == 14) {
            actionHtml += "<div class= \"vide\"></div>";
        }
        else if (pas == 7) {
            actionHtml += "<div class= \"pot\">" + list[len] + "</div>";

        }
        else if (pas == 0) {
            actionHtml += "<div class= \"vide\">" + street + "</div>";
        }
        else {
            var len1 = list[i].length - 1
            if (i < len && list[i][0] == "Hero") {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/1.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
            }
            else if (i < len && h == 2) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/2.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else if (i < len && h == 3) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/3.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else if (i < len && h == 4) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/4.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else if (i < len && h == 5) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/5.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else if (i < len && h == 6) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/6.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else if (i < len && h == 7) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/7.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else if (i < len && h == 8) {
                actionHtml += "<div class= \"player\"><div class=\"action\">" + list[i][2] + "</div><div class=\"bet\">" + list[i][len1] + "</div><div class=\"image\"><img src=\"{{ url_for('static', filename = 'Head/8.png') }}\" alt=\"caracter\"></div><div class=\"name\">" + list[i][0] + "</div><div class=\"chips\">" + list[i][3] + "</div><div class=\"cards\">" + displaycards(list[i][1]) + "</div></div>"
                i++;
                h++;
            }
            else {
                actionHtml += "<div class= \"vide\"></div>"
            }
        }
    };
    actionHtml += "</div>"
    tableContainer.innerHTML = actionHtml;
}
function displaycards(cards) {
    cards_string = ""
    for (let i = 0; i < cards.length; i++) {
        if (cards[i][1] == 0) {
            cards_string += "<div class=\"s\">&" + cards[i][0] + "</div>"
        }
        else if (cards[i][1] == 1) {
            cards_string += "<div class=\"h\">&" + cards[i][0] + "</div>"
        }
        else if (cards[i][1] == 2) {
            cards_string += "<div class=\"d\">&" + cards[i][0] + "</div>"
        }
        else if (cards[i][1] == 3) {
            cards_string += "<div class=\"c\">&" + cards[i][0] + "</div>"
        }
    }
    return cards_string;
}