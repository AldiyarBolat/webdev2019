var btn = document.getElementById("btnn");

btn.addEventListener("click", addClicked)

var totRows = 0
var table = document.getElementById("list")

function addClicked(){
    var inputValue = document.getElementById("input-text").value;
    var row = table.insertRow(totRows)
    var cell1 = row.insertCell(0)
    var cell2 = row.insertCell(1)
    

    if(inputValue !== ''){
        cell1.innerHTML = inputValue
        cell2.innerHTML = 'X'

        totRows++
        document.getElementById("input-text").value = ""

        cell1.onclick = function(){
            cell1.style.setProperty("text-decoration","line-through")
        }

        cell2.onclick = function(){
            var rowdel = cell2.parentNode.parentNode;
            row.parentNode.removeChild(row)
            totRows--
        }
    }
}

