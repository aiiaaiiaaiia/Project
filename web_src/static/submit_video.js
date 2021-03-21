var inputlang = '';

fetch('/vdo_info', {
    method: 'GET',
    dataType: 'json'
})
.then(r => r.json())
.then(data => {
    var nameofvideo = data.title;
    console.log(nameofvideo)
    var vdo_name = document.getElementById("title");
    vdo_name.innerHTML = nameofvideo;
    console.log(data.title);
    console.log(inputlang);
    console.log(tranlang);
    if (data.title != 'None'){
        document.getElementById('submitBtn').disabled = false;
    };
    }
);
