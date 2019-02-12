var totRows = 0
var table = document.getElementById("list");



function addClicked(){
    var inputValue = document.getElementById("input-text").value;
    var row = table.insertRow(totRows)
    var cell1 = row.insertCell(0)
    var cell2 = row.insertCell(1)
    var cell3 = row.insertCell(2)

    if(inputValue !== ''){
        cell2.innerHTML = inputValue
        cell3.innerHTML = 'X'
        totRows++
        document.getElementById("input-text").value = ""

        cell2.onclick = function(){
            cell2.style.setProperty("text-decoration","line-through")
        }
        cell3.onclick = function(){
            var rowdel = cell3.parentNode.parentNode;
            row.parentNode.removeChild(row);
        }
        
        

    
    }
}


//delete row
var table = document.getElementsById('list');

function del(){
    var td = event.target.parentNode; 
    var tr = td.parentNode; // the row to be removed
    tr.parentNode.removeChild(tr);
}