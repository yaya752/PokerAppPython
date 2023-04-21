function updateTable(tableJson,idtbody,idpot,idrake) {
    var table = JSON.parse(tableJson);
    var tbody = document.getElementById(idtbody);
    var potSpan = document.getElementById(idpot);
    var rakeSpan = document.getElementById(idrake);

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

        var tdChipsTable = document.createElement('td');
        tdChipsTable.textContent = player['ChipsOnTable'];

        tr.appendChild(tdName);
        tr.appendChild(tdHand);
        tr.appendChild(tdAction);
        tr.appendChild(tdChips);
        tr.appendChild(tdChipsTable);
        tbody.appendChild(tr);
    }
    potSpan.textContent = table.Pot;
    rakeSpan.textContent = table.Rake;
}