function updateTable(tableJson) {
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
        if (player.Name = table.ManePlayer) {
            for (var j = 0; j < player.AllCards.length; j++) {
                var card = player.AllCards[j];
                cards.push(card.Value + card.Shape);
            }
        }
        else {
            for (var j = 0; j < player.CardSeen.length; j++) {
                var card = player.CardSeen[j];
                cards.push(card.Value + card.Shape);
            }
        }
        
        tdHand.textContent = cards.join(", ");

        var tdAction = document.createElement('td');
        tdAction.textContent = player['Action'];

        var tdChips = document.createElement('td');
        tdChips.textContent = player['Chips'];

        tr.appendChild(tdName);
        tr.appendChild(tdHand);
        tr.appendChild(tdAction);
        tr.appendChild(tdChips);
        tbody.appendChild(tr);
    }
    potSpan.textContent = table.Pot;
    rakeSpan.textContent = table.Rake;
}