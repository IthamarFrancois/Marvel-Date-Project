d3.csv("data.csv").then(function (data) {
    var heros = data;
    var button = d3.select('#button');
    var form = d3.select("#form");
    button.on("click", runEnter);
    form.on("submit", runEnter);


    
function runEnter() {
        
        d3.select('tbody').html("") 
        d3.event.preventDefault(); 
        inputValue = d3.select("#user-input").property("value");
        
        
        var filteredCODENAME = 
        heros.filter(sheros => sheros.CODENAME.includes(inputValue));
        console.log(filteredCODENAME)
        var output = filteredCODENAME

        
        for (var i = 0; i < filteredCODENAME.length; i++) 
        {
            d3.select("tbody").insert("tr").html(
            "<td>" + [i+1] + "</td>" +
            "<td>" + (output[i]['CODENAME'])+"</a>"+"</td>" + 
            "<td>" + (output[i]['GENDER'])+"</td>" +
            "<td>" + (output[i]['BIRTHPLACE'])+"</td>" +
            "<td>" + (output[i]['EXPERIENCE'])+"</td>" +
            "<td>" + (output[i]['RELATIONSHIP STATUS'])+"</td>") }
            };
});