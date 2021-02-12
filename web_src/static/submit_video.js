fetch('/vdo_info', {
    method: 'GET',
    dataType: 'json'
})
.then(r => r.json())
.then(data => {
    nameofvideo = data.file_name
    document.getElementById("file_name").innerHTML = nameofvideo;
    console.log(data.file_name)
    if (data.file_name != 'None'){
        document.getElementById('submitBtn').disabled = false;
    }
    }
);

                              