var tableJson = document.currentScript.getAttribute('Table_json');
var tableJson = '{{ Table_json|safe }}';
var table = JSON.parse(tableJson);
var tbody = document.getElementById('table-body');
var potSpan = document.getElementById('pot');
var rakeSpan = document.getElementById('rake');

for (var i = 0; i < table.Players.length; i++) {
    var player = table.Players[i];
    var tr = document.createElement('tr');

    var tdName = document.createElement('td');
    tdName.textContent = player.Name;

    var tdHand = document.createElement('td');
    var cards = [];
    for (var j = 0; j < player.CardSeen.length; j++) {
        var card = player.CardSeen[j];
        cards.push(card.Value + card.Shape);
    }
    tdHand.textContent = cards.join(", ");

    tr.appendChild(tdName);
    tr.appendChild(tdHand);
    tbody.appendChild(tr);
}

potSpan.textContent = table.Pot;
rakeSpan.textContent = table.Rake;